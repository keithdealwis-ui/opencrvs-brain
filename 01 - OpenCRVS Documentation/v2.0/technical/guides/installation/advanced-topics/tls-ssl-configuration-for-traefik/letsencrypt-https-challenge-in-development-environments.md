---
title: "LetsEncrypt https challenge in development environments"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-https-challenge-in-development-environments"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-https-challenge-in-development-environments.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:92c1795a59fb6cb8d90d5adb4d268ce64a268cf234931fb4248887c4137cb8aa"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-https-challenge-in-development-environments.md).

# LetsEncrypt https challenge in development environments

## LetsEncrypt https challenge in development environments

#### LetsEncrypt HTTPS Challenge

{% hint style="info" %}
`yarn environment:init` script automatically handles this configuration you, check the [Create a Github Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step.
{% endhint %}

If you are provisioning a **development** environment for learning purposes **outside of a VPN**, then this block is all you need in order to configure the LetsEncrypt HTTPS challenge mechanism for SSL cert generation.

1. Update traefik helm chart values by adding following code snippet to `environments/<env name>/traefik/values.yaml`

```yaml
ports:
  # ...
  websecure:
    # ...
    # 👇 Check this section at websecure entrypoint
    http:
      tls:
        enabled: true
        certResolver: letsencrypt

certificatesResolvers:
  letsencrypt:
    acme:
      tlsChallenge: false
      httpChallenge:
        entryPoint: web
      # 👇 Put admin email here
      email: <admin email>
      # Storage for certificates:
      storage: /certificates/acme.json
      # NOTE: Sometimes Let's Encrypt hit production SSL certificate issuing limits
      #       If you are having issues, switch to staging
      # Staging server
      caServer: https://acme-staging-v02.api.letsencrypt.org/directory
      # Production server
      # caServer: https://acme-v02.api.letsencrypt.org/directory

# Let's encrypt TLS resolver requires read/write volume
additionalVolumeMounts:
- mountPath: /certificates
  name: acme

deployment:
  hostNetwork: true
  # Attach volume to the traefik deployment
  additionalVolumes:
  - hostPath:
      path: /data/traefik
    name: acme
```

See full example at [examples/dev/traefik/values.yaml](https://github.com/opencrvs/infrastructure/blob/develop/examples/dev/traefik/values.yaml)

8. Commit and push changes
9. Run "Provision" workflow or deploy traefik manually

{% embed url="<https://doc.traefik.io/traefik/https/acme/#providers>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-https-challenge-in-development-environments.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
