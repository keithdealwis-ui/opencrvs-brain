---
title: "User roles"
source_url: "https://documentation.opencrvs.org/v1.8/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping"
markdown_url: "https://documentation.opencrvs.org/v1.8/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:1cb2557da7420cfc74edd3dfdfa285487f53489e5f8856aa691bea8c839cd7bb"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md).

# User roles

This section describes the user roles identified in Farajaland, along with the scopes assigned to each role to support essential business processes and achieve our CRVS goals

### User roles and responsibilities

Outlined below are the user roles identified in Farajaland and they key CRVS responsibilities

<table><thead><tr><th width="294">User role</th><th width="460">Key Responsibilities</th></tr></thead><tbody><tr><td>Hospital Clerk</td><td><ul><li>Submit vital event notifications / declarations from health institutions</li></ul></td></tr><tr><td>Community Leader</td><td><ul><li>Submit vital event notifications / declarations in the community</li></ul></td></tr><tr><td>Registration Officer</td><td><ul><li>Create vital event declarations</li><li>Validate and send declarations for approval</li><li>Print and issue certificates</li><li>Search for records</li><li>View performance statistics</li></ul></td></tr><tr><td>Local Registrar</td><td><ul><li>Create vital event declarations</li><li>Approve and register declarations</li><li>Issue certificates</li><li>Search for records</li><li>View performance statistics (default local)</li></ul></td></tr><tr><td>Registrar General</td><td><ul><li>View performance statistics (default Nationally)</li></ul></td></tr><tr><td>Administrator</td><td><ul><li>Create users (in their jurisdiction)</li><li>Edit users (in their jurisdiction)</li></ul></td></tr><tr><td>National Administrator</td><td><ul><li>Config management</li><li>Create users (nationally)</li><li>Edit users (nationally)</li></ul></td></tr><tr><td>Operations Manager</td><td><ul><li>View performance statistics (default local)</li></ul></td></tr></tbody></table>

### Scopes assigned to each user role

In the **Country Configuration Files** in the [Release Notes](https://github.com/opencrvs/documentation/blob/master/v1.8.0/general/v1.8-release-notes) you will see how we mapped and assigned permissions (scopes) to Farajaland user roles.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
