---
title: "OpenCRVS"
source_url: "https://documentation.opencrvs.org/general/opencrvs"
markdown_url: "https://documentation.opencrvs.org/general/opencrvs.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:d0aceb13d9d2a136f09a27393bdee1c62574c7c08e3b1a99e37e117209b0c03c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/general/opencrvs.md).

# OpenCRVS

OpenCRVS is a free, open-source digital system purpose-built for civil registration and vital statistics (CRVS). It helps governments register life events — births, deaths, marriages and others — and produce the reliable vital statistics that underpin planning, legal identity and public services.

Unlike a generic database or a repurposed health or identity system, OpenCRVS is designed around civil registration itself and around the realities of delivering it: it works on low-cost devices, supports low-connectivity and offline working, and is built to reach every person, including the hardest to register.

{% hint style="info" %}
**A digital public good.** OpenCRVS is openly licensed and standards-based, designed to be adopted, configured and run by governments as part of their national Digital Public Infrastructure.
{% endhint %}

#### What makes OpenCRVS different

* **Purpose-built for CRVS** — modelled on civil registration processes, roles and legal requirements, not adapted from another domain.
* **Configurable** — each country defines its own events, forms, business rules, user roles, certificates and languages, without changing the core software.
* **Built for real conditions** — mobile-friendly, usable on modest hardware, and resilient to intermittent connectivity.
* **Interoperable** — integrates with identity, health, statistics and social-protection systems through open standards.
* **Inclusive by design** — focused on universal registration and on removing barriers for under-served populations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/general/opencrvs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
