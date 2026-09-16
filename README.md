# OpenCRVS Brain — V0

A complete, reproducible local Markdown mirror of the currently published
[OpenCRVS documentation](https://documentation.opencrvs.org/), structured as
a Git-backed Obsidian vault.

This is **V0**: it establishes the canonical source corpus and a repeatable
sync only. It deliberately does not build capability extraction, a knowledge
graph, embeddings, tender matching, or any other derived intelligence — see
[KEI-733](https://linear.app/keith-de-alwis/issue/KEI-733) for the full
outcome and non-goals.

## What's here

```
OpenCRVS-Brain/
├── 00 - Index/
│   └── Home.md                          # Vault landing page (auto-generated)
├── 01 - OpenCRVS Documentation/
│   ├── v2.0/                            # Current release — unprefixed on the live site
│   ├── v1.9/ ... v1.3/                  # Older versions, still published side-by-side
├── 99 - System/
│   ├── manifest.json                    # Provenance for every page
│   ├── sync-log.md                      # Append-only record of every sync run
│   └── removed/<timestamp>/...          # Archived copies of pages GitBook has removed
├── scripts/
│   └── sync.py                          # The one-command sync
└── .obsidian/                           # Minimal vault config
```

The folder layout under `01 - OpenCRVS Documentation/` mirrors GitBook's own
`llms.txt` catalogue: one top-level folder per published documentation
version, then the page hierarchy exactly as published within it.

Every page is stored as Markdown with a small YAML frontmatter block added on
top (title, source URL, markdown URL, version, retrieval time, content hash).
The body below the frontmatter is the source Markdown byte-for-byte as
GitBook served it — nothing is rewritten, summarised, or otherwise modified.

## Initialise

```bash
git clone <this repo>
cd OpenCRVS-Brain
python3 scripts/sync.py
```

No dependencies beyond Python 3 (standard library only — `urllib`, no
`requests`/`pip install` needed).

## Sync

```bash
python3 scripts/sync.py
```

One command, safe to re-run at any time. Each run:

1. Fetches the current catalogue from `https://documentation.opencrvs.org/llms.txt`.
2. Fetches every listed page from its individual `.md` endpoint (GitBook's
   authoritative Markdown interface — not scraped HTML), in parallel.
3. Classifies every page as **unchanged**, **modified**, **new**, or
   **removed**, by comparing SHA-256 content hashes against
   `99 - System/manifest.json` from the last run.
4. Writes only what changed. An unchanged page's file, frontmatter and
   manifest entry are left byte-identical — a repeat sync against an
   unchanged source produces no corpus diff (verified below).
5. Never silently deletes. A page GitBook no longer publishes is moved out
   of the corpus into `99 - System/removed/<run-timestamp>/<original path>`
   (so it still exists in the repo and in Git history) and recorded in
   `99 - System/sync-log.md`.
6. Appends one dated entry to `99 - System/sync-log.md` summarising the run,
   and regenerates `00 - Index/Home.md`'s page count / last-change date.

Optional flags: `--base-url` (default `https://documentation.opencrvs.org`),
`--concurrency` (default `10`).

## Open in Obsidian

Open the repository root (`OpenCRVS-Brain/`) as a vault:
Obsidian → *Open folder as vault* → select this directory. `.obsidian/` is
already present and minimal, so it opens with no setup. Navigate via
`00 - Index/Home.md` or the file tree under `01 - OpenCRVS Documentation/`.

## Provenance

Every page in `99 - System/manifest.json` carries:

| Field | Meaning |
|---|---|
| `title` | Page title from the GitBook catalogue |
| `version` | Published documentation version (`v2.0`, `v1.9`, … `v1.3`) |
| `source_url` | The human-facing published page |
| `markdown_url` | The `.md` endpoint this content was fetched from |
| `local_path` | Path within this repo |
| `retrieved_at` | UTC timestamp this content was last actually fetched/changed |
| `content_hash` | `sha256:` of the exact bytes fetched |

The same fields (minus `local_path`, which is implicit) are duplicated as
YAML frontmatter at the top of each page, so provenance survives even if a
file is copied out of the vault.

## Evidence: V0 build (2026-09-16)

- **Pages ingested:** 1,270, across 8 published versions (v2.0, v1.9, v1.8,
  v1.7, v1.6, v1.5, v1.4, v1.3).
- **Fetch failures:** 0.
- **Repeat-sync idempotency:** a second `sync.py` run against the unchanged
  live source reported `unchanged=1270 modified=0 new=0 removed=0`, and
  `git status` after that run showed only the expected append to
  `99 - System/sync-log.md` — no documentation or manifest changes.
- **Pages that could not be represented faithfully:** none found in this
  run. GitBook's `.md` endpoints returned clean Markdown for every listed
  page.
- **Change-detection paths, all verified:**
  - *New*: the initial sync itself (`new=1270`).
  - *Unchanged*: the idempotent repeat sync above.
  - *Modified*: verified by forcing a stale `content_hash` on one real,
    already-ingested page and re-running `sync.py` — it was correctly
    reported as `modified` (not `new`), re-fetched, and its hash corrected;
    since the underlying page hadn't actually changed upstream, that
    synthetic run was reverted rather than committed.
  - *Removed*: verified by injecting a synthetic manifest entry/file for a
    page absent from the live catalogue and re-running `sync.py` — it was
    moved to `99 - System/removed/<timestamp>/...` (content preserved, not
    deleted), dropped from `manifest.json`, and logged in
    `99 - System/sync-log.md` with its former source URL; reverted after
    confirming, for the same reason.
- **Obsidian open:** structurally validated — every one of the 1,270 pages
  has well-formed YAML frontmatter (parsed and checked programmatically),
  the folder tree contains no path collisions, and `.obsidian/` is present
  with a minimal, valid config. `open`/the `obsidian://open?path=...` URI
  were used to ask the already-running Obsidian app to load this vault, but
  this session has no Screen Recording/Accessibility permission to confirm
  the resulting window visually — worth Keith opening it once himself to
  eyeball (`Obsidian → Open folder as vault` → this directory).

## Notes for the later capability layer (KEI-733 handover)

- The live site currently publishes **8 documentation versions
  simultaneously** (v1.3 through v2.0) under separate URL prefixes, all
  listed together in one `llms.txt`. Any future requirements/tender-matching
  layer will need to decide explicitly which version(s) are authoritative
  for a given engagement — older OpenCRVS deployments may still be running
  against v1.x behaviour that differs materially from v2.0.
- `llms.txt` already carries a short human-written description for many
  (not all) pages — a cheap, pre-existing summary signal worth reusing
  before generating new summaries downstream.
- GitBook's own catalogue ordering is a reasonable proxy for the intended
  reading/navigation order and could seed a future table-of-contents or
  chunking strategy without re-deriving structure from headings alone.
- Every page's `.md` endpoint response includes ~2 lines of identical
  GitBook platform boilerplate at the top (a pointer to `llms.txt`/the
  Markdown URL) and a longer identical "Agent Instructions" block at the
  bottom (GitBook's `?ask=` query API, unrelated to OpenCRVS). It has been
  **kept verbatim** in all 1,270 pages per the "do not rewrite or summarise
  source documentation" instruction — but it is pure repeated chrome, not
  OpenCRVS content, and a future capability layer should strip it (it's
  trivially identifiable: a leading `> For the complete documentation
  index...` blockquote and a trailing `# Agent Instructions` section) before
  doing anything semantic with page text.
