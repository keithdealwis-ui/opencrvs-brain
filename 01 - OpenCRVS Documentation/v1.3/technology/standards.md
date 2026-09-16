---
title: "Standards"
source_url: "https://documentation.opencrvs.org/v1.3/technology/standards"
markdown_url: "https://documentation.opencrvs.org/v1.3/technology/standards.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:6d7e1e3716b5d4bfff3a09202b02d9383670cfef341e14bdea8ffc482cd78a14"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/technology/standards.md).

# Standards

Overview of how OpenCRVS uses best-practice technology standards

At OpenCRVS we are obsessed with conforming to good, existing standards.  We want to make implementers' lives as easy as possible, so we have no intention of re-inventing the wheel when we don't have to.&#x20;

#### **Data**

By using [FHIR](https://hl7.org/FHIR/) as a standard for our NoSQL datastore, [Hearth](https://github.com/jembi/hearth) and the [OpenHIE](https://ohie.org/) standard interoperability layer [OpenHIM](http://openhim.org/), OpenCRVS seamlessly connects civil registration to health services and other systems. We can receive birth and death notifications from the hospital setting and expose registration events to any other technical system, such as National ID, via our FHIR standard API gateways.

[FHIR](https://hl7.org/FHIR/) was created by [Health Level Seven International (HL7)](http://hl7.org/), a not-for-profit, ANSI-accredited, standards organization dedicated to providing a comprehensive framework and related standards for the exchange, integration, sharing and retrieval of electronic health information that supports clinical practice and the management, delivery and evaluation of health services.

We have extended FHIR's model to include custom codes and extensions that assist the Civil Registration context.  To understand more about how and why we use FHIR, click [here](/v1.3/technology/standards/fhir-documents.md).

#### **Interoperability**

Systems can interoperate with OpenCRVS using FHIR or via Webhooks which follow [WebSub](https://www.w3.org/TR/websub/) process and standards. Our friends at MOSIP have demonstrated [ease of integration with OpenCRVS](https://docs.mosip.io/1.2.0/integrations/mosip-opencrvs-integration) using these methods.

#### **Internationalisation**

OpenCRVS uses industry-wide i18n [JSON](https://en.wikipedia.org/wiki/JSON) standards, the [unicode ICU Message Syntax](https://unicode-org.github.io/icu/userguide/format_parse/messages/),  [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes and [ISO 3166 Alpha 3 country codes ](https://www.iban.com/country-codes)to make localisation a breeze and integrate seamlessly with enterprise level content management systems such as [Transifex](https://www.transifex.com/) or [Contentful](https://www.contentful.com/).

#### **Authentication**

Our applications are protected by [2-Factor Authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication) utilising [OAuth JWT best practices](https://tools.ietf.org/id/draft-ietf-oauth-jwt-bcp-02.html). You can read more about our security standards in the next section.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/technology/standards.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
