---
title: "National ID"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:99dbbd6228f54cfd91dc82882687c7186725ae7bab1afca86510ad2efd72c047"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client.md).

# National ID

### Why integrate OpenCRVS with National ID?

Civil registration provides the source of truth for any vital event that occurs in a country.  Civil registration can inform a National ID system when a birth occurs and therefore instigate the generation of a National ID for the child at birth.  At the point of death, a civil registration system can inform the National ID system that the person is deceased, thus preventing fraudulent usage of a National ID of a deceased person.

The partnership of Civil Registration and National ID is what collectively constitutes the foundational identity infrastructure of a nation.  &#x20;

[Bridging the Identity Gap: Integrating Civil Registration and National Identity Systems](http://prod-website-903390823.ap-south-1.elb.amazonaws.com/mosip16.9/bridging-the-identity-gap-integrating-civil-registration-and-national-identity-systems)

### Which National ID systems can OpenCRVS interoperate with?

OpenCRVS is agnostic regarding which National ID system it integrates with.  This section is first organised around the main business use cases. &#x20;

As of OpenCRVS v1.8.0, OpenCRVS has a production ready integration library dedicated to interoperating with [MOSIP](https://www.mosip.io/) and [E-Signet](https://docs.esignet.io/), fellow OpenSource Digital Public Goods.  A dedicated section exists that builds on the same agnostic integration points specifically for integrating with MOSIP.

In the past, OpenCRVS has delivered proof-of-concept (not production ready) integrations with [INGroupe](https://ingroupe.com/) and [OSIA standard](https://secureidentityalliance.org/osia) National ID systems

### Existing National ID integration functionality

Currently OpenCRVS supports the following default National ID integration functionality:

* Authenticating and verifying the identity of informants and parents during the event application process both offline and online.
* Configurable rules to determine whether or not a civil registration event should or should not integrate with a National ID system at the point of registration.
* Integration with a National ID system at the point of registration synchronously and asynchronously

### Roadmap (Backlog) of National ID/MOSIP  integration functionality

The following integrations between OpenCRVS and a National ID / MOSIP system are in development.  Should you require them in your country, we welcome contributions to this effort.  Please get in touch:

* Notifying a National ID system of any legal correction to a previously registered record
* Notifying a National ID system of any legal revocation of a previously registered record
* Notifying a National ID system of any legal name change
* Authenticating and verifying the identity of an individual who is collecting an issued certificate


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
