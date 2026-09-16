---
title: "Functional Architecture"
source_url: "https://documentation.opencrvs.org/v1.8/product-specifications/functional-architecture"
markdown_url: "https://documentation.opencrvs.org/v1.8/product-specifications/functional-architecture.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3dfc2e5f383fec3ae79e3f0b4b2e31e809488a5af5f9c0c91e196aaff7f0de80"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/product-specifications/functional-architecture.md).

# Functional Architecture

The OpenCRVS functional architecture shows the logical components of which the system is comprised. Each of these "functions" is explained in greater detail within the relevant section of the documentation.

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-f93dc928336333fd9b4a7c8af2974c358ff5faf2%2FFunctional%20architecture2.png?alt=media" alt=""><figcaption></figcaption></figure>

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
GET https://documentation.opencrvs.org/v1.8/product-specifications/functional-architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
