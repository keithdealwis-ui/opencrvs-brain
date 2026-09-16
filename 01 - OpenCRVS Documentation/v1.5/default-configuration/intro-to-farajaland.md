---
title: "Intro to Farajaland"
source_url: "https://documentation.opencrvs.org/v1.5/default-configuration/intro-to-farajaland"
markdown_url: "https://documentation.opencrvs.org/v1.5/default-configuration/intro-to-farajaland.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8b1307db09eadcb70cf3a807d07be0b057093c5b0e08db548feeb927369f3398"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/default-configuration/intro-to-farajaland.md).

# Intro to Farajaland

Provides details of the OpenCRVS default configuration

Farajaland is a fictitious country used to illustrate how OpenCRVS is specifically designed to meet the needs of typical low-resource settings. The OpenCRVS demos are built around the needs of this country, which reflect a variety of real-life contexts from around the world.

* Farajaland acts as the **default configuration**. The OpenCRVS product works "out of the box" so that functionality can be quickly demonstrated and explored, based on the needs of the Farajaland context.
* The Farajaland configuration illustrates a number of **new service delivery models**, which have the potential to strengthen CRVS systems and improve key performance indicators, such as completeness rates, quality of vital events data etc.

Take time to become familiar with Farajaland and its requirements for a digital CRVS system. This will help you to understand how to configure OpenCRVS based on your own needs.

#### **Background on Farajaland**

* A small country in sub-Saharan African with a population of approx. 2m people.
* Farajaland is organised into Provinces and Districts as shown on the Farajaland map below.
* Many areas are rural with a low population density.
* There is good mobile phone connectivity in the urban areas but in rural areas it is very poor.
* A number of different local languages are spoken in Farajaland but in the North the common language is English and in the South it is French.
* The currency used is the US dollar.
* Farajaland has a National ID card and this is used to prove the identity of adults over 18 years of age.

#### Map of Farajaland

![Provinces and Districts of Farajaland](https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/nCq67odvpUHnjzMjCKAp/farajaland-map.png)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/default-configuration/intro-to-farajaland.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
