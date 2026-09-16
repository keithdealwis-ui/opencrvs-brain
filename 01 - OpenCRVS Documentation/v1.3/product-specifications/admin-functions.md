---
title: "Admin functions"
source_url: "https://documentation.opencrvs.org/v1.3/product-specifications/admin-functions"
markdown_url: "https://documentation.opencrvs.org/v1.3/product-specifications/admin-functions.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:7b7300d4407cd5b02a2451aa2a34ac5267709ecb6cca8d0a888453b7005b6f8e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/product-specifications/admin-functions.md).

# Admin functions

Overview of functionality for a system administrator to effectively manage and maintain the OpenCRVS product.

{% hint style="info" %}
**OpenCRVS Specifications 1.3**\
For a comprehensive understanding of the features of OpenCRVS, please refer to the complete product specification, which can be found in the [OpenCRVS Specifications v1.3](https://docs.google.com/spreadsheets/d/1ZKYmYTj9qd9vG1jbcNVXFw0GeZGL0xk5pD8c8UaxsZ0/edit?usp=sharing) excel document
{% endhint %}

<table><thead><tr><th>Function</th><th width="419.6666666666667">Description</th></tr></thead><tbody><tr><td><a href="/v1.3/product-specifications/admin-functions/17.-user-management.md">User management</a></td><td>Manage users, including creating new users and deactivating users</td></tr><tr><td><a href="/v1.3/product-specifications/admin-functions/18.-comms-management.md">Comms management</a></td><td>Manage communications that are sent to both customers and system users</td></tr><tr><td><a href="/v1.3/product-specifications/admin-functions/19.-content-management.md">Content management</a></td><td>Manage product content (copy), including language translation</td></tr><tr><td><a href="/v1.3/product-specifications/admin-functions/20.-config-management.md">Config management</a></td><td>Configure the product to reflect country needs</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/product-specifications/admin-functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
