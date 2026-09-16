---
title: "Functional Architecture"
source_url: "https://documentation.opencrvs.org/v1.9/product-specifications/functional-architecture"
markdown_url: "https://documentation.opencrvs.org/v1.9/product-specifications/functional-architecture.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:154107e0c42c7cee157f206b0c4cfefe5f8878bce6117c1934efa6bb2d4c0f1a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/product-specifications/functional-architecture.md).

# Functional Architecture

OpenCRVS 1.9 is a major rewrite to support the configuration of any number of civil events with existing core, support and admin functions.\
\
It is seen as a stepping stone to supporting in OpenCRVS 2.0 (with this a new functional architecture will be shared):

* custom business process record workflows (eg. attestation, senior approvals, escalations)
* hierarchy of offices and jurisdictions (control what records users can view and action)
* verifiable credentials

{% embed url="<https://www.loom.com/share/b2f1a094d3e64450a16c9d201e0cb677>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/product-specifications/functional-architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
