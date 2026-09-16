---
title: "Monitoring"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/monitoring"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/monitoring.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:0060464819e657bfabbee3427dafdd6dcd1ccd879a8dbff8ec20bf9676f11c91"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/monitoring.md).

# Monitoring

### 1. Introduction

Monitoring is an essential operational activity for every OpenCRVS implementation. Effective monitoring enables support teams to identify and resolve issues before they affect users, helping to maximise system availability and minimise service disruption.

This page provides a high-level overview of monitoring and alerting within OpenCRVS. The [technical monitoring guidance](/technical/guides/monitoring.md) explains how to configure monitoring tools, create alerts and investigate operational issues.

**Where this sits:** Monitoring begins immediately after Go-live and continues throughout the lifetime of the system as part of routine operations and support.

***

### 2. Why monitoring matters

Operating a national civil registration system requires continuous oversight of both the application and the infrastructure on which it runs.

Many operational issues develop gradually before users notice them. Examples include increasing disk usage, failing services, repeated authentication attempts or application errors. Monitoring allows support teams to detect these conditions early and take corrective action before they become service outages.

Monitoring should therefore form part of the responsibilities of all operational support teams.

***

### 3. Monitoring OpenCRVS

OpenCRVS provides monitoring capabilities that allow support teams to observe both system health and application behaviour.

At a high level, monitoring consists of:

**Monitor infrastructure health** — ensure that servers and supporting services remain healthy by monitoring system logs, resource utilisation, storage capacity and security-related events.

**Monitor application behaviour** — identify application errors and exceptions as users experience them, allowing issues to be investigated before they become widespread.

**Respond to alerts** — configure automated notifications so that operational teams are informed whenever predefined conditions are met, allowing timely investigation and resolution.

**Investigate incidents** — use historical logs and diagnostic information to determine the cause of issues and verify that corrective actions have resolved them.

***

### 4. Monitoring tools

OpenCRVS provides recommended tools to support operational monitoring.

**Kibana** provides operational visibility into the infrastructure and OpenCRVS services. It can be configured to send automated email alerts for conditions such as:

* server and application log events
* failed SSH login attempts and other security events
* disk space exhaustion
* service failures
* other infrastructure health indicators

Kibana also provides searchable historical logs for each OpenCRVS service, allowing support teams to investigate incidents over a configurable retention period.

**Sentry** monitors application errors from the user's perspective. It captures software exceptions and performance issues as they occur, enabling support teams to identify defects, understand their impact and prioritise corrective action.

Together, these tools provide a comprehensive view of both infrastructure health and user experience.

***

### 5. Operational responsibilities

Monitoring is only effective when alerts are acted upon. Project teams should establish operational procedures that define:

* who receives alerts
* how incidents are prioritised and escalated
* expected response and resolution times
* how incidents are investigated and documented
* how recurring issues are analysed and permanently resolved

Monitoring should be considered an integral part of the L1-L3 support process, helping teams detect problems early, maintain service availability and continually improve the reliability of the OpenCRVS deployment.

***

### 6. Resources and support

Understand [operational support](/implementation/your-opencrvs-project/operational-support.md) service level expectations

Technical [monitoring guides](/technical/guides/monitoring.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/monitoring.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
