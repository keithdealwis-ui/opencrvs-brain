---
title: "Interoperability roadmap"
source_url: "https://documentation.opencrvs.org/v1.3/general/interoperability-roadmap"
markdown_url: "https://documentation.opencrvs.org/v1.3/general/interoperability-roadmap.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:37c13c8e2c8300de08f30ac2e33f239f43fd0bee3cfc5b3cc275b443e6f2562a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/general/interoperability-roadmap.md).

# Interoperability roadmap

OpenCRVS has been technically architected from conception to interoperate with other systems. The following outlines the interoperability achievements in previous releases along with the roadmap of future releases planned in 2023/2024.

{% hint style="success" %}
OpenCRVS interoperates out-the-box using the [FHIR](https://www.hl7.org/fhir/overview.html) standard as JSON. The [FHIR API](https://www.hl7.org/fhir/http.html) is exposed via [OpenHIM](http://openhim.org/). **The supported FHIR version is: STU3**
{% endhint %}

**OpenCRVS v1.0: June 2022:**

a) Adopted the [OpenHIE](https://guides.ohie.org/arch-spec/) architectural framework by design and [FHIR](https://www.hl7.org/fhir/overview.html) standard interoperability reference middleware [OpenHIM](http://openhim.org/) - FHIR version STU3.

b) Integrated with [DHIS2](https://dhis2.org/) to standardise [event notifications](/v1.3/technology/interoperability/event-notification-clients.md) from a hospital setting for civil registration using [FHIR](https://www.hl7.org/fhir/overview.html) in Bangladesh pilot.

**OpenCRVS v1.1: Sep 2022**

a) Birth registration integration with [MOSIP](https://mosip.io/).

b) Death registration integration with [MOSIP](https://mosip.io/).

c) Release of OpenCRVS [FHIR](https://www.hl7.org/fhir/overview.html) standard W3C standard [WebSub](https://www.w3.org/TR/websub/) [webhooks](/v1.3/technology/interoperability/webhook-clients.md) for subscription.

**OpenCRVS v1.2: Jan 2023**

a) Release of the [Elasticsearch](https://www.elastic.co/) [Record Search API](/v1.3/technology/interoperability/record-search-clients.md) for use as part of a social protection interoperability collaboration the[ Digital Convergance Initiative](https://spdci.org/).

b) Release of the OpenCRVS [FHIR Location REST API](/v1.3/technology/interoperability/fhir-location-rest-api.md) for reading, updating and archiving jurisdictions and facilities.

**OpenCRVS v1.3 - Planned release: June 2023**

a) Authentication and validation of National ID using [MOSIP](https://mosip.io/) [E-Signet](https://docs.esignet.io/) consent.

b) Permanent installation of MOSIP integration at the MOSIP Experience Center in Bangalore, India.

d) Core collaboration of the [G2PConnect](https://g2pconnect.global/) protocol initiated.

e) Integration with [Secure Identity Alliance](https://secureidentityalliance.org/), OSIA standard [Birth Use Case](https://osia.readthedocs.io/en/v4.1/02%20-%20functional.html#birth-use-case)

f) Integration with [OpenSPP](https://openspp.org/) social protection system, using QR code.

g) Integration with [INGroupe](https://ingroupe.com/) National ID system.

**OpenCRVS v1.4 - Planned release: Sep 2023:**

a) [W3C Verifiable Credential](https://www.w3.org/TR/vc-data-model/) integration with [MOSIP](https://mosip.io/)

b) Correct record integration with [MOSIP](https://mosip.io/)

c) Revocation of a record integration with [MOSIP](https://mosip.io/)

d) [G2PConnect](https://g2pconnect.global/) protocol integration v0.1

e) OpenCRVS civil registration related [FHIR](https://www.hl7.org/fhir/extensibility.html) extensions published

**OpenCRVS v1.5 - Planned release: Jan 2024:**

a) [G2PConnect](https://g2pconnect.global/) protocol integration v1.0

b) Integration with the [JeMPI Master Patient index](https://github.com/jembi/JeMPI) v0.1

**OpenCRVS v1.6 - Planned release: May 2024:**

a) [G2PConnect](https://g2pconnect.global/) protocol integration v2.0

b) Integration with the [JeMPI Master Patient index](https://github.com/jembi/JeMPI) v1.0


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/general/interoperability-roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
