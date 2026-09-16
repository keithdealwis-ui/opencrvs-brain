---
title: "MOSIP"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:92cdbabb76d0b2c180fa9a76e847ccbf9b0ff9f373ea1423933da61c73e417c1"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip.md).

# MOSIP

Interoperating with MOSIP and E-Signet, OpenSource DPG solutions for National ID and digital identity verification

{% embed url="<https://youtu.be/mUrXeuOjQZE?si=5BW217DrYOz5OU1n>" %}

{% hint style="warning" %}
Watch the video above to see a successful configuration of components that are all explained in this section
{% endhint %}

### Introduction

OpenCRVS integration with MOSIP follows a very similar technical process as followed for configuring integration with any other National ID system. &#x20;

For registration, the same API endpoints are configured, "in-form authentication and verification" uses QR Code scanning or E-Signet.

In order to make MOSIP integration easier from a back-end perspective, we supply a [**mosip-api** ](https://github.com/opencrvs/mosip/tree/v1.8.0/packages/mosip-api)middleware component, which should be deployed in the OpenCRVS stack using a docker-compose configuration.  The middleware allows you to configure the required business logic for interacting with the MOSIP Packet Manager API according to your needs.

### Detailed flow diagrams

To understand the business process around the technical integration between OpenCRVS and MOSIP that is currently available, refer to this Figjam flow diagram:

{% embed url="<https://www.figma.com/board/ouhT8BRAu7HASKkebrUkwu/MOSIP-Public-Documentation?node-id=0-1&t=tJj8mP3hENcpXbBI-1>" %}

### opencrvs/mosip library

In order to make life as easy as possible for developers who wish to configure the MOSIP integration, we have abstracted away all the non-customisable logic into an NPM library and created mock servers for both MOSIP and E-Signet.

{% embed url="<https://github.com/opencrvs/mosip/releases/tag/v1.8.0>" %}

Checkout this repo and follow the README to run the middleware and mocks alongside your local instance of OpenCRVS.

### mosip-api middleware

The mosip-api middleware is a critical component that must be deployed.  This is explained further in the following sections.

{% embed url="<https://github.com/opencrvs/mosip/tree/release-v1.8.0/packages/mosip-api>" %}

### Example countryconfig

We also provide an example, forked country configuration that uses this library.  You can follow exactly how we have configured the full business logic by reading the code.

{% embed url="<https://github.com/opencrvs/opencrvs-countryconfig-mosip/releases/tag/v1.8.0>" %}

### Mocks:

{% embed url="<https://github.com/opencrvs/mosip/tree/v1.8.0/packages/mosip-mock>" %}

{% embed url="<https://github.com/opencrvs/mosip/tree/v1.8.0/packages/esignet-mock>" %}

The following sections will delve into the configuration points in more detail.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
