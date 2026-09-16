---
title: "Deployment"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/deployment"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/deployment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:042f6b7e48a2f3044ee2d4992ddca467a6f5f3cb610b7b491b772086b0de5da6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/deployment.md).

# Deployment

### 1. Introduction

Deployment is the process of making your configured OpenCRVS system available for users to access. It takes the validated country configuration and installs it into the environments where the system will operate, ensuring that the software, infrastructure, integrations and supporting services are ready for quality assurance and production use.

This page is a high-level, non-technical overview of what deployment involves and the activities required before go-live. The detailed technical procedures for installing, upgrading and operating OpenCRVS are covered in the technical deployment guides.

***

### 2. What goes into deployment

Deployment brings together everything needed to run and maintain OpenCRVS.

This includes:

* Infrastructure (cloud or on-premise server configuration)
* Environments (Server installations for Development, QA, Staging (production mirror), Production & Backup)
* Networking (VPN, DNS & TLS certification)
* Continuous integration and deployment pipelines (e.g. Github Actions)
* Communications method (Email, SMS)
* Databases and storage
* Integrations with external systems
* Security configuration (secrets & secrets management, SSH access controls)
* Monitoring, logging and alerting services

***

### 3. How deployment works

OpenCRVS is deployed using containerised services that can run either in cloud infrastructure or on-premise environments. The deployment process installs the OpenCRVS platform together with the country's validated configuration and supporting services.

At a high level, deployment consists of:

**Prepare the supporting services & networking** — Confirm the hosting provider and/or data center meets the required specifications, set up code repositories, set up SMTP or communications APIs, define required environments, configure DNS networking for each environment following your desired URL pattern, purchase TLS certificates, select containerisation directory provider.

**Prepare the infrastructure** — Provision the servers, networking, storage and security required for the target environment, whether development, QA, staging or production.

**Deploy the OpenCRVS core and country configuration** — install the OpenCRVS services, databases and supporting infrastructure. Build & deploy the validated country configuration, including forms, business rules, workflows, certificates and dashboards.

**Configure integrations** — connect OpenCRVS to any external services such as identity providers, authentication services, notification systems, health information systems or national data platforms.

**Operationalise** — enable monitoring, logging, backups, disaster recovery and routine operational processes to support the live system.

**Verify the deployment** — confirm that all services are running correctly, integrations are functioning and users can successfully access the system.

Each of these activities is described in detail in the technical deployment guides. Deployment is typically led by a Technical System Administrator, working closely with infrastructure teams and any cloud or hosting providers to ensure the environment is correctly configured and operational.

***

### 4. Resources and support

* [Technical installation guides](https://documentation.opencrvs.org/v2.0/technical/guides/configuration) — step-by-step instructions for installing OpenCRVS on servers
* [Maintenance tasks](/technical/guides/installation/opencrvs-maintenance-tasks.md) — guides for backup, database seeding & disaster recovery
* [Advanced topics](/technical/guides/installation/advanced-topics.md) — guides regarding networking and TLS
* [Monitoring](/technical/guides/monitoring.md) — guides for monitoring & logging

If you require assistance with deployment planning, infrastructure design or production operations, contact the OpenCRVS community or your implementation partner for guidance.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/deployment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
