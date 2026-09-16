---
title: "Standards"
source_url: "https://documentation.opencrvs.org/v1.4/technology/standards"
markdown_url: "https://documentation.opencrvs.org/v1.4/technology/standards.md"
version: "v1.4"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:9034cfa8b8a1a6082203be3d0abb3d59aeb8e7df8f75c0e4f786f8e39f326939"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.4/technology/standards.md).

# Standards

Overview of how OpenCRVS uses best-practice technology standards

Because OpenCRVS is a core component of Digital Public Infrastructure, we are obsessed with conforming to good, existing standards.&#x20;

CR Standards: [Digital Convergence Initiative](https://spdci.org/events/crvs-and-sp-mis-standards-released-v1-0-0/)

OpenCRVS are a [Standards Committee Member ](https://standards.spdci.org/standards/v/crvs-v1.0-1/resources/standards-committee)of the Digital Convergence Initiative, [CRVS and SP-MIS](https://standards.spdci.org/standards/v/crvs-v1.0-1/crvs/crvs-with-sp-mis-standards) interfaces.  We helped author these standards and interoperate with social protection systems such as [OpenSPP](https://openspp.org/).

[Centre for Digital Public Infrastructure](https://cdpi.dev/) - [G2PConnect](https://g2pconnect.global/)

OpenCRVS has contributed to and conforms to the G2PConnect [standardised API](https://github.com/opencrvs/dci-crvs-api) using the DCI payloads above.

#### **Data**

By using [FHIR](https://hl7.org/FHIR/) as a standard for our NoSQL datastore, [Hearth](https://github.com/jembi/hearth) and the [OpenHIE](https://ohie.org/) standard interoperability layer [OpenHIM](http://openhim.org/), OpenCRVS seamlessly connects civil registration to health services and other systems. We can receive birth and death notifications from the hospital setting and expose registration events to any other technical system, such as National ID, via our FHIR standard API gateways.

[FHIR](https://hl7.org/FHIR/) was created by [Health Level Seven International (HL7)](http://hl7.org/), a not-for-profit, ANSI-accredited, standards organization dedicated to providing a comprehensive framework and related standards for the exchange, integration, sharing and retrieval of electronic health information that supports clinical practice and the management, delivery and evaluation of health services.

We have extended FHIR's model to include custom codes and extensions that assist the Civil Registration context.  To understand more about how and why we use FHIR, click [here](/v1.4/technology/standards/fhir-documents.md).

#### **Interoperability**

Systems can interoperate with OpenCRVS using FHIR or via Webhooks which follow [WebSub](https://www.w3.org/TR/websub/) process and standards. Our friends at [MOSIP](https://mosip.io/) have demonstrated [ease of integration with OpenCRVS](https://docs.mosip.io/1.2.0/integrations/mosip-opencrvs-integration) using these methods.

#### **I**


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.4/technology/standards.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
