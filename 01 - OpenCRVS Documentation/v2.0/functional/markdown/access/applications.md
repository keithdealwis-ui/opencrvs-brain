---
title: "Applications"
source_url: "https://documentation.opencrvs.org/functional/markdown/access/applications"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/access/applications.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3a75df47bfce76f3c4410b660a3c6bc7b7e85315e635cc08366e84dc5700fe75"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/access/applications.md).

# Applications

### 1. Introduction

In OpenCRVS, **Applications** describes how people access the system in practice:

* The **core OpenCRVS interface** that most registration staff use every day in their browser (or installed as a PWA).
* Optional **custom applications ("side apps")** that connect to the OpenCRVS backend eRegistry using APIs for specialised use cases.

This page explains when the core interface is sufficient, and when a country may decide to build additional side apps.

***

### 2. Core OpenCRVS interface

OpenCRVS provides a core web interface for registration staff, built as a responsive progressive web application (PWA) that works on mobile phones, tablets and desktop devices.

The core interface is the primary way that registrars and other authorised users interact with the eRegistry. It provides:

* **Event registration workflows** for births, deaths, marriages and other civil events, including notification, declaration, review, registration, correction and revocation.
* **Workqueues** that show users the records they need to work on, filtered by role, scope and location (for example: "New birth declarations to review" or "Corrections awaiting approval").
* **Search and retrieval** of registered records, with support for protected records and audit.
* **Offline working** so that users can capture and process records even when connectivity is unreliable, with actions queued in an Outbox and synchronised when a connection is available.
* **Outputs and communications**, such as printing certificates and certified copies, and sending SMS or email notifications when actions are completed.

The core interface runs in a browser and can be installed to a device home screen like an app. It is designed for day‑to‑day use by registration staff in offices, health facilities and mobile registration teams.

***

### 3. Custom applications ("side apps")

Although most business needs can be met using the core interface, countries may also develop custom applications that interact with the OpenCRVS backend eRegistry using standard APIs. These are often referred to as **"side apps"**.

Side apps:

* Are built and maintained outside the core OpenCRVS codebase.
* Use OpenCRVS APIs and authentication to read and write records in the eRegistry.
* Implement specialised user interfaces and workflows for specific use cases or user groups.
* Must follow the same data protection, security and audit requirements as the core interface.

Side apps are optional. They should only be introduced where there is a clear need that is not well served by the standard OpenCRVS interface.

#### 3.1 Example custom app: digitisation app for historical records

A common side app use case is **digitising old paper civil registration records**.

In this scenario:

* The country has a large volume of historical paper records (for example, birth and death registers stored in district offices or archives).
* A dedicated digitisation team is contracted to scan and capture these records into the OpenCRVS eRegistry.
* The team uses a custom digitisation app, designed for high‑throughput data entry and document capture.

A digitisation side app:

* Allows operators to **scan or photograph** pages from old paper registers.
* Provides **data entry forms** that map to the same event data model used by OpenCRVS, including mandatory and optional fields.
* Validates data locally and then **submits records via the OpenCRVS APIs** into the eRegistry as declarations or as directly registered events, depending on the agreed business rules.
* Records **who digitised each record and when**, so that audit trails remain complete.
* May support **batch processing**, so that many records from a single book or time period can be captured efficiently.

The digitisation app does not replace the core OpenCRVS interface. Instead, it complements it by providing a specialised tool for one task: converting historical paper records into structured, searchable digital records in the same eRegistry that serves routine day‑to‑day registration.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/access/applications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
