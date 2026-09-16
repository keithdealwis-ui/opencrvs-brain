---
title: "Welcome!"
source_url: "https://documentation.opencrvs.org/v1.7/readme"
markdown_url: "https://documentation.opencrvs.org/v1.7/readme.md"
version: "v1.7"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f8b31fa5226acbb1012fac5daa8a3068bf0a291432d93a012093af1d60a4b818"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.7/readme.md).

# Welcome!

{% embed url="<https://youtu.be/HAYN3ATxQGI>" %}

OpenCRVS is an open-source digital solution for civil registration, designed specifically for low-resource settings and available as a Digital Public Good.

This documentation can be used by governments, system integrators and development partners to design, configure, operate and maintain an OpenCRVS application that meets your country's needs.

* to understand what effective digital CRVS looks like and the role that OpenCRVS can play, check out [CRVS Systems](/v1.7/crvs-systems/effective-digital-crvs-systems.md).&#x20;
* to explore the OpenCRVS functionality, take a look at the [Product Specifications](/v1.7/product-specifications/functional-architecture.md) and the [Default Configuration for Farajaland](/v1.7/default-configuration/intro-to-farajaland.md)
* to understand how OpenCRVS works technically, go to [Technology](/v1.7/technology/architecture.md)
* to setup you own OpenCRVS project, then go to [Setup](/v1.7/setup/1.-establish-project-and-team.md)
* to run OpenCRVS on your laptop, take a look at the [Quick Start](/v1.7/setup/3.-installation/3.1-set-up-a-development-environment.md).
* to technically configure OpenCRVS, go to [Configure](/v1.7/setup/3.-installation/3.2-set-up-your-own-country-configuration.md).
* to deploy to a server, a configured version of OpenCRVS, go to [Deploy](/v1.7/setup/3.-installation/3.3-set-up-a-server-hosted-environment.md).
* to see what's coming next for OpenCRVS, see the [Product Roadmap](/v1.7/general/product-roadmap.md)

{% hint style="info" %}
We recommend that you use this documentation in combination with the [CRVS Digitisation Guidebook](http://www.crvs-dgb.org/en/), an online resource that provides step-by-step guidance for countries to implement digitized systems and automated processes for CRVS.
{% endhint %}

### Why is OpenCRVS needed?

Civil registration is the foundation of legal identity and rights-based service delivery. A Civil Registration and Vital Statistics (CRVS) system records the details of all major life events, such as births, deaths, marriage and divorce. It is an essential component of the "leave no one behind" agenda and without it working effectively, it is virtually impossible to ensure inclusive growth.

Unfortunately, in many countries CRVS systems are broken. 1 in 4 children under the age of 5 have not had their birth registered and hence do not officially exist. As a result, they struggle to access basic rights like education, healthcare and social protection. Two thirds of the world's deaths are not recorded, meaning that governments cannot design effective public health policies or measure their impact.

Through our extensive research of CRVS systems around the world we understand many of the specific challenges that are often experienced by civil registration staff and the families trying to register vital events:

* The civil registration processes are bureaucratic and time-consuming, with requests for supporting documents that family members do not possess and unofficial payments.
* Family members need to travel long distances to register vital events with several trips often required before the registration process is complete and a certificate is obtained.
* Systems are not integrated so birth registration does not lead to automatic access to other rights e.g. vaccination programmes, enrolment in social protection schemes etc.

### Our Product Commitments

We continue to stand by our original product commitments for OpenCRVS and these help steer the strategic direction of the product.

1. Fully open-source, with no license fees or ties to specific vendors
2. Configurable for all country contexts
3. Interoperable with other government systems
4. Highly accessible to ensure inclusion, even in remote areas
5. Safe and secure to keep personal data protected
6. Easy to deploy and use in low resource settings
7. Enabling new models of civil registration that can help achieve universal registration

### Our Design Principles

We are passionate about designing a product that fulfils our mission - to make civil registration easy and valuable for everyone by making high-quality and cost-effective digital systems widely available and sustainable. Our design principles are here to provide a clear framework to all those working on OpenCRVS of how to make design decisions that will affect how the product works.

#### **Start with users' needs**

Listen to, engage with and observe users. Spend time to understand their needs, assume nothing, and work with your users to create designs.

#### **Prioritise offline**

Every product feature must work offline and in areas of low connectivity. Where connectivity is required to complete an action, tell the user what's happening and always consider the loading state.

#### **Give guidance throughout**

The user shouldn't have any questions about what to do - it should be intuitive. Make the product simple and offer clear guidance every step of the way.

#### **Test, learn and iterate**

The best way to develop new features is to get an early version into the hands of users, then listen -> learn -> iterate.

#### **Enable rights**

We want to empower and protect those who use and are served by OpenCRVS. Is what you are designing likely to exclude or discriminate anyone? How can this be avoided?

#### **Be consistent**

Every part of the product should look and feel part of the whole - always use of the component library.

#### **Be hyper-accessible**

Our users are from across the world with varying levels of digital literacy. Whatever we design must be intuitive, legible and as accessible as possible.

#### **Words matter**

Every word should be understood by users, with no room for ambiguity. When drafting text, avoid use of administrative language and test it with local users.

#### **Design with data**

Use data generated from the system to inform design improvements.

#### **Consider other contexts**

OpenCRVS is a global product. Consider the variability of what you are designing - will it work in other countries and contexts, and how will it be easily configured?


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.7/readme.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
