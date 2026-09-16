---
title: "Add Custom GitHub secrets to Kubernetes"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/add-custom-github-secrets-to-kubernetes"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/add-custom-github-secrets-to-kubernetes.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:35ca84b2be59a776e13c8d9610e1a221baf8d1679c18fef8864d74d01d98cb2c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/add-custom-github-secrets-to-kubernetes.md).

# Add Custom GitHub secrets to Kubernetes

GitHub secrets are widely used to store sensitive information for CI/CD and Runtime. Secrets examples are DockerHub credentials, Disk encryption key, Kibana credentials, Postgres and Elasticsearch admin passwords, etc.

GitHub secrets are grouped per environment and at repository level, secret defined for environment will override value at repository level.

## Default secrets mapping

OpenCRVS Helm chart stores database connection properties and other sensitive data like SMTP configuration, backup credentials as Kubernetes secrets.

Check following link for default secrets specification at [Authentication configuration](https://github.com/opencrvs/opencrvs-core/tree/develop/charts/opencrvs-services/README.md#authentication-configuration) (helm chart README.md)

## SMTP secret mapping example

Country config image requires SMTP server configuration for emails. Following environment variables are required for container:

* SENDER\_EMAIL\_ADDRESS
* SMTP\_HOST
* SMTP\_PASSWORD
* SMTP\_PORT
* SMTP\_SECURE
* SMTP\_USERNAME
* ALERT\_EMAIL

Full description is at [Environment secrets and variables explained](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment/environment-secrets-and-variables-explained.md)

Steps to add GitHub secrets to Kubernetes

1. Create required variables at GitHub. E.g if you need SMTP configuration, make sure all variables from the list above are present under GitHub environment or repository level.

   <figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-46e5b422eb32cb2bb4abf13388b5796b971e46e2%2Fimage%20(12).png?alt=media" alt=""><figcaption><p>Email server secrets are defined for QA environment</p></figcaption></figure>
2. Map GitHub secrets to respective Kubernetes secret or secrets by defining secret in mapping file. One Kubernetes secret may contain multiple GitHub secrets as keys. It's reasonable to store all SMTP secrets as one Kubernetes secret `smtp-config`:<br>

   <pre class="language-yaml" data-title="Example for mapping all GitHub secrets required for country config SMTP configuration into single Kubermetes secret &#x22;smtp-config&#x22;"><code class="lang-yaml"># smtp-config: Kubernetes secret name
   smtp-config:
     # type: Kubernetes secret type
     type: Opaque
     # data: Mapping between particular GitHub secret 
     # and Secret key inside kubernetes secret
     # Format is &#x3C;GH Secret>:[Kubernetes secret key],
     # If the Kubernetes Secret key is omitted, the GitHub secret name will be used as the key.
     data:
       - SENDER_EMAIL_ADDRESS
       - SMTP_HOST
       - SMTP_PASSWORD
       - SMTP_PORT
       - SMTP_SECURE
       - SMTP_USERNAME
       - ALERT_EMAIL
   </code></pre>

   1. For mapping secrets in dependencies: [.github/TEMPLATES/secret-mapping-opencrvs-deps.yml](https://github.com/opencrvs/infrastructure/blob/develop/.github/TEMPLATES/secret-mapping-opencrvs-deps.yml)
   2. For mapping secrets in OpenCRVS: [.github/TEMPLATES/secret-mapping-opencrvs.yml](https://github.com/opencrvs/infrastructure/blob/develop/.github/TEMPLATES/secret-mapping-opencrvs.yml)
3. Map values from secret to particular container in helm chart values:\
   Check documentation for more information: [Mapping secrets](https://github.com/opencrvs/opencrvs-core/blob/develop/charts/opencrvs-services/README.md#mapping-secrets) (Helm chart README.md)

   <pre class="language-yaml" data-title="Example of mapping secret keys from &#x22;smtp-config&#x22; secret to countryconfig service"><code class="lang-yaml">countryconfig:
     secrets:
       smtp-config:
         - ALERT_EMAIL
         - SENDER_EMAIL_ADDRESS
         - SMTP_HOST
         - SMTP_PASSWORD
         - SMTP_PORT
         - SMTP_SECURE
         - SMTP_USERNAME
   </code></pre>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/add-custom-github-secrets-to-kubernetes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
