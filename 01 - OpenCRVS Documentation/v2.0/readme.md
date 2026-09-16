---
title: "Welcome"
source_url: "https://documentation.opencrvs.org/readme"
markdown_url: "https://documentation.opencrvs.org/readme.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:84a581c33e8471ae5ec40b391bbcfb4e7e8bef0c55fe32f95683e2b0b49f5d02"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/readme.md).

# Welcome

### 1. Introduction

OpenCRVS is an open-source digital solution for civil registration and available as a Digital Public Good.

This functional documentation is written for **governments, business analysts, systems Integrators, and development partners** to design, configure, operate, and maintain an OpenCRVS system that meets your country's needs.

***

### 2. How to use this documentation

#### 2.1. Understanding CRVS and OpenCRVS

* **CRVS Systems:** Understand what effective digital CRVS looks like and the role that OpenCRVS can play

  👉 [Effective digital CRVS systems](/general/crvs-systems/publish-your-docs.md)
* **Value Proposition:** Learn why governments, Systems Integrators, and development partners are choosing OpenCRVS
* 👉 [Value Proposition](/general/opencrvs/value-proposition.md)

#### 2.2. Exploring OpenCRVS functionality

* **Product Specifications:** Detailed functional architecture and system capabilities

  👉 [Functional architecture](/functional/markdown.md)
* **Default Configuration:** Explore the OpenCRVS reference implementation for Farajaland

  👉 [Example: Farajaland](/implementation/example-farajaland.md)

#### 2.3. Technical implementation

* **Quick Start:** Run OpenCRVS on your laptop for development

  👉 [Quick Start](/technical/guides/installation/quick-start.md)
* **Architecture:** Understand how OpenCRVS works technically

  👉 [Technical architecture](/technical/architecture.md)
* **Configuration:** Technically configure OpenCRVS for your country context

  👉 [Configuration](/technical/guides/configuration.md)
* **Deployment:** Deploy a configured version of OpenCRVS to a server

  👉 [Deploy](/technical/guides/installation/deploy-set-up-a-server-hosted-environment.md)

#### 2.4. Project setup and planning

* **Setup:** Establish your OpenCRVS project and team

  👉 [Project planning](/implementation/your-opencrvs-project/project-planning.md)
* **Product Roadmap:** See what's coming next for OpenCRVS

  👉 [Product roadmap](/releases/roadmap.md)
* **Upgrading:** Update your instance to the latest OpenCRVS release

  👉 [Version upgrades](/technical/guides/version-upgrades.md)

{% hint style="info" %}
**Additional resource:** We recommend using this documentation in combination with the [CRVS Digitisation Guidebook](http://www.crvs-dgb.org/en/), which provides step-by-step guidance for countries to implement digitised systems and automated processes for CRVS.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/readme.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
