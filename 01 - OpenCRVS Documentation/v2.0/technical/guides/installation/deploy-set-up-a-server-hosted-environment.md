---
title: "Deploy: Set-up a server-hosted environment"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b47f34c6bca42bdf4ff6fccc61a8007779f6d87151a7cc96df572bfe458f9f38"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment.md).

# Deploy: Set-up a server-hosted environment

In this chapter, you will learn how to create and configure the infrastructure and all required components for an OpenCRVS deployment using GitHub Actions workflows.

These workflows guide you through the installation and configuration of OpenCRVS on servers

The **essential** [**preparation steps**](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps.md) guide you through the following:

* Provision servers (virtual machines) & VPN.
* Configure DNS and obtain SSL certificates.
* Set up an SMTP server.
* Create the required accounts:
  * GitHub organisation
  * Docker Hub
  * 1Password (or another secrets manager)
  * Optional: other services such as Slack and Sentry

#### Fork the required repositories

If you have not already done so in the [Quick Start](/technical/guides/installation/quick-start.md), fork the [countryconfig](https://github.com/opencrvs/opencrvs-countryconfig) repository and configure its CI process to push images to your container registry. See [**Fork and build the countryconfig repo**](/technical/guides/installation/set-up-github-and-dockerhub-accounts.md)

Fork the [infrastructure](https://github.com/opencrvs/infrastructure) repository.

{% hint style="info" %}
The country configuration repository contains an [infrastructure](https://github.com/opencrvs/opencrvs-countryconfig/tree/develop/infrastructure) folder which supports: **Backwards compatibility for OpenCRVS versions 1.9 and below still using DockerSwarm. Docker Swarm will be deprecated in 2.1.** [**MIGRATE TO KUBERNETES IN TIME!**](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/migration-from-docker-swarm-guide.md)
{% endhint %}

All steps are described in detail in this chapter.

**Once the preparation steps are complete,** proceed with the installation steps **in order, starting with creating a Github environment**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
