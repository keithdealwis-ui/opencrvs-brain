---
title: "Contributing"
source_url: "https://documentation.opencrvs.org/v1.7/developer/contributing"
markdown_url: "https://documentation.opencrvs.org/v1.7/developer/contributing.md"
version: "v1.7"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:1edf5028ab0125ac942b6c803b04bdfceb7bbefd4283be9d45f8ecf79f816324"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.7/developer/contributing.md).

# Contributing

This documentation is intended for developers working daily as part of the OpenCRVS Core team, as well as external contributors who wish to contribute occasionally.

Here you’ll find documentation on our best practices, developer workflows, and the automation we use for feature development, bug fixing, and other day-to-day development tasks.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.7/developer/contributing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
