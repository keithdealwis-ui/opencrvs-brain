---
title: "Set up Github and Dockerhub accounts"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/set-up-github-and-dockerhub-accounts"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/set-up-github-and-dockerhub-accounts.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:0a90eae31b603a68fca5256e4891dab18e04c9ab72f986c4437b21be2fbe3258"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/set-up-github-and-dockerhub-accounts.md).

# Set up Github and Dockerhub accounts

In the previous step you set up a country configuration package with a minimal example configuration.

Next, you want to commit all changes to a repo and build your countryconfig Docker image using the Github Actions and a [**Dockerhub**](https://hub.docker.com/) account.

#### 1. Use a GitHub Organisation

The country configuration repository should be stored into a **GitHub Organisation**, not a personal GitHub account.

Your organisation should:

* use a **Github Team** or **Enterprise** plan (required for branch protection rules and Github Actions minutes)
* grant you **Administrator** permissions on the repository

Using an organisation simplifies collaboration, governance and access management throughout the lifetime of the project.

#### 2. Choose a repository name

Rename the repo to represent your own country implementation. E.G.

```
opencrvs-<country-name>
```

#### 3. Plan your branching strategy

We recommend adopting a Gitflow-style branching strategy to separate development, testing and production releases.

| Branch               | Purpose                   |
| -------------------- | ------------------------- |
| `main` (or `master`) | Deployment configuration  |
| `develop`            | Development configuration |

This allows configuration changes to be developed independently, tested in the `develop` branch and promoted to `main` only when approved.

#### 4. Define repository governance

Before development begins, configure your repository permissions.

This typically includes:

* adding implementation team members
* assigning code reviewers
* identifying repository administrators
* granting DevOps engineers appropriate deployment permissions

#### 5. Configure branch protection

To protect your production configuration and enforce code review, configure branch protection rules for your repository.

Navigate to:

**Settings → Branches → Add Branch Protection Rule**

Create a protection rule for the `main` branch (and optionally `develop`) with the following recommended settings:

* Require pull request reviews before merging
* Require status checks to pass before merging (when CI is configured)
* Require signed commits (recommended)
* Restrict who can push directly to protected branches

Once configured, test the protection rules by creating and merging a test pull request.

Branch protection helps ensure that all configuration changes are reviewed, validated and traceable before they are deployed.

#### 6. Set up an individual and an organisation account on Dockerhub <a href="#id-1.-set-up-an-individual-and-an-organisation-account-on-dockerhub" id="id-1.-set-up-an-individual-and-an-organisation-account-on-dockerhub"></a>

You will also need a container registry to store your country configuration Docker image. OpenCRVS is configured to use **Docker Hub** by default, although you can modify the infrastructure to use another container registry if preferred.

Create a **Docker Hub Organisation** and add all developers as members so they can publish and access images. Then create a **single private repository** to store your country configuration image. This repository will be accessed by both your development team and your OpenCRVS servers during deployment.

Docker Hub's free plan includes one private repository, which is sufficient for a typical OpenCRVS implementation.

Creating a private Dockerhub repository for a countryconfig forked container:

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-b986618ed5f3516583b78e6d5ee2848b280c93b9%2Fimage%20(1)%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

Ensure that the Dockerhub members have permissions to write to the repository:

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-3fad32c86118be40da9945f42c827c179e4fcdcb%2Fimage%20(21).png?alt=media" alt=""><figcaption></figcaption></figure>

You will need your Dockerhub **username** and a personal Dockerhub account **access token**. Our scripts use these credentials to login to Dockerhub programmatically. This is how you create a Dockerhub access token: <https://docs.docker.com/security/for-developers/access-tokens/>

#### 7. Ensure your Docker image can be built successfully

When you create a [Github environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md), you enter these Dockerhub login values, and they are saved into Github repository secrets.

When you merge any pull request into the "main", "master" or "develop" branch, or if you explicitly run the "Publish image to Dockerhub" Gthub Action, a docker container image will be built and pushed to Dockerhub for your **countryconfig** microservice.

{% hint style="info" %}
The image will automatically be tagged with the Git commit hash. You will use this hash when deploying.
{% endhint %}

In [Github repository secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), you can also manually set the following values and the above will occur.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-31fd5f99ec65095fdb809b89788706219248e6fd%2Frepo-secrets.png?alt=media" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/set-up-github-and-dockerhub-accounts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
