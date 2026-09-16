---
title: "Locations"
source_url: "https://documentation.opencrvs.org/technical/apis/core-apis/locations"
markdown_url: "https://documentation.opencrvs.org/technical/apis/core-apis/locations.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b3b2102d772812be40198e70282d8b2b9f9b905ea22faed92d37f8e4ad3c487e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis/core-apis/locations.md).

# Locations

## List locations

> Retrieve a list of locations based on provided filters.

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"servers":[{"url":"http://localhost:3000/api/events"}],"security":[{"Authorization":[]}],"components":{"securitySchemes":{"Authorization":{"type":"http","scheme":"bearer"}},"schemas":{"error.BAD_REQUEST":{"type":"object","properties":{"message":{"type":"string","description":"The error message"},"code":{"type":"string","description":"The error code"},"issues":{"description":"An array of issues that were responsible for the error","type":"array","items":{"type":"object","properties":{"message":{"type":"string"}},"required":["message"],"additionalProperties":false}}},"required":["message","code"],"additionalProperties":false,"title":"Invalid input data error (400)","description":"The error information"},"error.UNAUTHORIZED":{"type":"object","properties":{"message":{"type":"string","description":"The error message"},"code":{"type":"string","description":"The error code"},"issues":{"description":"An array of issues that were responsible for the error","type":"array","items":{"type":"object","properties":{"message":{"type":"string"}},"required":["message"],"additionalProperties":false}}},"required":["message","code"],"additionalProperties":false,"title":"Authorization not provided error (401)","description":"The error information"},"error.FORBIDDEN":{"type":"object","properties":{"message":{"type":"string","description":"The error message"},"code":{"type":"string","description":"The error code"},"issues":{"description":"An array of issues that were responsible for the error","type":"array","items":{"type":"object","properties":{"message":{"type":"string"}},"required":["message"],"additionalProperties":false}}},"required":["message","code"],"additionalProperties":false,"title":"Insufficient access error (403)","description":"The error information"},"error.NOT_FOUND":{"type":"object","properties":{"message":{"type":"string","description":"The error message"},"code":{"type":"string","description":"The error code"},"issues":{"description":"An array of issues that were responsible for the error","type":"array","items":{"type":"object","properties":{"message":{"type":"string"}},"required":["message"],"additionalProperties":false}}},"required":["message","code"],"additionalProperties":false,"title":"Not found error (404)","description":"The error information"},"error.INTERNAL_SERVER_ERROR":{"type":"object","properties":{"message":{"type":"string","description":"The error message"},"code":{"type":"string","description":"The error code"},"issues":{"description":"An array of issues that were responsible for the error","type":"array","items":{"type":"object","properties":{"message":{"type":"string"}},"required":["message"],"additionalProperties":false}}},"required":["message","code"],"additionalProperties":false,"title":"Internal server error error (500)","description":"The error information"}}},"paths":{"/locations":{"get":{"operationId":"locations-list","summary":"List locations","description":"Retrieve a list of locations based on provided filters.","tags":["Locations"],"parameters":[{"in":"query","name":"isActive","schema":{"type":"boolean"}},{"in":"query","name":"locationIds","schema":{"type":"array","items":{"type":"string","format":"uuid","pattern":"^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"}}},{"in":"query","name":"locationType","schema":{"type":"string"}},{"in":"query","name":"externalId","schema":{"type":"string"}}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"array","items":{"type":"object","properties":{"id":{"type":"string","format":"uuid","pattern":"^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"},"name":{"type":"string"},"externalId":{"anyOf":[{"type":"string"},{"type":"null"}]},"administrativeAreaId":{"anyOf":[{"type":"string","format":"uuid","pattern":"^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"},{"type":"null"}]},"validUntil":{"anyOf":[{"type":"string","format":"date-time","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))T(?:(?:[01]\\d|2[0-3]):[0-5]\\d(?::[0-5]\\d(?:\\.\\d+)?)?(?:Z))$"},{"type":"null"}]},"locationType":{"anyOf":[{"type":"string"},{"type":"null"}]}},"required":["id","name","administrativeAreaId","validUntil","locationType"],"additionalProperties":false}}}}},"400":{"description":"Invalid input data","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error.BAD_REQUEST"}}}},"401":{"description":"Authorization not provided","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error.UNAUTHORIZED"}}}},"403":{"description":"Insufficient access","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error.FORBIDDEN"}}}},"404":{"description":"Not found","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error.NOT_FOUND"}}}},"500":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error.INTERNAL_SERVER_ERROR"}}}}}}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis/core-apis/locations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
