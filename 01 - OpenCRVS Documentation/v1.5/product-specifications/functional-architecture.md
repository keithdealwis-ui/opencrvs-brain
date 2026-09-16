---
title: "Functional Architecture"
source_url: "https://documentation.opencrvs.org/v1.5/product-specifications/functional-architecture"
markdown_url: "https://documentation.opencrvs.org/v1.5/product-specifications/functional-architecture.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:5fb9b396065b6972520409a3e707932f71c48ee66f9365fb17fbf6041f24c34a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/product-specifications/functional-architecture.md).

# Functional Architecture

The OpenCRVS functional architecture shows the logical components of which the system is comprised. Each of these "functions" is explained in greater detail within the relevant section of the documentation.

{% hint style="info" %}
**OpenCRVS Specifications 1.4**\
For a comprehensive understanding of the features of OpenCRVS, please refer to the complete product specification, which can be found in the [OpenCRVS Specifications v1.4](https://docs.google.com/spreadsheets/d/1Jf31WkNMqlfQOYpjpfG73M5utVGrx4zqA5eiODaftNI/edit?usp=sharing) excel document
{% endhint %}

<figure><img src="https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/eh0UFy9qBKrTeXSSqn8Z/Functional%20architecture2.png" alt=""><figcaption></figcaption></figure>

#### Key:

* Blue (built)
* White (coming soon)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/product-specifications/functional-architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
