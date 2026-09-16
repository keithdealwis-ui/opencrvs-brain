---
title: "Static TLS certificates"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e588432142cfa9ec05d37743dbdf3226a02c7838f296185577c29d1eb3a4392a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates.md).

# Static TLS certificates

## Static TLS certificates

{% hint style="info" %}
`yarn environment:init` script automatically handles this configuration you, check the [Create a Github Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step
{% endhint %}

#### Static TLS certificates

Traefik requires access to key and certificate files which your certificate supplier must provide to you. In the previous step these were created by `certbot` for LetsEncrypt but other certificate providers will provide equivalent files albeit they may be named differently. The files that Traefik requires are:

**.crt**

This is the certificate "Full Chain File", equivalent to the `fullchain.pem` file that is created by `certbot`. The full chain file combines both your domain's certificate and the intermediate certificates in a single file.

**.key**

This file holds the private key associated with your SSL certificate, equivalent to the `privkey.pem` file that is created by `certbot`. **It's crucial to keep this file secure and private, as anyone with access to it can impersonate your domain.**

Static TLS certificate files have an expiry, therefore they need to be refreshed. The default country configuration doesn't provide an automated way to do this, but the following snippets explain how static files and their refresh can be automatically configurable going forward.

1. Create temporal folder to store certificate and private key. Folder can be created in your home directory or in any other safe place:

```
mkdir $(date +%F)
```

Example folder name: `2025-10-31`

2. Copy and rename certificate and private key files:
   * Certificate file name should be cert.pem
   * Private key file name should be private.key Example folder content:

```
~/2025-10-31$ ls -1l
total 12
-rw-r--r-- 1 bob bob 4128 Oct 27 15:43 cert.pem
-rw-r--r-- 1 bob bob 3243 Oct 27 15:43 private.key
```

3. Make sure you are connected to correct kubernetes cluster, you need to check your kubernetes context:

```
kubectl config current-context
```

Example output: In this output `bob` is your user name, `tmp-k8s-server` is master node name:

```
bob@public-k8s-tmp-k8s-server
```

4. Navigate to folder with certificates:

```
cd $(date +%F)
```

5. Create kubernetes secret in `traefik` namespace:

```
kubectl create secret tls traefik-cert  --cert=cert.pem --key=private.key -n traefik
```

* `tls`: is special kubernetes secret type
* `--cert=cert.pem --key=private.key`: are properties passed for secret creation
* `traefik-cert`: is kubernetes secret name
* `traefik`: is namespace

6. Verify the secret was created:

```
kubectl get secret -n traefik traefik-cert
```

Example output

```
NAME           TYPE                DATA   AGE
traefik-cert   kubernetes.io/tls   2      3m
```

7. Update traefik helm chart values by adding following code snippet to `environments/<env name>/traefik/values.yaml`

```yaml

# 👇 Disable ACME
certificatesResolvers: {}

# 👇 Custom TLS configuration
tlsStore:
  default:
    defaultCertificate:
      # Provide secret name from previous step
      secretName: traefik-cert

```

Check full example at [examples/dev/traefik/values-custom-ssl](https://github.com/opencrvs/infrastructure/blob/develop/examples/dev/traefik/values-custom-ssl.yaml)

8. Commit and push changes
9. Run "Deploy dependencies" workflow or re-deploy traefik helm chart manually


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
