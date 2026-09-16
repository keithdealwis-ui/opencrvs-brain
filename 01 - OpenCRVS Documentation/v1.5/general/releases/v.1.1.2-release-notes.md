---
title: "v.1.1.2: Release notes"
source_url: "https://documentation.opencrvs.org/v1.5/general/releases/v.1.1.2-release-notes"
markdown_url: "https://documentation.opencrvs.org/v1.5/general/releases/v.1.1.2-release-notes.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:704cc8d9724767c3a1dd64e2182ace21eca410e3373b3c4e69199beb52dc25c9"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/general/releases/v.1.1.2-release-notes.md).

# v.1.1.2: Release notes

**OpenCRVS v1.1.2** is a minor release that contains minor and non-breaking hotfixes for the **OpenCRVS v1.1.1** release. It is to be used in conjunction with a forked country configuration release [v1.1.2](https://github.com/opencrvs/opencrvs-farajaland/releases/tag/v1.1.2)

### Non breaking hotfix

* ocrvs-4210 Ansible amend to ensure that data folders do not get cleared when the script is run during a migration @euanmillar in <https://github.com/opencrvs/opencrvs-core/pull/4210>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/general/releases/v.1.1.2-release-notes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
