---
title: "Routine monitoring"
source_url: "https://documentation.opencrvs.org/technical/guides/monitoring/routine-monitoring"
markdown_url: "https://documentation.opencrvs.org/technical/guides/monitoring/routine-monitoring.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:52f09699e13364563e92ece0a872ea5d431892d71ede5e35dae9837b27a389b6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/monitoring/routine-monitoring.md).

# Routine monitoring

### 1. Introduction

Routine monitoring is essential for maintaining a healthy and reliable OpenCRVS installation. Regular monitoring helps you identify and resolve issues before they impact users, and ensures that your infrastructure is operating within safe limits.

This section provides guidance on daily monitoring tasks and built-in alerts.

### 2. Monitoring and maintenance checklist

We provide a comprehensive document to understand regular tasks required to monitor and maintain a running instance of OpenCRVS.

**Download the checklist:**

Download the Monitoring & Maintenance document and Excel checklist from the "Technical" zip in the [OpenCRVS Requirements Templates](https://github.com/opencrvs/opencrvs-core/wiki/Gather-requirements).

**These cover tasks such as:**

* Tracking the OpenCRVS release and upgrading when required
* Monitoring system upgrades such as for the server operating system
* Refreshing expiring TLS/SSL certificates
* Reacting to automatic alerts from Sentry or Kibana

### 3. Built-in alerts from Kibana

OpenCRVS comes with a built-in set of automatic email alerts that capture a minimal set of critical limits and conditions necessary for the product to work. When these alerts are triggered, the issues need to be solved as soon as possible.

{% hint style="info" icon="gear" %}
**Manual activation required** — After deployment, these alerts are configured automatically. However, you will need to log in to Kibana to manually turn the alerts on after each deployment. We are addressing automatic enabling of these alerts by default in future versions of OpenCRVS.
{% endhint %}

### 4. Daily monitoring checklist

It's a good practice to monitor your production installation's infrastructure manually on a daily basis. This practice improves the reliability of your environment and gives your team a chance to include server improvements in planned work.

#### 4.1 Disk space usage on all nodes is less than 70%

**Steps:**

1. Login to Kibana
2. Navigate to **Observability** → **Metrics** → **Metrics Explorer**
3. Use the parameters listed in the Infrastructure health section under Available disk space
4. Verify all used disk space is under 70% on all nodes

#### 4.2 CPU and memory usage less than 80% on all nodes

**Steps:**

1. Login to Kibana
2. Navigate to **Observability** → **Metrics** → **Metrics Explorer**
3. Use the parameters listed in the Infrastructure health section under CPU usage
4. Select a timeframe of 24 hours
5. Verify CPU load has not exceeded 80% on any of your server nodes

#### 4.3 No errors in any services

**Steps:**

1. Login to Kibana
2. Navigate to **Observability** → **APM** → **Services**
3. Select each service
4. Check the **Errors** tab
5. Investigate any errors reported

### 5. Responding to alerts

When alerts are triggered:

* **Acknowledge immediately** — ensure the team is aware of the issue
* **Assess severity** — determine if immediate action is required or if it can be planned
* **Investigate root cause** — use the monitoring tools to understand what triggered the alert
* **Take corrective action** — resolve the issue or scale resources as needed
* **Document** — log the incident and resolution for future reference

Oftentimes it's better if issues are solved and planned for even before reaching the critical limits. Proactive monitoring helps prevent alerts from triggering in the first place.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/monitoring/routine-monitoring.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
