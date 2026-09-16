---
title: "Running an OpenCRVS deployment"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:2e79cd4154813064800d8431d234f49f6c83244f6aa646830c45fa6bfc6e889d"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment.md).

# Running an OpenCRVS deployment

### Preparation steps

Before you can deploy, you need to make sure that your country configuration Docker image has compiled and has been pushed to your container registry (E.G. Dockerhub). This was explained previously in [Fork and buld the countryconfig repo](/technical/guides/installation/set-up-github-and-dockerhub-accounts.md)

Copy the githash tag associated with your **countryconfig** Docker container image because you will use it in the next step.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-084744f90a73a279598b71aeb95414f31dd3d817%2FScreenshot%202023-01-10%20at%2015.51.12.png?alt=media" alt=""><figcaption></figcaption></figure>

### Run OpenCRVS Deployment

You can deploy to your server using the automated **"Deploy OpenCRVS"** Github Action for any environment created at [Create a GitHub Environment](https://github.com/opencrvs/documentation/tree/master/v2.0.0/setup/3.-installation/3.3-set-up-a-server-hosted-environment/4.3.4-create-a-github-environment) step.

1. Navigate to **GitHub Actions** within **`infrastructure`** repository
2. Select **"Deploy OpenCRVS"** workflow
3. Enter the **Tag of the core image**. This usually corresponds to the OpenCRVS release tag, e.g. `v2.0.0`.
4. Enter the **Tag of the country config image**. Use the tag of the image built from your fork of the country config repository.
5. For the initial deployment, enable the **“Data seeding during deployment”** option. Note: You can also seed the environment later.
6. Select **"Target environment"** from dropdown menu.
7. Click "**Run workflow"** button, and monitor the run logs to ensure that the deployment completes successfully.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-a0986b59370a0cc0effcba56cbc5d7eed3f145cf%2Fimage%20(1).png?alt=media" alt=""><figcaption><p>Deploy OpenCRVS GitHub Actions Workflow options</p></figcaption></figure>

### Verification steps

* Verify workflow was completed successfully
* Verify resources are up and running after deployment: `kubectl get pods -n opencrvs-<env>`
* Make sure all helm pre-/post-deploy hooks completed successfully:<br>

  ```
  kubectl get jobs
  ```
* Access opencrvs in browser: `https://<your domain>`

### Next steps

* [Seed OpenCRVS databases with reference data so that you can login](/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md)
* [Login to an OpenCRVS server](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/login-to-an-opencrvs-server.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
