---
title: "Authenticate a client"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/authenticate-a-client"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/authenticate-a-client.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e4080176f47ade24182e7406cd6b4660e1b241abeec0549d75cd35a97cf77598"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/integrations/authenticate-a-client.md).

# Authenticate a client

Authenticating with your client details to retrieve an access token using OAuth 2.0

Now that you have created a client, when you want to perform an API request you must first authenticate and receive an OpenCRVS access token. The token endpoint is OAuth 2.0 compliant.

Client access tokens are valid for a maximum of 10 minutes. After it expires you must authenticate again to retrieve a new access token.

**URL**

`POST https://gateway.<your_domain>/auth/token`

**Request payload**

| Parameter       | Type   | Description                                |
| --------------- | ------ | ------------------------------------------ |
| `client_id`     | string | The unique identifier for your client      |
| `client_secret` | string | The secret key associated with your client |
| `grant_type`    | string | Must be set to `client_credentials`        |

**Example request body**

```json
{
    "client_id": "2fd153ab-86c8-45fb-990d-721140e46061",
    "client_secret": "8636abe2-affb-4238-8bff-200ed3652d1e",
    "grant_type": "client_credentials"
}
```

**Response**

```json
{
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6Ikp..."
}
```

The token is a JWT and must be included as a header `Authorization: Bearer <token>` in all future API requests. The content of an OpenCRVS access token looks like this:


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/integrations/authenticate-a-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
