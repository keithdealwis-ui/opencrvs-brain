---
title: "Advanced search"
source_url: "https://documentation.opencrvs.org/functional/markdown/search/advanced-search"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/search/advanced-search.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:2d15eab7b972d3a50a60c26505ee7f16834c96b069ea2ec6e48877849e9def7f"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/search/advanced-search.md).

# Advanced search

### 1. Introduction

In OpenCRVS, **advanced search** provides a structured way to search for event records using multiple data points when the user does not have a unique identifier.

Advanced search:

* Uses fields from the event data (for example, names, dates, locations) to narrow down results.
* Respects the same **scopes, roles, and jurisdictions** that apply elsewhere in the system (users only see records they are authorised to see).
* Complements **quick search**, which is optimised for simple keyword or ID lookups.

Typical use cases include:

* A Registrar searching for a birth record with only the child’s name and approximate date of birth.
* A Registration Agent locating a declaration using the mother’s details and place of birth.
* Staff investigating potential duplicates or historical records without a Tracking ID.

***

### 2. Feature overview

Advanced search provides a **flexible, form-based way** to find records when strong identifiers are not available.

#### Core capabilities

With advanced search, OpenCRVS supports:

* **Multi-field search** using names, dates, locations, and other event data.
* **Configurable search forms** per event type, grouped into logical sections (for example, registration, child, mother, father).
* **Scope- and jurisdiction-aware results**, aligned with the wider access control model.
* Efficient triage and investigation when users only have partial or approximate information.
* Complementary behaviour with **quick search**, so users can move between identifier-based and data-based search.

Advanced search is:

* **Form-driven** — users fill in structured fields rather than entering free text.
* **Filter-friendly** — supports narrowing down large datasets using combinations of criteria.
* **Policy-aligned** — fields and visibility can be configured to respect privacy and governance rules.

***

### 3. Configuration overview

Advanced search is **configurable per event type** (for example, birth, death, marriage). Configuration defines:

* Which fields appear on the **advanced search form**.
* How those fields are grouped (for example, Registration details, Child’s details, Mother’s details).

Key principles:

* Only include fields that help meaningfully narrow down results.
* Avoid including sensitive fields that are not needed for search.
* Ensure configuration is aligned with country policy on who may search for which records.

#### Access control and scopes

Quick search & advanced search is always subject to the standard access control model:

* Users only see records that their **scopes and jurisdictions** allow.
* Search results never include records outside the user’s permitted scope, even if the identifier matches

Access to search (quick search and advanced search) is controlled by **search scopes** on the user’s role.

* `search[event=<event> placeOfEvent=my-administrative-area]` where `<event>` is the relevant event type (for example, `birth`, `death`, `marriage`).

To learn more about users scopes please refer to Users, Jurisdictions

***

### 4. Worked example

Below is an example of how advanced search for birth records might be configured.

**Business requirement:**

Users can perform an advanced search for birth records based on registration, child, mother and father details

#### Configuration input

| Section                  | Data                            | ... |
| ------------------------ | ------------------------------- | --- |
| **Registration details** | Record status                   |     |
|                          | Place of registration           |     |
|                          | Date of registration            |     |
|                          | Time period since status change |     |
|                          |                                 |     |
| **Child’s details**      | First name(s)                   |     |
|                          | Last name                       |     |
|                          | Date of birth                   |     |
|                          | Place of birth                  |     |
|                          |                                 |     |
| **Mother’s details**     | First name(s)                   |     |
|                          | Last name                       |     |
|                          | Date of birth                   |     |
|                          |                                 |     |
| **Father’s details**     | First name(s)                   |     |
|                          | Last name                       |     |
|                          | Date of birth                   |     |
|                          |                                 |     |
|                          |                                 |     |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/search/advanced-search.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
