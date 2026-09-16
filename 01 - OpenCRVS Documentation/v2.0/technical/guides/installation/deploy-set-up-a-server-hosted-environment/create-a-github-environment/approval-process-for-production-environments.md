---
title: "Approval Process for Production Environments"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/approval-process-for-production-environments"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/approval-process-for-production-environments.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b8a9dedbf490a65030ef58d51133c3fcf993a71ea66c275830596872599621d3"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/approval-process-for-production-environments.md).

# Approval Process for Production Environments

To provide System Administrators and DevOps teams with an additional layer of protection against human error and unauthorized access, an approval process should be configured for production environments.

The list of individuals eligible to approve GitHub workflows is defined by the repository-level variable `GH_APPROVERS`. Each approver must be a valid GitHub account holder and added as a collaborator to the infrastructure repository.

Approval can be enabled for specific environments by setting the `APPROVAL_REQUIRED` variable to `true`. It is strongly recommended to enforce this requirement in production environments to mitigate the risk of accidental deployments or environment resets, which may lead to the deletion of citizen data.

The infrastructure repository should have issues enabled to facilitate the approval process.

**Workflow execution**

As demonstrated in the screenshot below, when approval is enabled for an environment, workflow execution will be paused. An issue will be automatically created within the infrastructure repository, and a link to this issue will appear in the workflow log.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-c304289fb22b17a0ae3e991fc2a285b2b5f159ee%2Fimage%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

The GitHub issue will contain a detailed description outlining exactly what needs approval.

Once the necessary approvals have been received, the workflow execution will resume.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-e41866643fb00957cf8276c7a1e22691b8b9fe90%2Fimage%20(3).png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
For workflows that involve cleaning up environments and potentially wiping all citizen data, at least three approvals are required. This ensures that a minimum of three team members review and approve such critical actions.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/approval-process-for-production-environments.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
