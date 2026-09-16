---
title: "Seeding a server environment"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:a333605ec77e357a89e4814c1454b0983f77d7f2826188fe89638f9aa6858a35"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md).

# Seeding a server environment

### Introduction

Seeding, is the process of installing reference data created in configuration onto servers before they are ready to go-live. Seeding is a one-time only operation and can only be reverted by re-setting. After going live, configuration reference data is only manageable via APIs.

### Before you begin

OpenCRVS helm chart seeds data at installation time and can be performed only on empty database.

### Data seed flows

There are few scenarios when you need to seed data again:

* **Changes to Country config codebase:** In that scenario please complete following steps:
  * [Run OpenCRVS deployment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment.md): Codebase will be deployed on target environment
  * [Reset a server environment](/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md): Cleanup database for update with new schema and data
  * [Run "Seed data" workflow](#run-seed-data-workflow): Populate new schema and data
* **Reset environment to initial state:**
  * [Reset a server environment](/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md)
  * [Run "Seed data" workflow](#run-seed-data-workflow)
* **Seed was not executed at installation time due to any kind of errors:** In this case run data seed manually, see [Run "Seed data" workflow](#run-seed-data-workflow)

### Run "Seed data" workflow

If for some reason data seed was not executed at OpenCRVS installation time, please use instructions from this page to seed your database.

1. Navigate to GitHub Actions within `infrastructure` repository
2. Select "Seed data" action
3. Select "Target environment" from dropdown menu, all environments created in the [Create a Github Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step, should be listed here.
4. Click "Run workflow" button

If an error occurs, the environment must be reset before it can be seeded again. Resetting an environment is explained [here](/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md). **Resetting clears all data on the server. Only a backup can restore a previous configuration. Use with caution and see warning below.**

{% hint style="warning" %}
**After going live, a production server environment cannot be re-seeded. To manage locations or users after going live, use the APIs or the Team management UI**
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
