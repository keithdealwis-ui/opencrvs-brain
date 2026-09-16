---
title: "Operational support"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/operational-support"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/operational-support.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ce04a6684bffcc27e489b61c488a9eb92eb8fc2099c31cabf95ded01d0b3f495"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/operational-support.md).

# Operational support

### 1. Introduction

Operational support is the ongoing management and maintenance of the OpenCRVS solution to ensure its continued successful operation. A well-structured support model ensures that users can resolve issues quickly, that common problems are identified and addressed, and that the system remains stable and available.

This section describes a tiered support model that can be adapted to the country context, ensuring that issues are resolved at the appropriate level and escalated when necessary.

***

### 2. Support model overview

A tiered support model provides clear pathways for issue resolution, from self-service options through to expert technical support.

#### Benefits of a tiered support model

* **Efficiency** — users can resolve simple issues themselves without waiting for support.
* **Scalability** — first-line support can handle common issues, freeing expert resources for complex problems.
* **Visibility** — issue tracking provides insight into common problems and training needs.
* **Clear escalation** — issues are escalated to the appropriate level based on complexity.

A typical support model includes four tiers, from self-service through to expert support.

***

### 3. Support tiers

#### 3.1 Level 0: Self-service options

Self-service options allow end-users to find answers to common questions and resolve simple issues without contacting support.

**What to provide:**

* **User guides and handbooks** — paper or digital guides covering common tasks and workflows.
* **Online support materials** — searchable documentation and FAQs.
* **Chatbots** — automated tools that answer simple questions.
* **Country-specific materials** — update generic User Support Materials with details of your country configuration.

**Benefits:**

* Users can resolve issues immediately, any time of day.
* Reduces the volume of support requests to first-line support.
* Empowers users to find answers independently.

#### 3.2 Level 1: First-line support

First-line support provides a mechanism for users to raise issues or questions that they have not been able to resolve themselves.

**What to provide:**

* **Easy-to-use contact channels** — WhatsApp, email, phone, or other instant communication tools.
* **Issue tracking system** — use a ticket tracking tool such as [GitHub](https://github.com/), Jira, or similar to log and track issues to resolution.
* **Response and resolution targets** — define service level agreements for how quickly issues should be acknowledged and resolved.

**Benefits:**

* Users have a clear way to get help when they need it.
* Issue tracking provides visibility into common problems and patterns.
* Patterns in user issues can inform follow-up training or improvements to user support materials.

**Example tools:**

* GitHub Issues for tracking
* Zendesk or Freshdesk for helpdesk management
* WhatsApp Business for communication

#### 3.3 Level 2: Technical support

Technical support handles issues that cannot be resolved through first-line support, typically requiring deeper technical knowledge or configuration changes.

**What to provide:**

* **Management and maintenance team** — technical staff who can investigate and resolve issues that require system access or configuration changes.
* **Access to production environments** — ability to review logs, check configurations, and make basic technical fixes.
* **Escalation procedures** — clear criteria for when issues should be escalated to expert support.

**Typical issues handled at this level:**

* Configuration issues (forms, workflows, certificates).
* User account management and permissions.
* Performance or connectivity problems.
* Data quality issues requiring investigation.

#### 3.4 Level 3: Expert support

Expert support provides resolution for issues that cannot be resolved by level 2 support, typically requiring fixes to the OpenCRVS Core Product or deep technical expertise.

What to provide:

* **Expert technical team** — core product developers or senior engineers with deep knowledge of the OpenCRVS codebase.
* **Bug fixes and patches** — ability to diagnose and fix bugs in the core product.
* **Upgrade management** — coordinated rollout of fixes and updates to all instances.

**Typical issues handled at this level:**

* Bugs in the OpenCRVS Core Product.
* Security vulnerabilities.
* Complex performance or scalability issues.
* Core product feature requests or enhancements.

***

### 4. Escalation and issue tracking

Clear escalation paths ensure that issues are resolved at the appropriate level and tracked to completion.

#### 4.1 Escalation criteria

Issues should be escalated when:

* **Level 0 → Level 1** — the user cannot find the answer in self-service materials.
* **Level 1 → Level 2** — the issue requires technical investigation or configuration changes.
* **Level 2 → Level 3** — the issue requires a fix to the core product or deep technical expertise.

#### 4.2 Issue tracking best practices

* **Log all issues** — use a ticket tracking tool to capture all issues reported to first-line support.
* **Categorize issues** — tag issues by type (training, configuration, bug, etc.) to identify patterns.
* **Track resolution time** — monitor how long issues take to resolve at each tier.
* **Review regularly** — hold regular reviews of open issues and common problem areas.
* **Update support materials** — use insights from issue tracking to improve self-service materials and training.

***

### 5. Getting support from OpenCRVS

If you require support with any level of operational support, the OpenCRVS team can provide guidance and assistance.

Please reach out to [**team@opencrvs.org**](mailto:team@opencrvs.org) to discuss how we can support you with:

* Setting up support structures and processes.
* Training your support teams.
* Providing expert-level technical support.
* Addressing core product issues.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/operational-support.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
