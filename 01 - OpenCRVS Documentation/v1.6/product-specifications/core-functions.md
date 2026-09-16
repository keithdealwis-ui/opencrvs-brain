---
title: "Core functions"
source_url: "https://documentation.opencrvs.org/v1.6/product-specifications/core-functions"
markdown_url: "https://documentation.opencrvs.org/v1.6/product-specifications/core-functions.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:302640db8a416f5e13ffdae44b5be0163b1d3ec667f0f7c2cffb27bf4d4e9fc5"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/product-specifications/core-functions.md).

# Core functions

Overview of core functions

{% hint style="info" %}
**OpenCRVS Specifications 1.4**\
For a comprehensive understanding of the features of OpenCRVS, please refer to the complete product specification, which can be found in the [OpenCRVS Specifications v1.4](https://docs.google.com/spreadsheets/d/1Jf31WkNMqlfQOYpjpfG73M5utVGrx4zqA5eiODaftNI/edit?usp=sharing) excel document
{% endhint %}

<table><thead><tr><th width="246">Function</th><th width="431.3333333333333">Description</th></tr></thead><tbody><tr><td><a href="/v1.6/product-specifications/core-functions/1.-notify-event.md">Notify event</a></td><td>User or external system sends a vital event notification to an assigned office. The notification appears in the 'In Progress' workqueue for follow-up and completion.</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/2.-declare-event.md">Declare even</a>t</td><td>User completes declaration form in an office or roaming (mobile) and either sends for review or registers it</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/3.-validate-event.md">Validate event</a></td><td>User reviews submitted declaration form against supporting documents</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/4.-register-event.md">Register event</a></td><td>User registers vital event</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/5.-print-certificate.md">Print certificate</a></td><td>User prints certificate</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/5.-issue-certificate.md">Issue certificate</a></td><td>User issues a certificate</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/6.-search-for-a-record.md">Search for a record</a></td><td>User searches and retrieves a vital event record</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/7.-view-record.md">View record</a></td><td>User views a record</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/8.-correct-record.md">Correct record</a></td><td>User corrects a record, providing a reason for the correction</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/9.-verify-record.md">Verify record</a></td><td>User is able to verify the existence of a birth record and see relevant details</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/10.-archive-record.md">Archive record</a></td><td>User archives a record</td></tr><tr><td><a href="/v1.6/product-specifications/core-functions/11.-vital-statistics-export.md">Vital statistics export</a></td><td>User is able to view vital statistics data and download in required format</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/product-specifications/core-functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
