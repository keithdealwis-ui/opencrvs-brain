---
title: "Toolkit"
source_url: "https://documentation.opencrvs.org/technical/apis/toolkit"
markdown_url: "https://documentation.opencrvs.org/technical/apis/toolkit.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:99cb1e9b1588aacf76e42f273f0be2a1425d23c9e1858737ee53638934727e52"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis/toolkit.md).

# Toolkit

The toolkit is the primary dependency for building OpenCRVS country configurations. It exposes typed builders and helpers for defining events, forms, conditional logic, deduplication rules, and advanced search.

The toolkit version must match your OpenCRVS Core version exactly. If you are running OpenCRVS 2.0.0, install `@opencrvs/toolkit@2.0.0`.

```bash
npm install @opencrvs/toolkit@2.0.0
```

When upgrading OpenCRVS to a new version, upgrading the toolkit first is a good starting point. Type errors and breaking changes in your country configuration surface immediately at compile time, so you can address any required configuration updates before deploying.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis/toolkit.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
