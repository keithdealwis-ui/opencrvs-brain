---
title: "Standards"
source_url: "https://documentation.opencrvs.org/v1.9/technology/standards"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/standards.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e90ce4b6434f99d39d92a781b03d500493ec5fb38e306b0b738bbe942035cd98"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/standards.md).

# Standards

Overview of how OpenCRVS uses best-practice technology standards

**We implement as per the U.N. Guidelines for Civil Registration.**

Because OpenCRVS is a core component of Digital Public Infrastructure, we are committed to adopting digital gov data standards.

**Social protection standards:** [**Digital Convergence Initiative**](https://spdci.org/events/crvs-and-sp-mis-standards-released-v1-0-0/)**.** OpenCRVS are a [Standards Committee Member ](https://standards.spdci.org/standards/v/crvs-v1.0-1/resources/standards-committee)of the Digital Convergence Initiative, [CRVS and SP-MIS](https://standards.spdci.org/standards/v/crvs-v1.0-1/crvs/crvs-with-sp-mis-standards) interfaces. We helped author these standards and interoperate with social protection systems such as [OpenSPP](https://openspp.org/).

**DPI standards:** [Centre for Digital Public Infrastructure](https://cdpi.dev/) - [G2PConnect](https://g2pconnect.global/) standards are in use in the interoperable [middleware](https://github.com/opencrvs/dci-crvs-api) relevant to the social protection standards above.

**Healthcare standards:** Event registrations such as births and deaths, that occur in a hospital setting can interoperate with OpenCRVS using [FHIR](https://hl7.org/FHIR/) , a global healthcare standard managed by: [Health Level Seven International (HL7)](http://hl7.org/). We have extended FHIR's model to include custom codes and extensions that assist the Civil Registration context.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/standards.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
