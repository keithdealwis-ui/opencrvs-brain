---
title: "Deploy"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c5654035d62936e8e1ac6bf7a1a0693de00e560e960b76005391327f59c3dc7a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy.md).

# Deploy

This deployment guide covers deployment processes for the following components:

* Traefik: Ingress controller and traffic routing.
* OpenCRVS Dependencies: Datastores, Monitoring
* OpenCRVS Core and Country config template: Core components and Configuration container

All OpenCRVS images except the country configuration template are hosted in the [GitHub container registry](https://github.com/orgs/opencrvs/packages?ecosystem=container).

### Publishing your countryconfig image to Dockerhub

The default country configuration image is hosted on our DockerHub.

You will need to register your own DockerHub account and create a private repository.

The DockerHub login information that you set during Github environment creation is used to compile and store a container image of your countruyconfig microservice. When you merge any pull request into the "main", "master" or "develop" branch, or if you explicitly run the **"Publish image to Dockerhub"** Github Action, a docker container image will be built and pushed to Dockerhub for your **countryconfig** microservice.

Now that you have configured repository secrets for Dockerhub access, you will notice that this action can be successfully run.

If you look at the logs for each build, you can see the image tag associated with the Docker container image. You use this tag in the Deploy action.

Once you are certain that your image is successfully being built and hosted on DockerHub, you can continue.

{% hint style="warning" %}
We strongly recommend that you have enabled an [approval](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/approval-process-for-production-environments.md) process for all deployment scripts to **production** and **staging** environments.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
