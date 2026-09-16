---
title: "National ID client"
source_url: "https://documentation.opencrvs.org/v1.7/technology/interoperability/national-id-client"
markdown_url: "https://documentation.opencrvs.org/v1.7/technology/interoperability/national-id-client.md"
version: "v1.7"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:a78be5a5849376f35883713514203347c7eebffa10b1c76fcf39715ca796221b"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.7/technology/interoperability/national-id-client.md).

# National ID client

Civil registration provides the source of truth for any vital event that occurs in a country. As a result is usual that an integration with a country's National ID system is requested.

### Default functionality

Currently OpenCRVS supports the following default National ID integration functionality:

#### Use cases:

OpenCRVS can let a National ID system know of any birth that occurs in the country so that operations can be put in place to provide a National ID number for the child.  OpenCRVS can let a National ID system know of any death that occurs in the country so that operations can be put in place to mark the individual as deceased.

There are 3 points of integration possible.

1\) Configuration of a HTTP, FETCH\_BUTTON, ID\_READER (used when scanning QR codes on ID cards), or ID\_VERIFICATION\_BANNER (used to display authentication status to the user) components in your declaration forms to authenticate a parent or informant's National ID via the National ID portal's APIs. &#x20;

2\) Intgegration to the National ID system at the point where backend processing is [poised to register the event](https://github.com/opencrvs/opencrvs-countryconfig/blob/a84fe1bb9499fd09dd957e2744261daeeb4ee87f/src/api/event-registration/handler.ts#L21) in OpenCRVS.

3\) Subscription to the REGISTERED webhook to perform an action once the civil registration is completed.

### Future National ID integration functionality

**Revocation**: Occasionally a birth or death may be wrongly registered either fraudulently or by mistake. Any revocation in OpenCRVS should be communicated to the National ID system.

**Correction**: Occasionally data may have been entered incorrectly to the registration and a legal correction is performed in OpenCRVS. Any correction in OpenCRVS should be communicated to the National ID system.

We are continually improving our National ID integration capabilities and look forward to addressing functionality such as this in future versions of OpenCRVS. For more information, please get in touch at: **<team@opencrvs.org>**

### MOSIP / E-Signet integration

Previous integrations with MOSIP & E-Signet are in a state of refactor to utilise the MOSIP Packet Manager API. &#x20;

OpenCRVS 1.8.0 will introduce a MVP, production ready integration with MOSIP using Packet Manager API.  A new [OpenCRVS > MOSIP NPM package](https://www.npmjs.com/package/@opencrvs/mosip) has been created to ease interoperability requirements. &#x20;

This [country configuration repository](https://github.com/opencrvs/opencrvs-countryconfig-mosip) gives code examples regarding how to use the package and configure the flows. &#x20;

Flows are currently in a design state and will be updated and finalised for a production ready integration covering all possible unhappy path eventualities in OpenCRVS v1.9.0

{% embed url="<https://www.figma.com/board/DifOmLi6RpYidYy7p28zXy/MOSIP-Integration?node-id=940-1862&t=oOM7CgPvAr4ioy9P-1>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.7/technology/interoperability/national-id-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
