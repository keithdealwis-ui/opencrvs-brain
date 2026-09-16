---
title: "Why OpenCRVS?"
source_url: "https://documentation.opencrvs.org/general/opencrvs/why-opencrvs"
markdown_url: "https://documentation.opencrvs.org/general/opencrvs/why-opencrvs.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:fe5332619eda99cbb8ffb9fb2a388325a4c6a1ee88c48f730255d5c45f9f48cd"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/general/opencrvs/why-opencrvs.md).

# Why OpenCRVS?

### 1. Introduction

Civil registration is the foundation of legal identity and rights-based service delivery. A Civil Registration and Vital Statistics (CRVS) system records the details of all major life events, such as births, deaths, marriage, and divorce. It is an essential component of the "leave no one behind" agenda, and without it working effectively, it is virtually impossible to ensure inclusive growth.

### 2. The civil registration challenge

Unfortunately, in many countries CRVS systems are broken:

* **1 in 4 children** under the age of 5 have not had their birth registered and hence do not officially exist
* As a result, they struggle to access basic rights like education, healthcare, and social protection
* **Two thirds of the world's deaths** are not recorded, meaning governments cannot design effective public health policies or measure their impact

### 3. Common challenges faced by users

Through extensive research of CRVS systems around the world, we understand many of the specific challenges experienced by civil registration staff and families trying to register vital events:

**For families and informants:**

* Civil registration processes are bureaucratic and time-consuming, with requests for supporting documents that family members do not possess and unofficial payments
* Family members need to travel long distances to register vital events, with several trips often required before the registration process is complete and a certificate is obtained
* Systems are not integrated, so birth registration does not lead to automatic access to other rights such as vaccination programmes or enrolment in social protection schemes

**For civil registration staff:**

* Manual, paper-based processes are prone to errors, delays, and loss of records
* Limited visibility into registration backlogs, performance metrics, or data quality issues
* Fragmented systems that do not communicate with each other, requiring duplicate data entry and reconciliation


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/general/opencrvs/why-opencrvs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
