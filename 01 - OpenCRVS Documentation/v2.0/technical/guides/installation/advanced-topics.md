---
title: "Advanced topics"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b8f311d6b134fe2b05dd04f3845f7705b7860e251e505c1186d8c6e9af58a435"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics.md).

# Advanced topics

- [Ubuntu Firewall configuration](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-firewall-configuration.md)
- [Ubuntu unattended-upgrades](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-unattended-upgrades.md)
- [TLS/SSL Configuration for traefik](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik.md)
- [LetsEncrypt https challenge in development environments](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-https-challenge-in-development-environments.md)
- [LetsEncrypt DNS challenge in production](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/letsencrypt-dns-challenge-in-production.md)
- [Static TLS certificates](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates.md)
- [SSH access](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ssh-access.md)
- [Kubernetes cluster access](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/kubernetes-cluster-access.md)
- [Add Custom GitHub secrets to Kubernetes](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/add-custom-github-secrets-to-kubernetes.md)
- [Disk space management](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-space-management.md)
- [Elasticsearch disk management](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/elasticsearch-disk-management.md)
- [Disk encryption](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-encryption.md)
- [Why VPN?](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/why-vpn.md)
- [Deploy OpenCRVS with external data stores](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/deploy-opencrvs-with-external-data-stores.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
