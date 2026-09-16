---
title: "Example: Farajaland"
source_url: "https://documentation.opencrvs.org/implementation/example-farajaland"
markdown_url: "https://documentation.opencrvs.org/implementation/example-farajaland.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c9912e05d7ffdb1e1312c7da5b87d9ace3dbcb090da436fb3d0ad60b133a2353"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/example-farajaland.md).

# Example: Farajaland

### 1. Introduction

Farajaland is a fictitious country used throughout the OpenCRVS documentation to **demonstrate a complete country configuration**. It shows, end‑to‑end, how real civil registration business rules can be translated into OpenCRVS features such as Users, Actions, Status, Flags, Workqueues, Certificates, and Integrations.

Use Farajaland as a **reference country** when designing a real implementation: it provides concrete patterns to copy and adapt, not a template that must be followed exactly.

***

### 2. Why Farajaland exists

Farajaland is designed to be:

* **Realistic enough** to reflect common challenges in low‑resource CRVS settings.
* **Opinionated enough** to show good practices (for example, who should approve late registrations, how to handle duplicates, how to stage certificates and certified copies).
* **Flexible enough** that countries can change the rules while reusing the underlying configuration patterns.

In the OpenCRVS demos:

* Farajaland acts as the **default out‑of‑the‑box configuration**.
* The demo workflows (birth and death registration, late registration, corrections, revocations, printing, performance monitoring) are all based on Farajaland’s requirements.

***

### 3. How Farajaland is organised

Farajaland is a small sub‑Saharan African country with:

* A population of approximately **2 million** people.
* A **Province → District → Facility / Community** administrative hierarchy.
* Many rural areas with **low population density** and **poor connectivity**.
* Better mobile connectivity in urban centres.
* Multiple local languages, with **English** more common in the north and **French** more common in the south.
* The **US dollar** as the currency in the demo configuration.
* A **National ID card** used to prove the identity of adults over 18 years of age.

The **Civil Registration Authority (CRA)** is responsible for civil registration in Farajaland. It is headed by the **Registrar General**, based at the CRA HQ in Isamba District, and supported by provincial and district‑level civil registration offices.

For more detail on the institutional context and strategic goals, see **“Background & Goals”**.

***

### 4. Using Farajaland when designing a real country configuration

When configuring OpenCRVS for a real country, treat Farajaland as a **worked example**:

* Start from Farajaland’s **business rules** and ask whether similar rules apply in your context.
* Use Farajaland’s configuration (roles, scopes, actions, statuses, flags, queues) as a **pattern**, not a prescription.
* Adapt each rule to match your national legislation, policy, and operational practices.

As you update or extend the Farajaland example, keep these questions in mind:

* What problem in Farajaland’s CRVS system does this change solve?
* Which law, regulation, or policy does this rule reflect?
* Which OpenCRVS feature (scope, action, flag, workqueue, integration) is best suited to implement it?

By keeping Farajaland realistic and coherent, the example remains a powerful tool for explaining OpenCRVS to stakeholders and for designing new configurations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/example-farajaland.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
