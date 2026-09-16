---
title: "Status Flow Diagram"
source_url: "https://documentation.opencrvs.org/v1.9/product-specifications/status-flow-diagram"
markdown_url: "https://documentation.opencrvs.org/v1.9/product-specifications/status-flow-diagram.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:09928330c35385d420e146f4c703541195706fb40659836b276c6f61d780a2e0"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/product-specifications/status-flow-diagram.md).

# Status Flow Diagram

The status flow diagram shows all the vital event record statuses and record flags in OpenCRVS and how it is possible to move from one to the next.\\

**Statuses**:\
A record status describe the primary legal status of a record, control what actions can be performed and can be used to filter custom workqueues:

* Draft
* Notified
* Declared
* Archived
* Validated (Deprecated in 1.10. Will become a record flag)
* Registered

\
**Flags:**\
A record flag can be thought of as a secondary record status. It describes additonal characteristics of a declared or registered record, control what actions can be performed and can be used to filter custom workqueues.

* Rejected
* Potential duplicate
* Pending certification
* Correction requested
* Duplicate\\

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-591fcd3c1095d9a88da86a501f070ae5d7e5e0c2%2FStatus%20WorkFlow%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/product-specifications/status-flow-diagram.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
