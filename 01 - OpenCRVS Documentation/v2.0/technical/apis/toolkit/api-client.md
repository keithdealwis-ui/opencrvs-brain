---
title: "API Client"
source_url: "https://documentation.opencrvs.org/technical/apis/toolkit/api-client"
markdown_url: "https://documentation.opencrvs.org/technical/apis/toolkit/api-client.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3d69edd8dd97e77ff2ba3ee85b552d7d59eccedc0f1b35d6764ff22f41d7bc3a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis/toolkit/api-client.md).

# API Client

#### `createClient`

Creates a typed tRPC client for communicating with the OpenCRVS events service. Used in country-config server-side code to fetch event and location data, e.g. inside certificate handlebar helpers or custom action handlers.

**Signature**

```ts
import { createClient } from '@opencrvs/toolkit/api'

function createClient(
  baseUrl: string,
  token: `Bearer ${string}`
): TRPCClient
```

**Parameters**

| Parameter | Type                     | Description                                                                   |
| --------- | ------------------------ | ----------------------------------------------------------------------------- |
| `baseUrl` | `string`                 | URL of the tRPC events endpoint, e.g. `process.env.GATEWAY_HOST + '/events'`. |
| `token`   | `` `Bearer ${string}` `` | Authorization header value. Must include the `Bearer` prefix.                 |

The returned client exposes:

| Method                                                        | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| `client.event.get.query({ eventId })`                         | Fetch a single event document by ID.                  |
| `client.locations.list.query({ locationIds })`                | Fetch one or more location objects by UUID.           |
| `client.locations.getLocationHierarchy.query({ locationId })` | Get the full administrative hierarchy for a location. |
| `client.user.get.query(userId)`                               | Fetch a user's profile by ID.                         |

**Example 1 — fetch an event and read its current state**

```ts
import { createClient } from '@opencrvs/toolkit/api'
import { aggregateActionDeclarations } from '@opencrvs/toolkit/events'

const client = createClient(`${process.env.GATEWAY_HOST}/events`, `Bearer ${token}`)
const event = await client.event.get.query({ eventId })
const state = aggregateActionDeclarations(event)
const childNid = state['child.nid'] as string
```

**Example 2 — resolve a location name from its UUID**

```ts
const client = createClient(`${process.env.GATEWAY_HOST}/events`, `Bearer ${token}`)

const [location] = await client.locations.list.query({ locationIds: [locationId] })
return location.name
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis/toolkit/api-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
