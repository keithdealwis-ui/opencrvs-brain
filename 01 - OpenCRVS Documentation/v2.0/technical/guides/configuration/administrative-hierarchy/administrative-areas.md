---
title: "Administrative areas"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/administrative-areas"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/administrative-areas.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:992f7ca8ae61556b68ad757486a83094b4a295d25c9538c84c9346fbbfd8fac5"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/administrative-areas.md).

# Administrative areas

Administrative areas divide a country into hierarchical jurisdictions. Areas are dynamic and configurable per country. See how administrative area configuration affects [Roles, scopes and jurisidictions](/technical/guides/configuration/users/roles-and-scopes.md).

**Example 1: Simple hierarchy**

![](https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-8d5a9f075b5a53a23ba9364b7ea3dde7d896c8c8%2FScreenshot%202026-05-06%20at%2013.54.21.png?alt=media)

In this example, a country has one province, one district, and one village.

**Example 2: Uneven hierarchy**

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-6608b4473c7fe8bd7caef39c6d3ce31b91fe6cb5%2FScreenshot%202026-05-06%20at%2014.01.01.png?alt=media" alt="" width="188"><figcaption></figcaption></figure>

\
In this example, a country has an uneven hierarchy. Jurisdiction branches start from Province A, Province B, and District C. Branches are independent and do not need to include every level — a district does not always need to be preceded by a province or followed by a village.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/administrative-areas.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
