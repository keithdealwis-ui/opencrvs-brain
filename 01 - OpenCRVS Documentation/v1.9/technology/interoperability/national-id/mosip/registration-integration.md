---
title: "Configuration"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:d9140de50828767a3f73cf67f900f68e2051366defe8afb0945900d458598d66"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration.md).

# Configuration

The countryconfig-mosip example contains a fully operational configuration for birth and death forms that includes:

* In-form authentication / verification with E-Signet
* Registration integration with MOSIP

{% embed url="<https://github.com/opencrvs/opencrvs-countryconfig-mosip>" %}

Helper functions that wrap your form components are written and contained within the opencrvs/mosip library for inclusion using package.json

{% embed url="<https://github.com/opencrvs/mosip>" %}

The mosip-api middleware is the key Docker container that must be deployed and configured with appropriate secrets to communicate with both E-Signet & MOSIP.

{% embed url="<https://github.com/opencrvs/mosip/tree/main/packages/mosip-api>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/registration-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
