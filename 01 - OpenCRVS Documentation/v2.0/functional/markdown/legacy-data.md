---
title: "Legacy data"
source_url: "https://documentation.opencrvs.org/functional/markdown/legacy-data"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/legacy-data.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:428d9741ea77d48c01e709293f6ae4abe3f8529c38315221d418ed83cce24e94"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/legacy-data.md).

# Legacy data

Legacy data covers OpenCRVS capabilities for bringing historical civil registration records into the eRegistry.

There are two related capabilities:

* [Data migration](https://documentation.opencrvs.org/v2.0/functional/markdown/legacy-data/data-migration) — for historical records that already exist in a digital source, such as a previous CRVS database, spreadsheet, or another electronic register.
* [Digitise paper records](https://documentation.opencrvs.org/v2.0/functional/markdown/legacy-data/digitise-paper-records) — for historical records that exist only in physical sources, such as register books, certificate counterfoils, bound volumes, or archive files.

Both capabilities aim to make historical civil registration records usable in OpenCRVS for search, certified copies, correction, reporting, audit and interoperability, subject to the same record lifecycle, access control and configuration principles as records created in OpenCRVS.

These Functional Architecture pages describe what OpenCRVS supports and the principles that apply. For project planning and readiness activities, see [Migrate legacy data](https://documentation.opencrvs.org/v2.0/implementation/your-opencrvs-project/migrate-legacy-data). For technical implementation guidance, see [Legacy Data migration](https://documentation.opencrvs.org/v2.0/technical/guides/data-migration).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/legacy-data.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
