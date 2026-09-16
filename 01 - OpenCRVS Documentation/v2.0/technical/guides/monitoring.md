---
title: "Monitoring"
source_url: "https://documentation.opencrvs.org/technical/guides/monitoring"
markdown_url: "https://documentation.opencrvs.org/technical/guides/monitoring.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b63da78907d60cf23f696afddf22edaf6246f3b46b46e24551fb5ef6885a0903"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/monitoring.md).

# Monitoring

### 1. Introduction

Monitoring is essential for maintaining a healthy, reliable, and performant OpenCRVS installation. The OpenCRVS monitoring suite provides comprehensive visibility into infrastructure health, application performance, and system behavior.

OpenCRVS comes with a pre-installed suite of tools for monitoring and debugging a live installation. The [Elastic Stack](https://www.elastic.co/elastic-stack) is used to monitor the infrastructure, applications, and dependencies, and also for sending alerts on application errors and system health. All of these tools are accessed using [Kibana](https://www.elastic.co/kibana), a free and open user interface that lets you access all your Elasticsearch data, including metrics, logs, and other monitoring information.

{% hint style="info" %}
**Server-hosted environments only** — These tools are only available for server-hosted environments and are not part of the development environment.
{% endhint %}

### 2. Monitoring features

OpenCRVS monitoring provides the following core capabilities:

* **Reading and searching application logs** — view detailed logs from all services to debug issues and understand system behavior.
* **Infrastructure performance insights** — monitor disk space, CPU, and memory usage to know when to scale up.
* **Application Performance Monitoring (APM)** — track service performance, detect bottlenecks, and identify errors.
* **Automated alerting** — receive notifications for application errors and infrastructure health issues.
* **Request tracing** — follow requests through multiple services to understand the full lifecycle.

***

### 3. Getting started with Kibana

Once the environment is installed, the monitoring suite can be accessed using the `kibana.<your_domain>` URL.

#### Login credentials

The login credentials are the ones you used as `KIBANA_USERNAME` and `KIBANA_PASSWORD` as part of the [deployment](https://github.com/opencrvs/documentation/tree/master/v1.9.0/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.6-deploy-automated-and-manual), or the username "elastic" and `ELASTICSEARCH_SUPERUSER_PASSWORD`.

***

### 4. Monitoring tools

OpenCRVS uses several specialized tools as part of the monitoring stack:

#### 4.1 Metricbeat

Metricbeat gets installed on all host machines in your infrastructure. Its sole purpose is to collect data about the network, the host machines, and the Docker environment. The data is stored in the OpenCRVS Elasticsearch database.

This data can be viewed by navigating to **Observability** → **Metrics** and selecting either **Inventory** or **Metrics Explorer**. The data can be visualized, grouped, and filtered in these views.

#### 4.2 Application Performance Monitoring (APM)

The OpenCRVS monitoring stack comes with a pre-installed Application Performance Monitoring tool (APM). This tool collects performance metrics, errors, and HTTP request information from each of the services in the OpenCRVS stack.

You can find this tool in Kibana by navigating to **Observability** → **APM** → **Services**. This tool can be used to:

* Catch anomalies such as errors happening inside the services
* Detect bottlenecks in the architecture
* Identify which services should be scaled up

#### 4.3 Logstash

Logstash receives log entries in [GELF format](https://docs.graylog.org/docs/gelf) from all OpenCRVS services and writes them into the Elasticsearch database.

These logs can be viewed in real-time from **Observability** → **Logs** → **Stream** or through APM.

\<aside> ⏰

**Log retention** — By default, OpenCRVS stores all logs for three days before they are removed.

\</aside>

***

### 5. Monitoring topics

The following pages provide detailed guidance on specific monitoring topics:

#### [Application logs](/technical/guides/monitoring/application-logs.md)

Learn how to access, search, and trace application logs to debug issues and understand system behavior.

#### [Infrastructure health](/technical/guides/monitoring/infrastructure-health.md)

Monitor critical infrastructure metrics such as disk space, CPU usage, and memory consumption to proactively manage resources.

#### [Routine monitoring](/technical/guides/monitoring/routine-monitoring.md)

Establish daily monitoring practices and understand the built-in alerts to maintain a healthy installation.

#### [Setting up alerts](/technical/guides/monitoring/setting-up-alerts.md)

Configure custom alerts to notify you when critical conditions occur, ensuring rapid response to issues.

***

### 6. Read more

* [Elasticsearch disk management](/technical/guides/installation/advanced-topics/elasticsearch-disk-management.md)
* ​[OpenCRVS Dependencies and monitoring helm chart README.md](https://github.com/opencrvs/opencrvs-core/blob/develop/charts/dependencies/README.md)​
* ​[Kibana — your window into Elastic](https://www.elastic.co/guide/en/kibana/current/introduction.html#introduction)​
* ​[Application Performance Monitoring (APM)](https://www.elastic.co/observability/application-performance-monitoring)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/monitoring.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
