---
title: "Functional Architecture"
source_url: "https://documentation.opencrvs.org/v1.7/product-specifications/functional-architecture"
markdown_url: "https://documentation.opencrvs.org/v1.7/product-specifications/functional-architecture.md"
version: "v1.7"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ea007f0089d50d4e35dd24fd06189b5fc902c3b00f21db067fd41804e1e22928"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.7/product-specifications/functional-architecture.md).

# Functional Architecture

The OpenCRVS functional architecture shows the logical components of which the system is comprised. Each of these "functions" is explained in greater detail within the relevant section of the documentation.

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/lh3l4TjY0kklVfOUTXn7/Functional%20architecture2.png" alt=""><figcaption></figcaption></figure>

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
GET https://documentation.opencrvs.org/v1.7/product-specifications/functional-architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
