---
title: "Interoperability"
source_url: "https://documentation.opencrvs.org/v1.5/technology/interoperability"
markdown_url: "https://documentation.opencrvs.org/v1.5/technology/interoperability.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f23ce98c36c4a3253457bc8c5183d59dc57a4255fd09aab5e0c823ec8ad2921c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/technology/interoperability.md).

# Interoperability

An introduction describing how OpenCRVS interoperates

OpenCRVS has been technically architected from conception to interoperate with other e-Gov systems in a standardised, safe and secure way. &#x20;

We have demonstrated how easy it is to interoperate with OpenCRVS in the past by:&#x20;

a) being a core collaborator of the [G2PConnect](https://g2pconnect.global/) initiative.

b) installing a permanent installation of an OpenCRVS and National ID integration with [MOSIP](https://mosip.io/) at the MOSIP Experience Center in Bangalore, India.

c) integrating with [DHIS2](https://dhis2.org/) to standardise birth and death notifications from a hospital setting for civil registration using [FHIR](https://www.hl7.org/fhir/overview.html).

<figure><img src="https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/idVQt19A6tNtyCXSv1nX/Screenshot%202023-01-10%20at%2016.46.06.png" alt=""><figcaption><p>Using the OpenCRVS v1.2.* Integrations GUI to configure a webhook client</p></figcaption></figure>

As of OpenCRVS v1.2.\* we now provide a simple GUI to set up, enable and disable integrating clients that generates and refreshes API keys. &#x20;

There are 4 common interoperability use cases you can easily take advantage of using our new GUI and specific API Gateway endpoints in JSON and GraphQL.

1. **Event Notification**: Allow any other service to POST full or partial civil registration event applications to OpenCRVS - referred to in civil registration nomenclature as a "notification".  Most commonly these are submitted by hospitals, but you could also use this functionality to enable application submission from a social protection system or a public portal.
2. **National ID**: Ensure a National ID system is notified by a webhook whenever an event (birth or death) is registered in OpenCRVS.  Use this to create or deactivate National ID numbers, or use it to authenticate citizens before allowing them to register an event.
3. **Record Search**: Allow any other service to perform an advanced search of civil registration records.  Use this to help support social protection systems, check the existence of civil registration records or check citizen demographics.
4. **Webhook**: Allow any other system to subscribe to event in OpenCRVS and retrieve a customisable payload of registration data.  Allow any system to react immediately when a birth or death is registered.

The following sections will describe step-by-step instructions regarding how to configure these integrations as well as show you how you can expose OpenHIM to have full interoperability control over OpenCRVS.&#x20;

**Other ways to interoperate**

OpenCRVS' database layer for all registration data is expressed in JSON as [FHIR](https://hl7.org/FHIR/) in MongoDB and exposed via a FHIR database server called [Hearth](https://github.com/opencrvs/hearth).  This means that our schema is automatically thoroughly documented in the HL7 FHIR specification.  We have made some customisations to support the civil registration context hat are documented in the [standards](/v1.5/technology/standards.md) section. We knew how important it would be for health institutions to be able to send us birth and death notifications from the beginning, hence our early adoption of FHIR as our interoperability standard.  This also makes it easy for interoperating systems to understand our data.

We expose some FHIR APIs directly via our API Gateway, specifically for performing CRUD actions on [FHIR Locations](https://build.fhir.org/location.html) which we use for administrative structure, civil registration and health office buildings where registrations occur.  When OpenCRVS is running you can view [Swagger](https://swagger.io/) documentation in this Gateway.

OpenCRVS stack includes [OpenHIM](http://openhim.org/).  The Open Health Information Mediator is a middleware component designed to ease interoperability between disparate information systems. Both OpenHIM and Hearth are OpenSource projects developed by [Jembi Health Systems](https://www.jembi.org/).  It is possible to expose direct access to OpenHIM in OpenCRVS Core, should you wish to interoperate with it.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/technology/interoperability.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
