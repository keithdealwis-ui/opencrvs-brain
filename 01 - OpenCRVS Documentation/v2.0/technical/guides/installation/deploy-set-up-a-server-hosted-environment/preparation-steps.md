---
title: "Preparation steps"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:2faebb5042ca7ca9e94a21065bb740f0db505eaa03b5b8b9c0304908a09288b2"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps.md).

# Preparation steps

#### Before you begin

Before running any scripts, you must complete the following **essential preparation steps**. Please carefully consider the information in these pages.

This section describes the environments, servers and network requirements that countries are required to prepare in order to install OpenCRVS.

We have an automated scripts to generate [Github environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) for you along with all the application secrets that Github needs to run the continuous provisioning and deployment scripts.

Github Actions use environment secrets and variables when installing software on servers and deploying OpenCRVS.

These secrets and variables are entirely dependant on the [prerequisite accounts and repositories](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/create-prerequisite-accounts-and-repositories.md).

#### Further reading

The [Advanced topics](/technical/guides/installation/advanced-topics.md) section gives you important detail on the various configurations related to servers, TLS, SSH access (to comply with internal procedures), Kubernetes cluster management and disk space.

The [OpenCRVS maintenance tasks](/technical/guides/installation/opencrvs-maintenance-tasks.md) section explains how to manage data and disaster recovery.

The [Monitoring](/technical/guides/monitoring.md) section explains how to use the ELK stack to track server and application health and respond to issues.

This further reading guides you through how to configure, provision, deploy and maintain OpenCRVS server deployments technically.

The [configuration inputs](/releases/release-notes.md) in our release notes contain Excel sheets helping you calculate required disk space, and track the acquisition of the required, country owned dependencies.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
