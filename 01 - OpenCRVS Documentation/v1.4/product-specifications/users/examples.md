---
title: "Examples"
source_url: "https://documentation.opencrvs.org/v1.4/product-specifications/users/examples"
markdown_url: "https://documentation.opencrvs.org/v1.4/product-specifications/users/examples.md"
version: "v1.4"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:044e5309197622ab6a1a5f2aec2123cf16622219678fc93f0926f1edd5e53d83"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.4/product-specifications/users/examples.md).

# Examples

![Field Agent: Sammi is a Community Health Assistant in Bangladesh. She is responsible for providing maternal and child health care and vaccination services in her community. She is comfortable using the tablet because she already had a smartphone and loves using OpenCRVS in the community: "By offering this service at their homes, this will make so many people's lives easier."](https://content.gitbook.com/content/CCxReqNLi05GgVKnwb07/blobs/94oi6GxEOQHEobBn2HfV/ha_bang.png)

![Field Agent: Maneya Mwansakilwa is a Nurse in Kanyama hospital in Lusaka, Zambia. She provides maternal and child health services in the hospital and in the community. She tells us that a large number of births occur in the community and these mothers often do not visit the hospital for services for their babies, they wait for community visits, "...and so if this process can be brought nearer to the people, it will do a lot of good to them".](https://content.gitbook.com/content/CCxReqNLi05GgVKnwb07/blobs/YfItlufHIsX20agrtBEQ/ha_zambia.jpeg)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.4/product-specifications/users/examples.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
