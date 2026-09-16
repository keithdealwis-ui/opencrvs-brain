---
title: "Configure DNS"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/configure-dns"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/configure-dns.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b0652bcc2e8c061c491fc4d2abf67a606338f86733133954e764147072f6926e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/configure-dns.md).

# Configure DNS

#### Setup Domain A records

Using your domain management system, A records will need to be created for all the services which are publicly exposed for **qa, production & staging** environments.

Either use a wildcard or create individual A records for your chosen environment's domain name, with a TTL of 1 hour that forwards the URL to your **manager server node's** external IP address.

**Option 1: Wildcard required A Records:**

{% hint style="info" %}
A total of 6 A Records are required for this option, 2 for each environment's domain: **qa, production & staging**
{% endhint %}

*\<your\_domain>*

*\*.\<your\_domain>*

**Option 2: Individual A Records:**

{% hint style="info" %}
A total of 27 A Records are required for this option, 9 for each environment's domain: **qa, production & staging**
{% endhint %}

*\<your\_domain>*

*countryconfig.\<your\_domain>*

*metabase.\<your\_domain>*

*minio.\<your\_domain>*

*minio-console.\<your\_domain>*

*gateway.\<your\_domain>*

*kibana.\<your\_domain>*

*login.\<your\_domain>*

*register.\<your\_domain>*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/preparation-steps/configure-dns.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
