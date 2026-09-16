---
title: "Records"
source_url: "https://documentation.opencrvs.org/functional/markdown/records"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/records.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:964aa3a4732c4a73858c6d0240cb41b495d84531c33fc1de64fd44b5fd3a0672"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/records.md).

# Records

### Overview

The **Records** section focuses on the lifecycle and structure of individual event records in OpenCRVS.

It is organised into the following pages:

* **Record data** — describes the underlying data model for a record, including form data vs action metadata, and how Notify/Declare, Edit, and Correct all operate on the same event form.
* **Statuses** — explains the record status model (for example, Draft, Notified, Declared, Registered, Corrected), including which actions move a record between statuses and how status is used in workqueues and search.
* **Flags** — covers flags as additional workflow markers (for example, pending-attestation, correction-requested, protected) that complement status when a new status is not needed.
* **Certificates** — describes how registered records produce certificates and certified copies from configured templates, and how those outputs relate to the underlying record data and status.
* **Verifiable Credential** — explains how a registered record can produce a verifiable credential (VC), how it links back to the source record, and how it can be verified.
* **Protected data** — explains how some records or fields can be marked as protected, how this hides them from general search, and how access is controlled via protected search scopes.
* **Audit** — describes how every action on a record is written to the audit log, including who did what, where, and when, and how this supports accountability, investigations, and quality improvement.

These pages together show how OpenCRVS treats each event record as a journaled, auditable history from first notification through registration, correction, and output.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/records.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
