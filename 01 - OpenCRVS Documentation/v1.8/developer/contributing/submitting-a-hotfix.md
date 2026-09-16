---
title: "Submitting a hotfix"
source_url: "https://documentation.opencrvs.org/v1.8/developer/contributing/submitting-a-hotfix"
markdown_url: "https://documentation.opencrvs.org/v1.8/developer/contributing/submitting-a-hotfix.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f64d9e2471b17c65f84acf475004877ad6013f140eea9c1a589aa9f0531c32b3"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/developer/contributing/submitting-a-hotfix.md).

# Submitting a hotfix

Found a bug from OpenCRVS? Please refer to our documentation first on [Contributing to OpenCRVS.](https://documentation.opencrvs.org/general/contributing#reporting-new-issues)

At any given time, OpenCRVS Core team has two minor versions in ongoing support:

* The latest minor version (e.g. 1.8.x)
* The previous support version (e.g. 1.7.x)

In most cases, all bugs found from OpenCRVS are fixed in both of these versions and only after that merged into the `develop` branch. For this reason it's critical, that a specific process is followed when contributing bug fixes to OpenCRVS.

Thew following diagram describes this process in detail:

{% embed url="<https://www.figma.com/board/paOtCyh4uoL99pWgjt8dxB/Git-hotfixing-process?node-id=0-1&t=hs3s8OqwHdtPJmTR-1>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/developer/contributing/submitting-a-hotfix.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
