---
title: "v.1.1.1: Release notes"
source_url: "https://documentation.opencrvs.org/v1.6/general/releases/v.1.1.1-release-notes"
markdown_url: "https://documentation.opencrvs.org/v1.6/general/releases/v.1.1.1-release-notes.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e03cc0d13cfd34b91daa4a360e2e507c0f5875f48c36e44739d3a5ee52f5ae68"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/general/releases/v.1.1.1-release-notes.md).

# v.1.1.1: Release notes

**OpenCRVS v1.1.1** is a minor release that contains minor and non-breaking hotfixes for the **OpenCRVS v1.1.0-stable** release. It is to be used in conjunction with a forked country configuration release [v1.1.1](https://github.com/opencrvs/opencrvs-farajaland/releases/tag/v1.1.1)

### Non breaking hotfixes

**Core**

* ocrvs-3707 Disabled add attachments when father and mother has no details by [@Zangetsu101](https://github.com/Zangetsu101) in [#4017](https://github.com/opencrvs/opencrvs-core/pull/4017)
* ocrvs-3859-fix Download certificate pdf in mobile device while printing by [@sadmananik](https://github.com/sadmananik) in [#4013](https://github.com/opencrvs/opencrvs-core/pull/4013)
* ocrvs-3985 Fixed default configurable field required issue by [@sadmananik](https://github.com/sadmananik) in [#4030](https://github.com/opencrvs/opencrvs-core/pull/4030)

**Country configuration**

* Removed the deprecated --update-metadata flag from the deploy.yml by [@euanmillar](https://github.com/euanmillar) in [#359](https://github.com/opencrvs/opencrvs-farajaland/pull/359)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/general/releases/v.1.1.1-release-notes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
