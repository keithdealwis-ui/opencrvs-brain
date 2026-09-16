---
title: "Attachments"
source_url: "https://documentation.opencrvs.org/technical/apis/core-apis/attachments"
markdown_url: "https://documentation.opencrvs.org/technical/apis/core-apis/attachments.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:2bfdc1694c862df24f98f9e28d3d7bb561609168295dceb01f12ea0029b2ee1c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis/core-apis/attachments.md).

# Attachments

## POST /attachments

> Upload a file attachment

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"servers":[{"url":"http://localhost:3000/api/events"}],"security":[{"bearerAuth":["attachment.upload"]}],"components":{"securitySchemes":{}},"paths":{"/attachments":{"post":{"summary":"Upload a file attachment","tags":["Attachments"],"requestBody":{"required":true,"content":{"multipart/form-data":{"schema":{"type":"object","properties":{"path":{"type":"string","description":"Optional path in S3 where the file should be stored"},"transactionId":{"type":"string","description":"Transaction ID"},"file":{"type":"string","format":"binary","description":"File to upload"}},"required":["transactionId","file"]}}}},"responses":{"200":{"description":"File uploaded successfully. Requires authentication and attachment.upload scope.","content":{"application/json":{"schema":{"type":"object","properties":{"result":{"type":"object","properties":{"data":{"type":"object","properties":{"json":{"type":"string"}}}}}}}}}}}}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis/core-apis/attachments.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
