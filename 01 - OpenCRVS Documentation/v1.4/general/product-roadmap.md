---
title: "Product roadmap"
source_url: "https://documentation.opencrvs.org/v1.4/general/product-roadmap"
markdown_url: "https://documentation.opencrvs.org/v1.4/general/product-roadmap.md"
version: "v1.4"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ef1bb7a02d426b5913b60c61b1d655dbed74e2212a4ec6ece1ce9671c6de04e6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.4/general/product-roadmap.md).

# Product roadmap

Scope for 1.5 and 1.6 will be determined based on requirements from reference implementations and other requests. Get in touch via <team@opencrvs.org> to join the Product Council and specify your priority features.

* Divorce registration
* Foetal death registration flow
* Web portal integration for public access to civil registration services
* Certified copy application flow
* Digitisation of paper records
* Correct record requests / approvals
* Supervisory offices
* Printed performance management reports
* Advanced configuration of forms, certificates, application settings and communications (during live operations)
* Integrated payments
* Delegated authority
* Validation overrides and approval (where outside normal bounds)
* Integrated learning modules
* Person centric views of vital events data
* Creation of certificates as verifiable credentials


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.4/general/product-roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
