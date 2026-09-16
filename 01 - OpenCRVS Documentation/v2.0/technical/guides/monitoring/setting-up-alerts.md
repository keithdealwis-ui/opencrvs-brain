---
title: "Setting up alerts"
source_url: "https://documentation.opencrvs.org/technical/guides/monitoring/setting-up-alerts"
markdown_url: "https://documentation.opencrvs.org/technical/guides/monitoring/setting-up-alerts.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ede53300817d126146de93968ff6f89f79f7b174e05d6a4f536d728a84e3ce1c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/monitoring/setting-up-alerts.md).

# Setting up alerts

### 1. Introduction

Alerts notify you when critical conditions occur in your OpenCRVS installation, allowing you to respond quickly before issues impact users. OpenCRVS comes with preconfigured alerts, but we recommend customizing these alerts to your country's specific needs.

All alerts and thresholds can be managed through **Management** → **Stack Management** → **Alerts and Insights** → **Rules and Connectors**.

### 2. Preconfigured alerts

OpenCRVS comes with the following preconfigured alerts:

| **Type** | **Description**                                | **Threshold** |
| -------- | ---------------------------------------------- | ------------- |
| Alert    | CPU load on any node                           | >70%          |
| Alert    | Service error                                  | >0            |
| Alert    | Available disk space on encrypted data storage | <30%          |

These alerts provide a baseline level of monitoring, but should be customized based on your operational experience and specific requirements.

### 3. Supported alert types

Currently, OpenCRVS supports email alerts out of the box. Other types of alerts (for example, Slack, PagerDuty, webhooks) are available by customizing your country config package.

### 4. Setting up a new alert

Basic instructions for setting up alerts can be found in the Kibana documentation under [Alerts and rules](https://www.elastic.co/guide/en/kibana/master/apm-alerts.html#apm-alerts).

#### Important: Use Index as the connection type

When setting up new alerts, it is important to use **"Index"** as the connection type. This option instructs Kibana to write alerts to an Elasticsearch index from where other tools can get notified about errors happening in the system.

### 5. How alerts are delivered

Our alerting tool [Elastalert2](https://github.com/jertel/elastalert2) reads alerts from a preconfigured index named `kibana-alert-history-default` and is configured to send an email to the `ALERT_EMAIL` email address.

This email address can be changed as part of [deployment](https://github.com/opencrvs/documentation/blob/master/v1.9.0/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.6-deploy-automated-and-manual).

### 6. Customizing alerts for your context

When customizing alerts, consider:

* **Your infrastructure capacity** — set thresholds based on when you need to take action, not just when critical failure is imminent
* **Your support team availability** — ensure alerts go to a monitored inbox or on-call rotation
* **Alert fatigue** — avoid setting thresholds so low that you receive constant alerts; focus on actionable issues
* **Response time requirements** — set more aggressive thresholds for production systems with strict uptime requirements

#### Example customizations

* Lower disk space threshold to 40% if provisioning new storage takes several days
* Add alerts for specific service response times if performance is critical
* Add alerts for failed backup jobs
* Add alerts for SSL certificate expiration (for example, 30 days before expiry)

### 7. Testing alerts

After configuring a new alert:

1. **Test the trigger condition** — temporarily adjust thresholds or simulate the condition to verify the alert fires
2. **Verify delivery** — confirm that alert emails are received by the intended recipients
3. **Check alert content** — ensure the alert message contains enough information to understand and respond to the issue
4. **Document** — update your monitoring procedures to include the new alert and expected response

### 8. Read more

* [Alerting](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/monitoring/setting-up-alerts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
