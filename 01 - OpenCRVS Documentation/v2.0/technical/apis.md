---
title: "APIs"
source_url: "https://documentation.opencrvs.org/technical/apis"
markdown_url: "https://documentation.opencrvs.org/technical/apis.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e8b385d62ffedd39e980ddeff69f1aca927cbb1b8a4df6a6d79737dfc9dbef45"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis.md).

# APIs

- [Core APIs](https://documentation.opencrvs.org/technical/apis/core-apis.md): Core OpenAPI spec
- [Events](https://documentation.opencrvs.org/technical/apis/core-apis/events.md)
- [Search](https://documentation.opencrvs.org/technical/apis/core-apis/search.md)
- [Locations](https://documentation.opencrvs.org/technical/apis/core-apis/locations.md)
- [Integrations](https://documentation.opencrvs.org/technical/apis/core-apis/integrations.md)
- [Attachments](https://documentation.opencrvs.org/technical/apis/core-apis/attachments.md)
- [Models](https://documentation.opencrvs.org/technical/apis/core-apis/models.md)
- [Country-config APIs](https://documentation.opencrvs.org/technical/apis/country-config-apis.md): Country-config OpenAPI spec
- [Events](https://documentation.opencrvs.org/technical/apis/country-config-apis/events.md)
- [Models](https://documentation.opencrvs.org/technical/apis/country-config-apis/models.md)
- [Toolkit](https://documentation.opencrvs.org/technical/apis/toolkit.md)
- [Configuration](https://documentation.opencrvs.org/technical/apis/toolkit/configuration.md)
- [Advanced search](https://documentation.opencrvs.org/technical/apis/toolkit/configuration/advanced-search.md)
- [Conditionals](https://documentation.opencrvs.org/technical/apis/toolkit/conditionals.md): All conditional builders return a JSONSchema object. Combine them with and, or, and not. Use them in field or action conditionals arrays.
- [Deduplication](https://documentation.opencrvs.org/technical/apis/toolkit/deduplication.md)
- [API Client](https://documentation.opencrvs.org/technical/apis/toolkit/api-client.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
