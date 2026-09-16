---
title: "Infrastructure"
source_url: "https://documentation.opencrvs.org/v1.9/developers/infrastructure"
markdown_url: "https://documentation.opencrvs.org/v1.9/developers/infrastructure.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:2901f7a417b26d54f5bee59c8a1a3569699bef562dad9f35b1aeca61bc134168"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/developers/infrastructure.md).

# Infrastructure

The OpenCRVS infrastructure setup includes:

* **Ansible-based server provisioning automation** that transforms bare Ubuntu servers into production-ready application and backup servers.
* **Configuration files** for deploying services on Docker Swarm.
* **Deployment automation pipelines** implemented with GitHub Actions.

If you are deploying OpenCRVS for your country, it is critical to understand and adapt these processes and configurations to align with your government's IT environment.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/developers/infrastructure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
