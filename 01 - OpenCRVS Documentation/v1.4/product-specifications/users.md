---
title: "Users"
source_url: "https://documentation.opencrvs.org/v1.4/product-specifications/users"
markdown_url: "https://documentation.opencrvs.org/v1.4/product-specifications/users.md"
version: "v1.4"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:7f41ab30056c1a1dde67184b5db24f66382fb67a8c7e8af3835114dc169a1802"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.4/product-specifications/users.md).

# Users

The different user roles in the system, and defined below, reflect common actors involved in civil registration services around the world as well as non-traditional actors that may help improve service delivery e.g. field agents who can take services to the community.

{% hint style="info" %}
**System Roles and User types**\
\
OpenCRVS has set roles with defined responsibilities in the system. You can create different user types based on your requirements and map them to these system roles. \
\
For example in Farajaland there are two different Field Agents: Hostpital Clerk and Community Leader. They are different user roles but all have the same responsibilities in the system.
{% endhint %}

* To see how these roles are mapped to user types in Farajaland, see [User / role mapping](/v1.4/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md).
* To see how these actors work together to improve service delivery in Farajaland, see [Business process flows in Farajaland](/v1.4/default-configuration/business-process-flows-in-farajaland.md).

<table><thead><tr><th width="228.08182370999793">System roles</th><th>Responsibilities</th><th>Farajaland user roles</th></tr></thead><tbody><tr><td>Field Agent</td><td><ul><li>Create vital event notifications / declarations</li></ul></td><td><p>Hospital Clerk</p><p>Community Leader</p></td></tr><tr><td>Registration Agent</td><td><ul><li>Create vital event declarations</li><li>Validate and send declarations for approval</li><li>Issue certificates</li><li>Search for records</li><li>View performance statistics</li></ul></td><td>Registration Officer</td></tr><tr><td>Registrar</td><td><ul><li>Create vital event declarations</li><li>Approve and register declarations</li><li>Issue certificates</li><li>Search for records</li><li>View performance statistics (default local)</li></ul></td><td>Registrar<br>Provincial Registrar</td></tr><tr><td>National Registrar</td><td><ul><li>Create vital event declarations</li><li>Approve and register declarations</li><li>Issue certificates</li><li>Search for records</li><li>View performance statistics (default Nationally)</li></ul></td><td>Registrar General</td></tr><tr><td>Local System Admin</td><td><ul><li>Create users</li><li>Edit users</li></ul></td><td>Administrator</td></tr><tr><td>National System Admin</td><td><ul><li>Config management</li><li>Create users</li><li>Edit users</li></ul></td><td>National Administrator</td></tr><tr><td>Performance Manager</td><td><ul><li>View performance statistics (default local)</li></ul></td><td>Operations Manager</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.4/product-specifications/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
