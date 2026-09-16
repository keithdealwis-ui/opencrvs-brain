---
title: "Integrations"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:95600ce8cde9594ac4f8f7de3d6cb4ec6cb3911e9c499f708456805aa06e85a6"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/integrations.md).

# Integrations

- [Create a client](https://documentation.opencrvs.org/technical/guides/configuration/integrations/create-a-client.md)
- [Authenticate a client](https://documentation.opencrvs.org/technical/guides/configuration/integrations/authenticate-a-client.md): Authenticating with your client details to retrieve an access token using OAuth 2.0
- [Integration: ID systems](https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-id-systems.md)
- [Integration: Health notifications / Self-service portal](https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-health-notifications-self-service-portal.md): Submitting full or partial event applications into OpenCRVS from an external service such as a health institution or public portal.
- [Integration: Location management](https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-location-management.md)
- [MOSIP Overview](https://documentation.opencrvs.org/technical/guides/configuration/integrations/mosip-overview.md)
- [MOSIP Deployment](https://documentation.opencrvs.org/technical/guides/configuration/integrations/mosip-deployment.md)
- [MOSIP Form Authentication](https://documentation.opencrvs.org/technical/guides/configuration/integrations/mosip-form-authentication.md)
- [MOSIP Registration Integration](https://documentation.opencrvs.org/technical/guides/configuration/integrations/mosip-registration-integration.md)
- [Verifiable Credentials](https://documentation.opencrvs.org/technical/guides/configuration/integrations/verifiable-credentials.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/integrations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
