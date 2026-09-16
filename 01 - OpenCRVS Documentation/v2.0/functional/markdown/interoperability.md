---
title: "Interoperability"
source_url: "https://documentation.opencrvs.org/functional/markdown/interoperability"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/interoperability.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:dadf620d36b78cf9e2d3a184a9f8fc234d457f7a9dce96520f223fd9a8a3aa68"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/interoperability.md).

# Interoperability

### 1. Introduction

Civil registration systems do not operate in isolation. They exchange information with other government systems to support public services, improve data quality and reduce duplicate data entry. OpenCRVS has been architected from its inception to interoperate with other e-Government systems in a standardised, safe and secure manner.

This page provides a high-level overview of interoperability in OpenCRVS and how it relates to [solution architecture](/implementation/your-opencrvs-project/solution-architecture.md). The detailed technical guidance for implementing integrations is provided in the [integration architecture](/technical/architecture/integration-architecture.md) and [configuration](/technical/guides/configuration/integrations.md) documentation.

**Where this sits:** Interoperability requirements are identified during **Design & Specification** as part of the solution architecture and are implemented during **Configuration** and **Deployment**.

***

### 2. Why interoperability matters

A civil registration system forms part of a wider government digital ecosystem. Depending on national requirements, OpenCRVS may exchange information with systems such as:

* National identity systems
* Social protection systems
* Population registers
* Health information systems
* Immigration systems
* Statistics platforms
* Notification services
* Digital identity and authentication providers
* Other government & private sector applications

Interoperability enables information to be shared electronically, reducing manual processes, improving data accuracy and allowing government services to operate more efficiently.

{% hint style="info" %}
Every integration should have a clearly defined business purpose and should exchange only the information required to support that purpose. Integration should not be "gamified" at the expense of privacy and consent.
{% endhint %}

***

### 3. Interoperability and solution architecture

Before any integrations are developed, the project's [Solution Architecture](/implementation/your-opencrvs-project/solution-architecture.md) defines how OpenCRVS fits within the wider government technology landscape.

The solution architecture helps identify:

* which external systems need to communicate with OpenCRVS
* the direction in which information flows
* the business events that trigger data exchange
* the security, privacy and governance requirements for each integration
* the responsibilities of each participating system

Developing the solution architecture early ensures that interoperability requirements are agreed before implementation begins and that all stakeholders understand how OpenCRVS will interact with the surrounding digital ecosystem.

***

### 4. How OpenCRVS supports interoperability

OpenCRVS provides a flexible interoperability framework that allows external systems to exchange information securely without modifying the core platform.

At a high level, interoperability is achieved through two complementary mechanisms:

[Application Programming Interfaces (APIs)](/functional/markdown/interoperability/apis.md) — OpenCRVS provides a range of APIs designed for different consumers and business use cases. These APIs allow authorised systems to securely retrieve information from OpenCRVS, submit information to OpenCRVS or perform approved business operations.

[Action Triggers](/functional/markdown/interoperability/action-triggers.md) — OpenCRVS can automatically notify external systems when defined business events occur, such as the registration or certification of a vital event. This enables other government systems to respond automatically without requiring manual intervention.

Together, APIs and Action Triggers enable OpenCRVS to participate in event-driven government architectures while maintaining clear security boundaries and auditability.

***

### 5. Designing interoperable solutions

Interoperability should always be driven by business requirements rather than technology.

When planning integrations, implementation teams should consider:

* the business outcome the integration is intended to achieve
* which system owns each item of information
* when information should be exchanged
* what level of security, authentication and authorisation is required
* how failures, retries and audit trails will be managed

These decisions are captured within the solution architecture before technical implementation begins.

***

### 6. Resources and support

For further guidance, see:

* [Solution Architecture](/implementation/your-opencrvs-project/solution-architecture.md) – understanding how OpenCRVS fits within the wider government ecosystem.
* [Integration Architecture](/technical/architecture/integration-architecture.md) – defines how OpenCRVS connects securely with a country's wider digital ecosystem, enabling it to exchange information with external systems while remaining agnostic.
* [Integration Configuration](/technical/guides/configuration/integrations.md) – technical guidance on configuring event-driven integrations with external systems.
* [ID Integration & MOSIP](/functional/markdown/interoperability/mosip-id-integration.md) - Integrating OpenCRVS with a National ID system creates a trusted foundation for legal identity, ensuring that vital events automatically support accurate and secure identity management throughout life.

These guides describe how to implement secure integrations using these capabilities while following OpenCRVS architectural principles.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/interoperability.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
