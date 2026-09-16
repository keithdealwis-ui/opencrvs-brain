---
title: "Data functions"
source_url: "https://documentation.opencrvs.org/v1.8/product-specifications/data-functions"
markdown_url: "https://documentation.opencrvs.org/v1.8/product-specifications/data-functions.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ce962439edd25ecb7c6bcaf74858620d6326e580e98ebff95d535a50fb6eaac6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/product-specifications/data-functions.md).

# Data functions

Overview of functionality that transforms legacy data.

<table><thead><tr><th>Functions</th><th width="427.6666666666667">Description</th></tr></thead><tbody><tr><td>Legacy data import</td><td>Import legacy digital data for ongoing use</td></tr><tr><td>Legacy paper import</td><td>Import paper records for ongoing use</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/product-specifications/data-functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
