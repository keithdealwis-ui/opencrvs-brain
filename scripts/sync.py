#!/usr/bin/env python3
"""
One-command sync for the OpenCRVS Brain vault (KEI-733).

Pulls the complete currently-published OpenCRVS documentation via GitBook's
llms.txt catalogue and individual .md page endpoints, writes it as an
Obsidian-navigable Markdown corpus, and keeps a provenance manifest plus an
append-only sync log. Safe to re-run: unchanged pages are left untouched so a
repeat sync against an unchanged source produces no corpus diff.

Usage:
    python3 scripts/sync.py [--base-url https://documentation.opencrvs.org] [--concurrency 10]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "01 - OpenCRVS Documentation"
SYSTEM_DIR = ROOT / "99 - System"
REMOVED_DIR = SYSTEM_DIR / "removed"
MANIFEST_PATH = SYSTEM_DIR / "manifest.json"
SYNC_LOG_PATH = SYSTEM_DIR / "sync-log.md"
HOME_PATH = ROOT / "00 - Index" / "Home.md"

DEFAULT_BASE_URL = "https://documentation.opencrvs.org"
USER_AGENT = "OpenCRVS-Brain-Sync/1.0 (KEI-733; +https://documentation.opencrvs.org)"

CATALOGUE_LINE_RE = re.compile(
    r"^-\s*\[(?P<title>[^\]]+)\]\((?P<url>https://[^)]+\.md)\)(?::\s*(?P<desc>.*))?$"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def http_get(url: str, timeout: int = 30, retries: int = 3) -> bytes:
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last_err = e
    raise RuntimeError(f"GET {url} failed after {retries} attempts: {last_err}")


@dataclass
class CatalogueEntry:
    version: str
    title: str
    markdown_url: str
    description: str = ""

    @property
    def source_url(self) -> str:
        # GitBook serves the human-facing page at the same path without ".md".
        return self.markdown_url[:-3] if self.markdown_url.endswith(".md") else self.markdown_url

    @property
    def local_rel_path(self) -> str:
        # Strip scheme+host, keep the path exactly as published. Older
        # versions already carry their own "vX.Y/" prefix in the URL path
        # (matching the catalogue section they're under); the current
        # release (v2.0) is unprefixed. Normalise both to exactly one
        # version-named folder so paths never duplicate it.
        path = re.sub(r"^https://[^/]+/", "", self.markdown_url)
        prefix = self.version + "/"
        if path.startswith(prefix):
            path = path[len(prefix):]
        return str(Path("01 - OpenCRVS Documentation") / self.version / path)


def parse_catalogue(base_url: str) -> list[CatalogueEntry]:
    raw = http_get(f"{base_url}/llms.txt").decode("utf-8")
    entries: list[CatalogueEntry] = []
    current_version = None
    seen_urls = set()
    for line in raw.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            # The catalogue's trailing "Agent Instructions" boilerplate is
            # GitBook platform chrome, not a documentation version - stop there.
            if heading.lower().startswith("querying this documentation"):
                break
            current_version = heading
            continue
        if current_version is None:
            continue
        m = CATALOGUE_LINE_RE.match(line.strip())
        if not m:
            continue
        url = m.group("url")
        if url in seen_urls:
            continue
        seen_urls.add(url)
        entries.append(
            CatalogueEntry(
                version=current_version,
                title=m.group("title").strip(),
                markdown_url=url,
                description=(m.group("desc") or "").strip(),
            )
        )
    return entries


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"pages": {}}


def write_page(local_path: Path, entry: CatalogueEntry, content: str, retrieved_at: str, content_hash: str) -> None:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        "---\n"
        f"title: {json.dumps(entry.title)}\n"
        f"source_url: {json.dumps(entry.source_url)}\n"
        f"markdown_url: {json.dumps(entry.markdown_url)}\n"
        f"version: {json.dumps(entry.version)}\n"
        f"retrieved_at: {json.dumps(retrieved_at)}\n"
        f"content_hash: {json.dumps('sha256:' + content_hash)}\n"
        "---\n\n"
    )
    local_path.write_text(frontmatter + content, encoding="utf-8")


def fetch_one(base_url: str, entry: CatalogueEntry) -> tuple[CatalogueEntry, bytes | None, str | None]:
    try:
        data = http_get(entry.markdown_url)
        return entry, data, None
    except Exception as e:  # noqa: BLE001 - recorded, not raised, so one bad page can't kill the run
        return entry, None, str(e)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default=DEFAULT_BASE_URL)
    ap.add_argument("--concurrency", type=int, default=10)
    args = ap.parse_args()

    run_started_at = now_iso()
    print(f"[sync] fetching catalogue from {args.base_url}/llms.txt")
    entries = parse_catalogue(args.base_url)
    print(f"[sync] catalogue lists {len(entries)} pages across "
          f"{len(sorted({e.version for e in entries}))} versions")

    old_manifest = load_manifest()
    old_pages: dict = old_manifest.get("pages", {})
    new_pages: dict = {}

    unchanged, modified, new, failed = [], [], [], []

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = [pool.submit(fetch_one, args.base_url, e) for e in entries]
        for fut in concurrent.futures.as_completed(futures):
            entry, data, err = fut.result()
            rel_path = entry.local_rel_path
            if err is not None:
                failed.append({"title": entry.title, "markdown_url": entry.markdown_url, "error": err})
                # Preserve any prior manifest record so a transient fetch
                # failure doesn't get misreported as a removal.
                if rel_path in old_pages:
                    new_pages[rel_path] = old_pages[rel_path]
                continue

            content = data.decode("utf-8", errors="replace")
            content_hash = sha256_hex(content.encode("utf-8"))
            prev = old_pages.get(rel_path)
            local_path = ROOT / rel_path

            if prev and prev.get("content_hash") == f"sha256:{content_hash}" and local_path.exists():
                # Byte-identical to last sync: don't touch the file or its
                # retrieved_at, so a no-op sync produces zero corpus diff.
                new_pages[rel_path] = prev
                unchanged.append(rel_path)
                continue

            retrieved_at = run_started_at
            write_page(local_path, entry, content, retrieved_at, content_hash)
            new_pages[rel_path] = {
                "title": entry.title,
                "version": entry.version,
                "description": entry.description,
                "source_url": entry.source_url,
                "markdown_url": entry.markdown_url,
                "local_path": rel_path,
                "retrieved_at": retrieved_at,
                "content_hash": f"sha256:{content_hash}",
            }
            (modified if prev else new).append(rel_path)

    # Anything in the old manifest that the live catalogue no longer lists is
    # a removal. Never silently delete: move the file into a timestamped
    # archive folder under 99 - System/removed/ and record it in the log.
    removed = []
    current_rel_paths = set(new_pages.keys())
    stamp = run_started_at.replace(":", "").replace("-", "")
    for rel_path, record in old_pages.items():
        if rel_path in current_rel_paths:
            continue
        src = ROOT / rel_path
        if src.exists():
            dest = REMOVED_DIR / stamp / rel_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dest)
            # Clean up now-empty parent directories left behind in the corpus.
            parent = src.parent
            while parent != DOCS_DIR and parent.exists() and not any(parent.iterdir()):
                parent.rmdir()
                parent = parent.parent
        removed.append({"local_path": rel_path, **record})

    manifest = {"pages": new_pages}
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    corpus_changed = bool(new or modified or removed)
    write_sync_log_entry(run_started_at, entries, unchanged, modified, new, removed, failed)
    write_home(len(new_pages), corpus_changed, run_started_at)

    print(f"[sync] unchanged={len(unchanged)} modified={len(modified)} new={len(new)} "
          f"removed={len(removed)} failed={len(failed)}")
    if failed:
        print("[sync] pages that could not be fetched this run:")
        for f in failed:
            print(f"  - {f['title']} <{f['markdown_url']}>: {f['error']}")
    return 0


def write_sync_log_entry(run_started_at, entries, unchanged, modified, new, removed, failed) -> None:
    lines = [f"## {run_started_at}", ""]
    lines.append(
        f"- Catalogue pages: {len(entries)}  |  unchanged: {len(unchanged)}  |  "
        f"modified: {len(modified)}  |  new: {len(new)}  |  removed: {len(removed)}  |  "
        f"failed: {len(failed)}"
    )
    if new:
        lines.append("- New:")
        lines += [f"  - `{p}`" for p in sorted(new)]
    if modified:
        lines.append("- Modified:")
        lines += [f"  - `{p}`" for p in sorted(modified)]
    if removed:
        lines.append("- Removed (archived under `99 - System/removed/`, not deleted):")
        lines += [f"  - `{r['local_path']}` (was: {r.get('source_url', '')})" for r in removed]
    if failed:
        lines.append("- Failed to fetch this run (previous copy, if any, retained as-is):")
        lines += [f"  - `{f['title']}` <{f['markdown_url']}>: {f['error']}" for f in failed]
    lines.append("")

    SYSTEM_DIR.mkdir(parents=True, exist_ok=True)
    existing = SYNC_LOG_PATH.read_text(encoding="utf-8") if SYNC_LOG_PATH.exists() else "# Sync Log\n\n"
    SYNC_LOG_PATH.write_text(existing.rstrip("\n") + "\n\n" + "\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")


def write_home(page_count: int, corpus_changed: bool, run_started_at: str) -> None:
    # "Last sync" tracks when the corpus content last actually changed, not
    # merely when the sync command was last executed, so a no-op re-run
    # leaves Home.md byte-identical.
    state_path = SYSTEM_DIR / ".last-corpus-change"
    if corpus_changed or not state_path.exists():
        last_change = run_started_at
        state_path.write_text(last_change, encoding="utf-8")
    else:
        last_change = state_path.read_text(encoding="utf-8").strip()

    HOME_PATH.parent.mkdir(parents=True, exist_ok=True)
    HOME_PATH.write_text(
        "# OpenCRVS Brain\n\n"
        "V0 mirror of the currently published OpenCRVS documentation, as a local Obsidian vault.\n\n"
        "- **Source:** https://documentation.opencrvs.org/\n"
        f"- **Last corpus change:** {last_change}\n"
        f"- **Pages in corpus:** {page_count}\n"
        "- **Sync:** `python3 scripts/sync.py` (see repo README)\n\n"
        "## Where to start\n\n"
        "- [[01 - OpenCRVS Documentation]] — the mirrored documentation tree, one folder per published version.\n"
        "- `99 - System/manifest.json` — provenance for every page (source URL, markdown URL, retrieval time, content hash).\n"
        "- `99 - System/sync-log.md` — append-only record of every sync run.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    sys.exit(main())
