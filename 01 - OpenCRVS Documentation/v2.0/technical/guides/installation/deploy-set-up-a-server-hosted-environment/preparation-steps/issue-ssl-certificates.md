---
title: "Issue SSL Certificates"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/issue-ssl-certificates"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/issue-ssl-certificates.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:7035a275e46b4a87ed47fb23d325a1815a088b473cdf4debac4dc4ed52b7a53e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/issue-ssl-certificates.md).

# Issue SSL Certificates

There are a number of ways you can configure TLS / SSL certificates for OpenCRVS. The options are explained in detail in the [Advance topics > TLS/SSL Configuration for traefik](/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik.md) section. All methods must be compatible with [Traefik](https://doc.traefik.io/traefik/https/overview/).

At a high-level, here is a brief intro to the subject.

**Free LetsEncrypt certificates**

A free approach is to use LetsEncrypt. However LetsEncrypt certificates must validate and refresh every 3 months.

{% hint style="info" %}
The OpenCRVS installation script will automatically configure Traefik to obtain and use dynamic Let's Encrypt SSL certificates for you that automatically refresh.

**This automated option is available for testing and demonstration purposes, and not for production environments.**

The server must be accessible from the public internet for this automated process to work. Therefore, as the server is not behind a VPN, the approach isnt suitable in production.
{% endhint %}

When installing OpenCRVS behind a VPN, **required for production and staging environments**, it's technically possible to create and refresh static LetsEncrypt certs every 3 months, with different approaches for certifcate validation via your DNS server.

For more information see official documentation <https://letsencrypt.org/docs/challenge-types/>

**Purchasing long term certificates**

Most government networks require you to purchase or use a long term SSL certificate per environment, and manually replacing the static .crt & .key files every 1, 2 or 3 years depending on it's lifetime.

Some governments have their own public key infrastructure to issue these static certs.

The SSL certificates that you obtain must support the [DNS](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/configure-dns.md) subdomains for each environment's individual domain: **qa, production & staging.**

You may opt for a single, wildcard SSL certificate for each domain.

**Technical guide**

For detailed technical guidance on how to configure the various options in helm charts read [Advance topics > TLS/SSL Configuration for traefik](/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/issue-ssl-certificates.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
