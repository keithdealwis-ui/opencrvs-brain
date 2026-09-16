---
title: "Events"
source_url: "https://documentation.opencrvs.org/functional/markdown/events"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/events.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:cd9421e0ecb03e1d703773b71b2703596b31c51d2349ada6fcd43b8356d4aae8"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/events.md).

# Events

## Overview

As part of the **Functional Architecture**, the **Events** section describes the events module in OpenCRVS — how different civil event types are modelled and configured.

It is organised into the following modules:

* **Types** — describes how event types (for example, birth, death, marriage) are defined and linked to forms, statuses, actions, and outputs.
* **Business Rules** — shows how legislation and policy are translated into configurable rules that control which actions are available, when declarations become late, when approvals are required, and related behaviour.
* **Forms** — explains how event forms are configured to capture Notify/Declare, Correct, and other action data, including pages, fields, validations, and evidence uploads.
* **UINs** — describes how unique identifiers (for example, Tracking ID, Registration number, National ID integration) are generated or captured for events and how they are used across workflows and search.

Together, these modules show how to configure each event type so that it reflects national law and policy while using a consistent model across OpenCRVS.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/events.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
