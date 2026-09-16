---
title: "Patch: Elasticsearch 7.10.2"
source_url: "https://documentation.opencrvs.org/v1.6/general/releases/patch-elasticsearch-7.10.2"
markdown_url: "https://documentation.opencrvs.org/v1.6/general/releases/patch-elasticsearch-7.10.2.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:deb5c6b0a8521fa8144820ff03de8b46a9f8399206d6037d4faf5ebdb165d9eb"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/general/releases/patch-elasticsearch-7.10.2.md).

# Patch: Elasticsearch 7.10.2

An Elasticseach downgrade, patch to demonstrate OpenCRVS' base configuration supports OSI standard licenses.

**Patch Elasticsearch 7.10.2** is a core code patch for all implementers who may wish to adopt a commercial posture not supported by [Elasticsearch custom / non-OSI approved, opensource licence change](https://www.elastic.co/pricing/faq/licensing).  &#x20;

OpenCRVS usage of Elasticsearch does not enable the capability for anyone to provide paid-for, managed cloud search services.  We believe that the latest versions of Elasticsearch have no material effect on Civil Registration use cases and OpenCRVS' use of Elasticsearch. &#x20;

{% hint style="success" %}
This patch demonstrates that OpenCRVS works with an Apache 2.0 Elasticsearch license to conform to OSI standard OpenSource licenses.
{% endhint %}

### Changes in this patch:

Elasticsearch & Kibana have been fixed at version 7.10.2.&#x20;

{% hint style="warning" %}
**THIS PATCH IS TO BE APPLIED ON NEW INSTALLATIONS ONLY!**
{% endhint %}

{% hint style="danger" %}
**THIS PATCH DOES NOT SUPPORT APPLE MAC M1 CHIPS.**  &#x20;

**We use a later version of Elasticsearch in order to provide a better Apple Mac development experience.**
{% endhint %}

### Background:

The following explains the reason for this patch as interpreted by the OpenCRVS development team.  &#x20;

As far as we understand it, Elasticsearch appear to be in some disagreement with Amazon because Amazon started providing a paid for, managed cloud search "[Opensearch Service](https://aws.amazon.com/opensearch-service/)" (using a fork of Elasticsearch 7.10.2 - as was permitted by Elasticsearch's 7.10.2 Apache 2 license). Amazon renamed this fork [Opensearch](https://opensearch.org/) and released it on an OpenSource basis with a compliant Apache 2.0 license.

Elasticsearch then amended their OpenSource licence in order to stop 3rd parties from selling "managed" search services using Elasticsearch.  Our interpretation is that this seems to have been done because Elastic provide their own paid-for "managed" services.

As Elasticsearch now use a custom OpenSource license, any Elasticsearch release later than v7.10 has not been [OSI approved](https://opensource.org/licenses/).  Implementing countries may be concerned about that should they wish to adopt a managed search commercial posture, an un-common use case. In order to satisfy yourself that this software can be used commercially without any concerns over licensing, this patch can be applied.

To apply the patch, you will need to build and host your own opencrvs-core Docker images which you can build after cherry-picking this commit.

**External reading:**

We point all users to Elasticsearch and Amazon own content that discusses this issue:

Amazon: <https://aws.amazon.com/what-is/opensearch/>

Elastic: <https://www.elastic.co/what-is/opensearch> / <https://www.elastic.co/pricing/faq/licensing>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/general/releases/patch-elasticsearch-7.10.2.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
