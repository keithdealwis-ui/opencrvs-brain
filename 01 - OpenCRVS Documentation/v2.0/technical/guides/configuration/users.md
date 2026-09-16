---
title: "Users"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/users"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/users.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:80f7474a9464039981ff073a3447d976bd4b00876062a815ca8026012abf49b5"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/users.md).

# Users

OpenCRVS has two types of users. System users (`type: 'system'`), which operate using API's, and human users (`type: 'user'`), which use the client. When referring to a user, we mean the latter.

[Users are seeded as part of the administrative hierarchy](/technical/guides/configuration/administrative-hierarchy/how-to-populate-administrative-hierarchy.md). Each user has a location and a role. The location's position in the administrative hierarchy determines the jurisdiction the scope grants.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
