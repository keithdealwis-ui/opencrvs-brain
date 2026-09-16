---
title: "Roadmap"
source_url: "https://documentation.opencrvs.org/v1.6/general/product-roadmap"
markdown_url: "https://documentation.opencrvs.org/v1.6/general/product-roadmap.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8cc505510e187e8e3875e1788e462fb0d276f5b392cd48ccb4f912104317304d"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/general/product-roadmap.md).

# Roadmap

Scope for future releases is determined based on requirements from reference implementations and community requests. Get in touch via [team@opencrvs.org ](mailto:team@opencrvs.org)to join the Product Council and specify your priority features.

The current product roadmap is available in Github Projects here:

[**Product roadmap**](https://github.com/orgs/opencrvs/projects/4/views/25)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/general/product-roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
