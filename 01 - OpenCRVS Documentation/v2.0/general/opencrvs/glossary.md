---
title: "Glossary"
source_url: "https://documentation.opencrvs.org/general/opencrvs/glossary"
markdown_url: "https://documentation.opencrvs.org/general/opencrvs/glossary.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:bd2aa57d379f5b1e8564a71b7dbf467b6cccc86b5f837e7a5708f1e8d79d8829"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/general/opencrvs/glossary.md).

# Glossary

OpenCRVS uses a consistent set of concepts across modules:

* **Event** – a civil registration event type such as birth, death, marriage, etc.
* **Record** – the data instance for a single event.
* **Notification** – a preliminary capture of event details that may form the basis of a formal declaration.
* **Declaration** – a formal statement that an event has taken place.
* **Registration** – the process by which an event record is reviewed and legally registered.
* **Certified copy / certificate** – an official document representing a registered event.
* **Informant** – the person who formally reports the event.
* **Workflow** – the ordered steps and rules that govern a record through its lifecycle.
* **Status** – the state of a record in the workflow (for example, Draft, Notified, Declared, Registered).
* **Action** – a user or system operation that changes a record or its status (for example, Notify, Declare, Validate, Register, Correct, Issue certificate).
* **Form** – the structured data capture for an event, defined by fields, conditional logic, and validations.
* **Business rule** – a configurable rule that validates data or controls workflow behaviour.
* **Administrative unit** – the organisational unit responsible for services for a specific area.
* **User / role** – the authenticated user and their permission set.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/general/opencrvs/glossary.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
