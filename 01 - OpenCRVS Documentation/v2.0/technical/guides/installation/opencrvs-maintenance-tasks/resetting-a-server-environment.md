---
title: "Resetting a server environment"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:22004adbe697904e2e8211a6f46c1bf62c4aec958efd8f9ffec32b5933b62037"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md).

# Resetting a server environment

### Before you begin

The **Reset environment** Github Action can be used to clear a **development,** **qa and staging** environment of all data. This is useful during testing of environments where you may have made test registrations.

{% hint style="info" %}
After resetting your environment, it contains no data at all. It must be seeded again
{% endhint %}

### Run "Reset environment" workflow

{% hint style="danger" %}
Before resetting production environment make sure you have working backup of your data.

In default configuration GitHub action will require at least 3 approvals for Production environment reset.
{% endhint %}

1. Navigate to GitHub Actions within `infrastructure` repository
2. Select "Reset environment" action
3. Select "Target environment" from dropdown menu, all environments created in the [Create a Github Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step, should be listed here.
4. Click "Run workflow" button


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/resetting-a-server-environment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
