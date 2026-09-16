---
title: "Product roadmap"
source_url: "https://documentation.opencrvs.org/v1.3/general/product-roadmap"
markdown_url: "https://documentation.opencrvs.org/v1.3/general/product-roadmap.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8f9d25b1b02b673ffc6f4c80d35af53582a608600c485da0edb82985e4725499"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/general/product-roadmap.md).

# Product roadmap

#### Upcoming in v1.3 (available in August 2023)

* Marriage registration
* Advanced deduplication
* Track issuance of certificates
* Verify a certificate with QR
* Configurable performance dashboards with infographics
* Configure National ID: MOSIP, OSIA or other
* Configure user role types
* Capture informant signature to consent declaration submission
* Organisation chart view
* Configure informant sms notifications
* Configure login background image or colour

**Backlog items**\
Scope for 1.4 will be determined based on requirements from reference implementations and other requests. Get in touch via <team@opencrvs.org> to join the Product Council and specify your priority features.

* Divorce registration
* Foetal death registration flow
* Web portal for direct public services
* Certified copy application flow
* Verify a record (API)
* Verify a certificate (via QR code)
* Printed performance management reports
* Advanced configuration of forms, certificates, application settings and communications (during live operations)
* Integrated payments
* Delegated authority
* Validation overrides and approval (where outside normal bounds)
* Integrated learning modules
* Legacy data import support (digital / paper)
* Person centric views of vital events data
* Social protection system interoperability


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/general/product-roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
