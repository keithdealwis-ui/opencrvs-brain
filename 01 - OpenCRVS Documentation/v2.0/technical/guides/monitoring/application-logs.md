---
title: "Application logs"
source_url: "https://documentation.opencrvs.org/technical/guides/monitoring/application-logs"
markdown_url: "https://documentation.opencrvs.org/technical/guides/monitoring/application-logs.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:132f82469f63e3762655d8c1e1bfd2d54dfd97132e2e38845c2fe469669fec04"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/monitoring/application-logs.md).

# Application logs

### 1. Introduction

All services in the OpenCRVS architecture emit logs that can be observed in real-time. Application logs provide detailed information about system behavior, HTTP requests and responses, informational events, and errors.

The most common use case for viewing logs is debugging an issue with the installation. The logs from each service are collected automatically by Filebeat and sent to Kibana for developers and maintainers to easily access.

**What logs contain:**

* HTTP requests and responses
* Informational logging (for example, countryconfig service sending 2FA email)
* Errors that have happened as part of requests
* System events and state changes

{% hint style="info" %}

* This document covers only basics, for more information how to work with Kibana please visit official website: <https://www.elastic.co/guide/en/kibana/8.19/index.html>
* Discover is not covered on this page, please visit official documentation
  {% endhint %}

### 2. Application logs

To access the logs of a specific service, first log in to Kibana and navigate to **Observability** → **APM** → Service Inventory, open up the service you want to observe:

* For Kubernetes clusters with multiple OpenCRVS instances (environments) use "Environment" filter to choose your environment
* Search log items by providing a time range

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FFKKmHFBRYPERGuGFjw6X%2Fimage.png?alt=media&amp;token=51882a6b-6b33-424c-8ea8-607dea9da3b6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FMXEDe8SGgwr7oLENP3R1%2Fimage.png?alt=media&amp;token=79660dc5-4613-4469-951b-0986674e4dee" alt=""><figcaption><p>Screenshot shows traefik service access logs. View logs for particular environment by narroving down results in "Environment" selector. Use date/time range to select logs for specific interval, use "Actions" to view more details from the log.</p></figcaption></figure>

### 3. Traces view

Another way of finding a specific request is by finding it through the **Observability** → **APM** → **Traces** or Switch to Transactions tab under selected service.

In this view, you can:

* See all requests that happened in the selected time interval grouped by the type of the request
* View average timings and error rates for each request type
* See trace samples of all actual requests made during the specified time interval

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FviyX43txGWfxsKvDXHyO%2Fimage.png?alt=media&amp;token=8f283096-b57a-4d45-98f1-f2cb8c0e39c6" alt=""><figcaption><p>All incoming requests go through Traefik ingress controller, almost always it will be on the top of the list. On the screenshot all transactions that took longer then 1 second (1000000us) are shown.</p></figcaption></figure>

#### Using the traces view

By clicking on the request type you are interested in observing, you can see:

* Average timings for that request type
* Error rates
* Trace samples at the bottom of the page showing all actual requests made during the specified time interval

This is especially useful for:

* Figuring out in which service the request fails
* Detecting bottlenecks in the architecture

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fxcac0Z1BzbgNHXfVX3W4%2Fimage.png?alt=media&amp;token=a11d46af-2fcd-441e-a06d-d3301798abb9" alt=""><figcaption><p>Transaction information is useful to identify particular service latency</p></figcaption></figure>

By clicking on **Investigate** → **Trace logs** you can navigate back to the logs view to see all logs corresponding to the selected request.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/monitoring/application-logs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
