---
title: "Interoperability"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e4b24c72ba9fba4c5afd7b5865835052b3f2bcb3786abf0fd8d48b92d51ca4e6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability.md).

# Interoperability

An introduction describing how OpenCRVS interoperates

OpenCRVS has been technically architected from conception to interoperate with other e-Gov systems in a standardised, safe and secure way.

Various APIs exist for different consumers and business use cases.  The interoperability documentation is structured around theses use cases.

### APIs requiring OAuth client credentials

OpenCRVS OAuth API client credentials are required in order for a trusted external system to integrate with OpenCRVS for the following use cases:

Performing a [R**ecord search**](/v1.8/technology/interoperability/create-a-client/record-search-clients.md) of the OpenCRVS database either directly using ur GraphQL Gateway or via a DCI standard middleware.

Submitting an [**"Event Notification"**](/v1.8/technology/interoperability/create-a-client/event-notification-clients.md) **in FHIR** from healthcare systems

Subscribing to event [**Webhooks**](/v1.8/technology/interoperability/create-a-client/webhook-clients.md) for status updates on a processing event

### APIs for system administrators

An API exists for system administrators to perform management of OpenCRVS reference data, specifically administrative structure, civil registration offices and health facilities on a running OpenCRVS instance in production.

This is the [FHIR Location API](#apis-for-system-administrators) and a National System Administrators JWT is used as an authentication mechanism for these APIs.

### National ID

Integrating with an external [National ID ](/v1.8/technology/interoperability/national-id-client.md)system is a complex topic with multiple, optional use cases available.  A dedicated section on National ID integration exists to cover:

* Authentication and verification of informants / parents details with NID / external systems during event form completion - online / offline.
* Generation of a National ID for a citizen at birth registration
* Informing a National ID system that an individual is deceased at death registration
* Specifics when selecting MOSIP as the integrating National ID system

### Interoperability Roadmap

Our interoperability roadmap currently incudes:

* Extension of the Event Notification and Webhook APIs to support a "Self-service" civil registration portal front end.  Simplified payloads with and without FHIR
* Verifiable credentials


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
