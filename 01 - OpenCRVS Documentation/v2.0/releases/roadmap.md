---
title: "Roadmap"
source_url: "https://documentation.opencrvs.org/releases/roadmap"
markdown_url: "https://documentation.opencrvs.org/releases/roadmap.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b7899386684323ab53ea2a345e5c0342d1ecf3d716630806aa221d35cf0a7617"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/releases/roadmap.md).

# Roadmap

### 1. Introduction

The OpenCRVS roadmap provides visibility into planned features and release timelines. This helps implementation partners, governments, and the OpenCRVS community plan their implementations and understand when specific capabilities will become available.

The roadmap is primarily determined based on confirmed system requirements coming from current and future OpenCRVS implementations, ensuring that development priorities align with real-world needs.

***

### 2. Release Schedule

This website provides an overview of projected delivery dates for future releases.

{% hint style="info" %}

### **📆 Dates are indicative**

All dates provided are subject to change, however OpenCRVS Product Management makes every effort to provide accurate estimates to support implementation planning.
{% endhint %}

{% embed url="<https://roadmap.opencrvs.org/>" %}

#### Release types

* **Beta release** — Made available after initial QA testing, but before full regression testing has been commenced. It is not intended for live use in a production environment, however it allows accredited implementation partners to test out sample configurations and to contribute to the release testing effort.
* **Full release** — Production-ready release that has passed full regression testing and is ready for live use.

***

### 3. Future product scope

Future releases are expected to evolve based on implementation feedback, country priorities, and emerging technical or regulatory requirements. The items outlined in this section represent potential areas of enhancement and should be treated as indicative rather than committed scope.

<table><thead><tr><th width="358.7999267578125">Area</th><th>Description</th></tr></thead><tbody><tr><td>Workflow Configuration</td><td>Enable configurable form fields on core actions and and provide greater control over record flag management during notification workflows</td></tr><tr><td>Notification Management</td><td>Add notification-based filtering to scopes, enabling records to be filtered by where notifications were issued and by the user who issued them</td></tr><tr><td>Platform Modernisation</td><td>Modernise the platform by removing deprecated components and improving long-term maintainability</td></tr><tr><td>Versioning of Administrative Structure and Locations</td><td>Allow administrative boundaries and locations to change over time without affecting the accuracy of existing civil registration records</td></tr><tr><td>Protected Records</td><td>Allow sensitive records to be marked as protected, making them hidden from standard searches and accessible only to authorised users.</td></tr></tbody></table>

***

### 4. How Roadmap Priorities Are Determined

Roadmap priorities are informed by:

* Requirements from active country implementations
* Feedback from implementation partners
* Community feature requests
* Strategic product objectives
* Technical platform improvements

***

### 5. Influence the Roadmap

Get in touch via [OpenCRVS GitHub Discussions](https://github.com/opencrvs/opencrvs-core/discussions/categories/feature-requests) to share your priority feature requests.

Your input helps us:

* **Prioritise features** that solve real-world problems
* **Understand use cases** that drive design decisions
* **Align releases** with implementation timelines
* **Build capabilities** that work across different country contexts

***

### 6. Stay informed

To stay up to date with OpenCRVS releases and roadmap changes:

* **GitHub Discussions** — Follow feature request discussions and provide feedback
* **Release notes** — Review detailed release notes for each version


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/releases/roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
