---
title: "Understanding CRVS"
source_url: "https://documentation.opencrvs.org/v1.6/crvs-systems/understanding-crvs"
markdown_url: "https://documentation.opencrvs.org/v1.6/crvs-systems/understanding-crvs.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:9eea56a36a5d9f09f2582179cd6919b98efd545e5a7ec334e7d6ab6fe1467060"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/crvs-systems/understanding-crvs.md).

# Understanding CRVS

Provides useful links to documentation about CRVS

Before considering to build a CRVS system using OpenCRVS it is important to understand the business domain. There is a lot of helpful material that explains what CRVS is and how it should work and this section highlights a number of useful references. Take the time to review the domain specific material below before proceeding with an implementation of OpenCRVS.&#x20;

| CRVS Reference                                                                                          | Description                                                                                                                                                                  | Link                                                                                                       |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| (UN) Handbook on Civil Registration and Vital Statistics Systems: Management, Operation and Maintenance | An exhaustive reference of administrative arrangements, operational functions, quality, interoperability and digitisation of civil registration and vital statistics systems | <https://unstats.un.org/unsd/demographic-social/Standards-and-Methods/files/Handbooks/crvs/crvs-mgt-E.pdf> |
| The Civil Registration and Vital Statistics Digitisation Guidebook (CRVS-DGB)                           | An online resource that provides step-by-step guidance for countries to plan, analyse, design and implement digitized systems and automated processes for CRVS               | <http://www.crvs-dgb.org/en/>                                                                              |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/crvs-systems/understanding-crvs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
