---
title: "Running Dependencies deployment"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-dependencies-deployment"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-dependencies-deployment.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:353db457a0caa1490965d64132376ead1caf6d12188e52948eee0b34c2116842"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-dependencies-deployment.md).

# Running Dependencies deployment

{% hint style="warning" %}
A deployment to a **staging** environment is not permitted unless a **production** environment exists in the GitHub environment. Please ensure a **production** environment is configured before proceeding with any **staging** deployment.
{% endhint %}

### Preparation steps

This section explains how to deploy OpenCRVS dependencies grouped in 2 helm charts:

* **Ingress controller:** [Traefik](https://doc.traefik.io/traefik/) helm chart
* **Datastores** (via the [OpenCRVS dependencies Helm chart](https://github.com/opencrvs/opencrvs-core/tree/develop/charts/opencrvs-services)):
  * MongoDB
  * PostgreSQL
  * Elasticsearch
  * Redis
  * MinIO
  * InfluxDB

Environment configuration script (`yarn environment:init`) prepared configuration files (`values.yaml`) for deployment with default parameters. Navigate to `environments` folder inside infrastructure repository and review configuration files.

Here is an example directory structure for a **development** environment:

```
environments/
├── development
│   ├── dependencies
│   │   └── values.yaml
│   ├── opencrvs-services
│   │   └── values.yaml
│   └── traefik
│       └── values.yaml
└── README.md
```

A default configuration, created by the `yarn environments:init` script, is sufficient for inital deployments, but sometimes you may need to adjust TLS / SSL configuration in `environments/traefik/values.yaml` or tweak some properties here like static storage, etc.

### Run dependencies deployment

1. Navigate to GitHub Actions within `infrastructure` repository
2. Select "Deploy Dependencies" action
3. Select "Target environment" from dropdown menu, all environments created at [Create a GitHub Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step should be listed here.
4. Click "Run workflow" button

### Verification steps

* Verify workflow was completed successfully
* Verify resources are up and running after deployment:
  * `kubectl get namespaces` : You should see 2 new namespaces created (`traefik`, `opencrvs-deps-<env>`).\
    NOTE: Check how to run `kubectl` at [Kubernetes cluster access](/technical/guides/installation/advanced-topics/kubernetes-cluster-access.md).
  * `kubectl get pods -n traefik`: Make sure traefik pod is up and running
  * `kubectl get pods -n opencrvs-deps-<environment>` : make sure datastores are up and running.\
    Example output: If monitoring is enabled, you will also see filebeat, metricbeat, kibana pods.

    ```
    NAME                             READY   STATUS      RESTARTS     AGE
    elasticsearch-0                  1/1     Running     0            8d
    influxdb-0                       1/1     Running     0            8d
    minio-0                          1/1     Running     0            8d
    mongodb-0                        1/1     Running     0            8d
    postgres-0                       1/1     Running     0            8d
    redis-0                          1/1     Running     0            8d
    ```
* Verify that **MinIO** and **Kibana** are available:
  * Kibana URL: `https://kibana.<your domain>`\
    Username and password are stored as Kubernetes secret `elasticsearch-opencrvs-users` in `opencrvs-deps-<environment>` namespace.
  * MinIO URL: `https://minio.<your domain>` . Username and password are stored as Kubernetes secret `minio-opencrvs-users` in `opencrvs-deps-<environment>` namespace.

> NOTE: Credentials are stored at GitHub secrets or can be fetched namespace `opencrvs-deps-<env>`.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-dependencies-deployment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
