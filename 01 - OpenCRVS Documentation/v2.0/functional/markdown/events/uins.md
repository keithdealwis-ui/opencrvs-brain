---
title: "UINs"
source_url: "https://documentation.opencrvs.org/functional/markdown/events/uins"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/events/uins.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c580f7d8d94ff6604b2d04528f18f93a6a877f5ed4aa4d235710388a220898ce"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/events/uins.md).

# UINs

### 1. Introduction

In OpenCRVS, **UINs (Unique Identification Numbers)** are identifiers that make it possible to:

* Track a declaration during the registration process. (Tracking ID)
* Uniquely identify a registered event record. (Registration no)
* Optionally link a person in OpenCRVS to an external National ID system eg MOSIP. (National ID)

OpenCRVS supports multiple identifiers, each with a clear purpose and lifecycle.

***

### 2. Core identifiers managed by OpenCRVS

#### 2.1 Tracking ID

A **Tracking ID** is generated when a declaration is submitted.

* Used to follow the progress of a declaration (for example, from Notify → Declare → Validate → Register).
* Can be shared with the informant in SMS or email notifications.
* Can be printed on receipts or acknowledgement slips.
* Does not change if the declaration is updated before registration.

#### 2.2 Registration number

A **Registration number** is generated when a declaration is successfully registered.

* Uniquely identifies the **registered event record**.
* Can appear on certificates and certified copies.
* Can be used in searches, verifications, and integrations with other systems (for example, statistics, health, ID systems).
* Remains stable even if corrections are applied to the record (subject to country policy).

Both identifiers can be formatted to match country standards (for example, include year, office code, serial number).

***

### 3. Integration with National ID systems

OpenCRVS can integrate with an external **National ID system** such as MOSIP.

#### 3.1 Creating a National ID on registration

For eligible events (typically **births**), OpenCRVS can:

* Send key data from the registered record to the National ID system.
* Request creation of a **National ID** for the person.
* Store the returned National ID on the record for future use (for example, verification, updates).

Eligibility rules (for example, “at least one parent must be a citizen”) are configured as **business rules** and can differ by country.

#### 3.2 Revoking or updating National ID on death

For **death registrations**, OpenCRVS can:

* Notify the National ID system that a person has died.
* Request deactivation or status update of the National ID, depending on integration design.

This helps keep identity systems and civil registration aligned and reduces identity fraud.

***

### 4. Configuration overview

Key configuration points for UINs include:

* **Formats**
  * How Tracking IDs and Registration numbers are structured (for example, office code + year + sequence).
  * Which parts are human-readable vs system-generated.
* **When generated**
  * Tracking ID: on declaration submission.
  * Registration number: on successful registration.
  * National ID: on registration of eligible events, if integrated.
* **Where displayed**
  * In the UI (search results, record views, review screens).
  * On certificates, certified copies, and receipts.
  * In notifications sent to informants.

By clearly defining and configuring UINs, countries can ensure that every record is traceable, every certificate can be verified, and integrations with other national systems remain consistent.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/events/uins.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
