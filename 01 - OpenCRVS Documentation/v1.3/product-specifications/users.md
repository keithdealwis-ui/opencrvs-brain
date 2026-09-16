---
title: "Users"
source_url: "https://documentation.opencrvs.org/v1.3/product-specifications/users"
markdown_url: "https://documentation.opencrvs.org/v1.3/product-specifications/users.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:d46057c4c5fce1bb0fa4285f439e6a88621c737bc12854a4592b9de0ec17328a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/product-specifications/users.md).

# Users

The different user roles in the system, and defined below, reflect common actors involved in civil registration services around the world as well as non-traditional actors that may help improve service delivery e.g. field agents who can take services to the community.

{% hint style="info" %}
**System Roles and User types**\
\
OpenCRVS has set roles with defined responsibilities in the system. You can create different user types based on your requirements and map them to these system roles. \
\
For example in Farajaland there are four different Field Agents user: Healthcare Worker, Police Office, Local Leader, Social Worker. They are different users but all have the same responsibilities in the system.
{% endhint %}

* The user types for Farajaland have been included as an example of how you can map different users with the same responsibilities to the system role.
* To see how these actors work together to improve service delivery in Farajaland, see [Business process flows in Farajaland](/v1.3/default-configuration/business-process-flows-in-farajaland.md).

<table><thead><tr><th width="228.08182370999793">System roles</th><th>Responsibilities</th><th>Farajaland user type/s</th></tr></thead><tbody><tr><td>Field agent</td><td><ul><li>Create birth and death notifications</li></ul></td><td>Healthcare Worker<br>Police Office<br>Local Leader<br>Social Worker</td></tr><tr><td>Registration agent</td><td><ul><li>Create birth and death declarations</li><li>Validate and send declarations for approval</li><li>Issue certificates</li><li>View performance statistics</li></ul></td><td>Registration office</td></tr><tr><td>Registrar</td><td><ul><li>Create birth and death declarations</li><li>Approve and register declarations</li><li>Issue certificates</li><li>View performance statistics</li></ul></td><td>Registrar</td></tr><tr><td>National Registrar</td><td><ul><li>Create birth and death declarations</li><li>Approve and register declarations</li><li>Issue certificates</li><li>View performance statistics</li></ul></td><td>Registrar General</td></tr><tr><td>Local System Admin</td><td><ul><li>Create users</li><li>Edit users</li></ul></td><td>Local System Admin</td></tr><tr><td>National System Admin</td><td><ul><li>Config management</li><li>Create users</li><li>Edit users</li></ul></td><td>National System Admin</td></tr><tr><td>Performance Manager</td><td><ul><li>View performance statistics</li></ul></td><td>Performance Manager</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/product-specifications/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
