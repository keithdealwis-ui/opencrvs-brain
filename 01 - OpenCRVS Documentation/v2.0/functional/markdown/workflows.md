---
title: "Workflows"
source_url: "https://documentation.opencrvs.org/functional/markdown/workflows"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/workflows.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ffbb48961bd8de4806488d8282b6ee70412d2afbb5a226e8e9074143b8177f63"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/workflows.md).

# Workflows

### Overview

As part of the **Functional Architecture**, the **Workflows** section describes the workflow module in OpenCRVS — how records move through the system and how users interact with them at each step.

It is organised into the following modules:

* **Administrative Structure** —
* **Users** — describes how user roles, scopes, and jurisdictions determine who can see which records and perform which actions in a workflow.
* Jurisdictions
* **Actions** — explains the building blocks of workflows: the actions users can take on a record (for example, Notify, Declare, Register, Correct), how actions change status and flags, and how custom actions are configured.
* **Workqueues** — covers how records are surfaced to users as work items, using filters, assignment, and queue configuration to support day-to-day operations (review, validation, approval, certification).
* **Offline working** — describes how users can continue workflow steps when offline, including assignment, Outbox behaviour, and how offline actions are synchronised and audited.
* **Deduplication** — explains how OpenCRVS detects and manages potential duplicate records, and how review actions (Mark as duplicate / Mark not duplicate) fit into the overall record workflow.
* **Comms** — describes how communications (SMS, email) are triggered from actions in the workflow, for example sending notifications to informants when a record is registered, rejected, or requires correction.

These modules together show how to translate country business rules into concrete, action-driven workflows in OpenCRVS.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/workflows.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
