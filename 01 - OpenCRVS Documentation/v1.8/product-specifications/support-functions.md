---
title: "Support functions"
source_url: "https://documentation.opencrvs.org/v1.8/product-specifications/support-functions"
markdown_url: "https://documentation.opencrvs.org/v1.8/product-specifications/support-functions.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8d885d30177eddde98a7974a55abba50e5535a9f5ceab10dba1576530b17cd22"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/product-specifications/support-functions.md).

# Support functions

Overview of functionality that enables users to conduct civil registration services safely, securely, and most effectively.

<table><thead><tr><th>Function</th><th width="423.6666666666667">Description</th></tr></thead><tbody><tr><td><a href="/v1.8/product-specifications/support-functions/10.-login.md">Login</a></td><td>User logs in to use the system</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/11.-audit.md">Audit</a></td><td>User searches for and views audit logs for a record</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/12.-deduplication.md">De-duplication</a></td><td>User reviews possible duplicate records identified by the system and takes action</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/13.-performance-management.md">Performance management</a></td><td>User views a suite of performance and operational level data in a dashboard</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/14.-payment.md">Payment</a></td><td>Customer makes payment for civil registration services through a range of payment modalities, including mobile money</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/15.-learning.md">Learning</a></td><td>User learns about the product and how to use it through interactive learning modules</td></tr><tr><td><a href="/v1.8/product-specifications/support-functions/16.-user-support.md">User support</a></td><td>User raises product and/or service issues for the attention and resolution of support staff</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/product-specifications/support-functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
