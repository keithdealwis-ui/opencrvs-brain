---
title: "Type"
source_url: "https://documentation.opencrvs.org/functional/markdown/events/type"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/events/type.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f6d79075b145a0eda4c5dae73c16189a24edb2cd0f8ac2a6bdf224aff21c7406"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/events/type.md).

# Type

### 1. Introduction

In OpenCRVS, an **event type** represents a kind of civil event that can be declared, registered, and certified. Each event type:

* Relates to one or more specific people (for example, child, mother, spouse, deceased).
* Occurs on a specific date (and optionally at a specific time and place).
* Has a set of data fields that describe what happened (for example, cause of death, place of birth).

OpenCRVS is not limited to births and deaths. Any civil event that can be clearly defined in terms of **who** it affects and **when** it occurred can be modelled as an event type.

***

### 2. Examples of civil event types

Common examples of civil events that can be configured in OpenCRVS include:

* Birth
* Death
* Stillbirth
* Foundling
* Marriage
* Divorce
* Adoption
* Legitimation
* Recognition
* Name change
* Address change

Countries can choose which event types to enable and how to name them, based on their legal framework and CRVS policy.

***

### 3. Configuring event types in OpenCRVS

Each event type can be configured to match country requirements. At a high level, configuration covers:

* **Forms and data**
  * Which fields are captured (for example, parents’ details, cause of death, place of marriage).
  * Which fields are mandatory vs optional.
* **Workflows and approvals**
  * Which record actions are available (for example, Notify, Declare, Validate, Register, Correct).
  * What deduplication checks should run.
  * Which workqueues surface records for review.
* **Roles, scopes, and jurisdiction**
  * Which user roles can create, review, approve, or correct records for that event type.
  * Jurisdiction rules based on event location, declared-in, or registered-in.
* **Outputs and post-registration steps**
  * Certificate templates for each event type.
  * Optional integrations such as verifiable credentials.

This configuration model allows a country to support **all relevant civil events** in a consistent way, while tailoring details to national law and practice.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/events/type.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
