---
title: "Infrastructure health"
source_url: "https://documentation.opencrvs.org/technical/guides/monitoring/infrastructure-health"
markdown_url: "https://documentation.opencrvs.org/technical/guides/monitoring/infrastructure-health.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ec1844a4e7e8c905ba3c94125919790c17a2adffc77e5f54bafceb496f0455c0"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/monitoring/infrastructure-health.md).

# Infrastructure health

### 1. Introduction

OpenCRVS monitoring tools let you measure and view critical metrics such as available disk space, used memory, and total CPU load. This information can be used to proactively increase available resources when demand increases.

These metrics are collected by a tool called [Metricbeat](https://www.elastic.co/beats/metricbeat) and stored in Elasticsearch.

### 2. Common infrastructure metrics

The following list summarises the most important infrastructure metrics to monitor:

* CPU usage
* RAM usage
* Network RX/TX
* Disk usage usage / IOPs

Navigate to **Observability > Infrastructure > Hosts**:

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FmhQClfYsHdKPFqXcjsd6%2Fimage.png?alt=media&amp;token=b4cdab76-3538-4df4-8396-24a701692df3" alt=""><figcaption></figcaption></figure>

### 3. Kubernetes metrics

Navigate to **Observability > Infrastructure > Infrastructure inventory**:

1. Change "Show" selector to "Kubernetes"
2. Change Presentation view to "Table"
3. From dropdown choose metric

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FdlfiBCUHvJDCdyStlLNy%2Fimage.png?alt=media&amp;token=3387568f-714b-431c-bb0c-17655f0cd574" alt=""><figcaption></figcaption></figure>

### 4. Accessing metrics from Explorer

To view infrastructure metrics, log in to Kibana and navigate to **Observability** → **Metrics** → **Metrics Explorer**.

In this view, you can:

* See current usage of different resources
* Group metrics by host, service, or other dimensions
* Filter and visualize data over time

### 5. Available disk space

To see the amount of available disk space, navigate to **Metrics Explorer** (Observability → Metrics → Metrics Explorer).

You can see the current usage of different storage devices by selecting:

* **Value:** Max of `system.filesystem.used.pct`
* **Grouped by:** `host.hostname` and `system.filesystem.device_name`

#### Filtering for encrypted data storage

The default installation of OpenCRVS uses an encrypted disk for data storage on all nodes named `/dev/mapper/cryptfs`.

You can filter the listed devices to only show these disks by using the following search clause:

`system.filesystem.device_name : "/dev/mapper/cryptfs"`

### 6. CPU usage

To monitor CPU usage:

* **Value:** Average of \[`system.process.cpu.total](<http://system.process.cpu.total>).pct`
* **Grouped by:** `host.hostname`

This shows you the average CPU load across all processes on each host. Use a 24-hour timeframe to identify patterns and peak usage periods.

***

### 6. Memory usage

To monitor memory usage:

* **Value:** `average(system.memory.actual.used.pct)`
* **Grouped by:** `host.name`

This shows you memory usage per Host

Example for Kubernetes container filtered by namespace:

* Metric: `kubernetes.container.memory.usage.bytes`
* group per: `container.name`&#x20;
* Filter by: `kubernetes.namespace`

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2FJbJhd90boTittkJGgouy%2Fimage.png?alt=media&amp;token=49558351-d126-4b2d-b854-2d40990bd2b0" alt=""><figcaption></figcaption></figure>

***

### 7. Read more

* [Host metrics](https://www.elastic.co/guide/en/observability/master/host-metrics.html)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/monitoring/infrastructure-health.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
