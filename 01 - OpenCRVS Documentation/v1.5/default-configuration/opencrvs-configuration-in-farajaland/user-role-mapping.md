---
title: "User / role mapping"
source_url: "https://documentation.opencrvs.org/v1.5/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping"
markdown_url: "https://documentation.opencrvs.org/v1.5/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:41402cf33e3479e60ac24f661778a3cfa61de73dc1f3b4a708ffb4bc9197e7b4"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md).

# User / role mapping

The Farajaland users have been mapped to the OpenCRVS systems roles accordingly in order to support the business process flows

<table><thead><tr><th>System Role</th><th>Farajaland User</th><th data-hidden>OpenCRVS Role</th><th data-hidden>Notes</th></tr></thead><tbody><tr><td>Field Agent</td><td>Hospital Clerk <br>Community Leader</td><td>Field Agent</td><td>A number of these users are added to each District Office in Farajaland (type: Community Leader)</td></tr><tr><td>Registration Agent</td><td>Registration Officer</td><td>Registration Agent</td><td>A number of these users are added to each District Office in Farajaland</td></tr><tr><td>Registrar</td><td>Registrar<br>Privisional Registrar</td><td>Registrar</td><td>This user is added to each District Office in Farajaland</td></tr><tr><td>National Registrar</td><td>Registrar General</td><td>National Registrar</td><td>This user is added to the HQ Office in Isamba District</td></tr><tr><td>Local System Admin</td><td>Administrator</td><td>Local System Admin</td><td>This user is added to each District Office in Farajaland</td></tr><tr><td>National System Admin</td><td>National Administrator</td><td>National System Admin</td><td>This user is added to the HQ Office in Isamba District</td></tr><tr><td>Performance Manager</td><td>Operations Manager</td><td>Performance Manager</td><td>This user is added to the HQ Office in Isamba District</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
