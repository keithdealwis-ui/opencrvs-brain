---
title: "Deploy OpenCRVS with external data stores"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/deploy-opencrvs-with-external-data-stores"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/deploy-opencrvs-with-external-data-stores.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e8f9c2e0e55c0511de14a05ada3dbaf10fa69f527363c4fc7f93b32f5588878a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/deploy-opencrvs-with-external-data-stores.md).

# Deploy OpenCRVS with external data stores

## General information

OpenCRVS can be deployed on decoupled infrastructure with clear permissions and responsibilities segregation. Default environment configuration script doesn't support advanced deployment scenario.

Only full backup and restore process jobs have support for decoupled data stores. Please refer to official Postgres and MinIO documentation how to configure backup/restore.

Supported data stores:

* MinIO
* Elasticsearch
* Postgres

## Postgres

This guide doesn't cover Postgres installation and configuration

Assumptions made:

* Database server port 5432 is available from Kubernetes nodes
* OpenCRVS DevOps/Sysadmin has Postgres admin user credentials

### Configure OpenCRVS to use external Postgres

1. Modify GitHub secrets for your environment:
   1. `POSTGRES_USER`
   2. `POSTGRES_PASSWORD`
2. Modify Dependencies helm chart configuration:
   1. Open `environments/<environment>/dependencies/values.override.yaml` and add following lines to disable postgres:

      ```yaml
      postgres:
        enabled: false
      ```
   2. Open `environments/<environment>/opencrvs-services/values.override.yaml` and add following lines to point OpenCRVS to external database server:<br>

      ```yaml
      postgres:
        host: <hostname or IP address>
      ```
3. Commit your changes to GitHub
4. Deploy Dependencies
5. Deploy OpenCRVS

### Postgres admin user configuration

Suppose you want your admin user to be called `adminuser`:

```sql
CREATE ROLE adminuser WITH LOGIN PASSWORD 'your_secure_password';
ALTER ROLE adminuser WITH SUPERUSER CREATEDB CREATEROLE REPLICATION;
```

Copy

**Explanation:**

* `WITH LOGIN`: Allows the user to log in.
* `PASSWORD 'your_secure_password'`: Sets the password (replace this with a strong password).
* `SUPERUSER`: Grants all access; the user can create roles, databases, schemas, tables, etc.
* `CREATEDB`: Allows creating new databases.
* `CREATEROLE`: Allows creating new roles.
* `REPLICATION`: Not necessary unless you want replication privileges (optional).

## MinIO

Assumptions made:

* MinIO internal server ports 9000 and 9001 are available from Kubernetes cluster nodes
* OpenCRVS DevOps/Sysadmin has MinIO admin user credentials
* MinIO frontend is exposed as subdomain of OpenCRVS domain. E/g If OpenCRVS is deployed as opencrvs.example.com then MinIO may have any URL under opencrvs.example.com (my-minio.opencrvs.example.com).

### Configure OpenCRVS to use external MinIO

1. Modify GitHub secrets for your environment:
   1. `MINIO_ROOT_USER`
   2. `MINIO_ROOT_PASSWORD`
2. Modify Dependencies helm chart configuration:
   1. Open `environments/<environment>/dependencies/values.override.yaml` and add following lines to disable MinIO:

      ```yaml
      minio:
        enabled: false
      ```
   2. Open `environments/<environment>/opencrvs-services/values.override.yaml` and add following lines to point OpenCRVS to external MinIO server:<br>

      ```yaml
      minio:
        host: <hostname or IP address>
        port: <port>
      ```
3. Commit your changes to GitHub
4. Deploy Dependencies
5. Deploy OpenCRVS

## Elasticsearch

Assumptions made:

* Elasticsearch server port 9200 is available from Kubernetes nodes
* Elasticsearch admin user name is `elastic` and OpenCRVS DevOps/Sysadmin has password.

### Configure OpenCRVS to use external Elasticsearch

1. Modify GitHub secret for your environment:
   1. `ELASTICSEARCH_SUPERUSER_PASSWORD`
2. Modify Dependencies helm chart configuration:
   1. Open `environments/<environment>/dependencies/values.override.yaml` and add following lines to disable Elasticsearch:

      ```yaml
      elasticsearch:
        enabled: false
      ```
   2. Open `environments/<environment>/opencrvs-services/values.override.yaml` and add following lines to point OpenCRVS to external Elasticsearch server:<br>

      ```yaml
      elasticsearch:
        host: <hostname or IP address>
      ```
3. Commit your changes to GitHub
4. Deploy Dependencies
5. Deploy OpenCRVS


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/deploy-opencrvs-with-external-data-stores.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
