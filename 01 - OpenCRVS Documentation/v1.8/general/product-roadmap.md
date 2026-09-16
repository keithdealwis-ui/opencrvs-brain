---
title: "Product roadmap"
source_url: "https://documentation.opencrvs.org/v1.8/general/product-roadmap"
markdown_url: "https://documentation.opencrvs.org/v1.8/general/product-roadmap.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:9c4c03f849c7faa725fec4300e42a4bb9dba3ca0f24c6cb942a15a61c4956a4e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/general/product-roadmap.md).

# Product roadmap

## The OpenCRVS Use Case Inventory

We often get the question "What does OpenCRVS do?". Beyond the descriptions found in the [Functional Architecture](/v1.8/product-specifications/functional-architecture.md) section, we maintain a full inventory of use cases, which will allow you to quickly map existing and future use cases supported by OpenCRVS with your own country requirements.

{% file src="/files/2YteqVtQgh8Uho5b8Oa6" %}

In addition to the functional and integration use cases, a separate tab includes non-functional requirements (NFRs) that we believe are important for national scale civil registration systems, the majority of which OpenCRVS is already compliant with.

## Future release dates

The following table provides an overview of projected delivery dates for future releases, as defined in the Use Case Inventory above.

* The beta release is typically made available after initial QA testing, but before full regression testing has been commenced. It is not intended for live use in a production environment, however it allows accredited implementation partners to test out sample configurations and to contribute to the release testing effort.
* All dates provided are indicative and are subject to change, however OpenCRVS Product Management makes every effort to provide accurate estimates to support implementation planning.

<table><thead><tr><th width="148">Release</th><th>Beta release date</th><th>Full release date</th></tr></thead><tbody><tr><td>v1.8.0</td><td>28 April 2025</td><td>21 July 2025</td></tr><tr><td>v1.9.0</td><td>05 September 2025</td><td>31 October 2025*</td></tr><tr><td>v1.10.0</td><td>TBC</td><td>TBC</td></tr></tbody></table>

\*Date adjusted to include configuration and migration testing beyond the Farajaland default,  including country reference implementations to ensure known local contexts are supported

## Future product scope

The scope for future releases of OpenCRVS is primarily determined based on confirmed system requirements coming from current and future OpenCRVS implementations.

Get in touch via [OpenCRVS Github Discussion ](https://github.com/opencrvs/opencrvs-core/discussions/categories/feature-requests)to share your priority feature requests.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/general/product-roadmap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
