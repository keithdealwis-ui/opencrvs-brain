---
title: "Architecture"
source_url: "https://documentation.opencrvs.org/v1.9/technology/architecture"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/architecture.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f50fc5626d00decbcf2479989f14e0a998287d7af41dc6784093395518fba7de"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/architecture.md).

# Architecture

OpenCRVS technical architecture is designed using modular, event-driven [microservices](https://en.wikipedia.org/wiki/Microservices). Each microservice and every OpenCRVS component is configurable, scalable and protects data sovereignty by being provisionable in on-premise private tier 2/3 data centres using included [Docker Swarm](https://docs.docker.com/engine/swarm/) configurations.

{% embed url="<https://youtu.be/u8dZcDpS6XU>" %}

To learn about the server hosting & network architecture required for hosting OpenCRVS visit [this section.](/v1.9/setup/3.-installation/3.3-set-up-a-server-hosted-environment.md)

OpenCRVS provides:

* Easy country configuration via a dedicated config microservice, simple csv files and a configuration UI.
* Standards-based multi-language content management.
* A market-leading, powerful search, audit and de-duplication engine powered by [Elasticsearch](https://www.elastic.co/).
* An Amazon S3 compatible object store for storing supporting documentation attachments powered by [Minio](https://min.io/).
* An automated continuous integration, delivery and testing suite.
* A single JS, [TypeScript](https://www.typescriptlang.org/) codebase for backend, desktop and mobile using [Progressive Web Application technology](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Introduction) for offline and low-connectivity access.
* External server and application health monitoring using [Kibana](https://www.elastic.co/kibana/)
* Automatic [LetsEncrypt](https://letsencrypt.org/) SSL configuration
* SMS 2-Factor Authentication with well defined user role authorization privileges
* HTTP hooks for programmatically extending the backend business logic

OpenCRVS is a full-stack that is designed to give you the lowest possible ["total cost of ownership"](https://en.wikipedia.org/wiki/Total_cost_of_ownership).

{% embed url="<https://www.figma.com/community/file/1576304609126977924>" %}

#### Docker Swarm

[Docker Swarm](https://docs.docker.com/engine/swarm/) was chosen by our architects in 2018 because, at the time, dependencies supporting bare-metal installations for Kubernetes architectures were in their infancy and difficult to understand.

Many countries cannot legally support international data storage of citizen data on a public cloud so were dependant on something quick and easy to install in a Tier-2 data centre.

#### **Kubernetes available in OpenCRVS 2.0**

Since 2018, Kubernetes bare-metal tooling has advanced significantly. Our work-in-progress [Kubernetes](https://kubernetes.io/) installation will be easier to use and configure. As of OpenCRVS 1.9, Docker Swarm is still the supported deployment mechanism.

Previously unskilled system administrators can quickly up-skill in the techniques of Docker infrastructure management using Docker Swarm.

#### **Databases**

OpenCRVS uses [Elasticsearch](https://www.elastic.co/), an industry standard, NoSQL document orientated, real-time de-duplication & search engine. Lightning fast, intelligent civil registration record returns are possible, even with imprecise “fuzzy” search parameters.

De-duplication management to ensure data integrity is essential to any civil registration system. A fast search engine lowers operational costs and improves the user experience for frontline staff.

Elasticsearch is also used with [Kibana](https://www.elastic.co/kibana) for application and server health monitoring.

Event data is stored in [PostgreSQL](https://www.postgresql.org/)

Some legacy code in OpenCRVS 1.9 still uses [MongoDB](https://www.mongodb.com/) and [InfluxData](https://www.influxdata.com/). These dependencies will be deprecated.

Analytics are developed in [Metabase](https://www.metabase.com/), but any BI tool can be used as a substitute.

#### Microservices

The core of OpenCRVS is a monorepo organised using [Lerna](https://github.com/lerna/lerna). Each package represents a single NodeJS microservice. Following the [microservice](https://en.wikipedia.org/wiki/Microservices), 1 service per container model, every package is independently scalable in a single [docker](https://www.docker.com/) container.

![](https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-c5aaca6d3e131910ea5b924420226c74e8a3f2b8%2Fimage%20\(8\).png?alt=media) ![](https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-471dc93293df45d85b6955f6e225f33738212f50%2Fimage%20\(4\).png?alt=media) ![](https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-28540fcd8d5ba39391224103a52563b4cc9b0f7a%2Fimage%20\(27\).png?alt=media)\\

The OpenCRVS microservice architecture enables continuous evolution of its business requirements.

The microservices are written in [TypeScript](https://github.com/microsoft/TypeScript) (a strictly typed superset of JavaScript that compiles to JavaScript)

Each microservice in OpenCRVS has no knowledge of other services or business requirements in the application, and each exposes it’s capabilities via [JWT](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/) secured APIs.

<div align="left"><img src="https://static.wixstatic.com/media/93440e_8452ed95c717459e86c95ed0e17378ad~mv2.png/v1/fill/w_136,h_70,al_c,q_80,usm_0.66_1.00_0.01/PWA-Progressive-Web-App-Logo.webp" alt=""></div>

<div align="left"><img src="https://static.wixstatic.com/media/93440e_50ed7c9e719e44daa7ca7d3e183f4071~mv2.png/v1/fill/w_121,h_55,al_c,q_80,usm_0.66_1.00_0.01/react.webp" alt=""></div>

Client applications are built using [React](https://reactjs.org/) and [progressive web application](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Introduction) technology. This means that we can take advantage of offline functionality and native mobile features using [Workbox](https://developers.google.com/web/tools/workbox), without the TCO overhead of maintaining multiple web and mobile codebases and respective App/Play Store releases. In remote areas, registrars can save a configurable number of registrations offline on their mobile phone, using Chrome's [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
