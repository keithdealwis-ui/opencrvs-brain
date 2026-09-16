---
title: "Registration integration"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration-1"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration-1.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c0ce0b14edeb58ab048044bfe88f5290862832ce4042e39a4018a2cb1709683f"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration-1.md).

# Registration integration

{% hint style="info" %}
This section assumes that you have already read the general [National ID registration integration page](/v1.9/technology/interoperability/national-id.md) and are familiar with those concepts. If you have not read that page, read it first for a high level introduction to the concepts, and then return here.
{% endhint %}

Our example shows integration with the [mosip-api](https://github.com/opencrvs/mosip/tree/main/packages/mosip-api) middleware at this point.

We perform [some business logic](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L195) based on props in the `declaration` and `pendingAction` and continue to MOSIP or reject.

Then we create a `createMosipInteropClient` [client](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L215) to register a [birth](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L221) or [death](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L297).

Asynchronous return of a MOSIP credential being issued is performed via websub. The OpenCRVS JWT is retrieved from SQLite and [registered with OpenCRVS](https://github.com/opencrvs/mosip/blob/dfa03cd9ea9cc01b4ec257edee5c0dc9837b1bbc/packages/mosip-api/src/routes/websub-credential-issued.ts#L63). All that code is abstracted away inside the middleware. You can decide to fork and configure as appropriate.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration-1.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
