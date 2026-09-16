---
title: "How \"record scope\" options map to event declaration?"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/how-record-scope-options-map-to-event-declaration"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/how-record-scope-options-map-to-event-declaration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3992ca68050f27d81a57371311bf552fdc77db7170c1631fc06d57081cb255f4"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/users/how-record-scope-options-map-to-event-declaration.md).

# How "record scope" options map to event declaration?

\
Record scopes manage access to event-related actions. A persisted event is called record.\
\
You can find [available scopes and their definitions here](https://github.com/opencrvs/opencrvs-core/blob/v2.0.0-beta/packages/commons/src/scopes.ts)

For a scope to grant access, every option must match. Scope options are specific to each scope type. Most options control access based on the user or their jurisdiction. [See administrative hierarchy to understand how jurisdictions work](/technical/guides/configuration/administrative-hierarchy.md).\
\
**Example 1: Searching for records**

`record.search` accepts up to six options. When searching for records, scopes act as an additional filter — results are returned based on your search query, excluding any records you do not have access to. Undefined options are ignored.

```typescript
export const JurisdictionFilter = z
  .enum(['administrativeArea', 'location', 'all'])
  .describe(
    'Filters based on user jurisdiction relative to their office location in hierarchy.'
  )
export type JurisdictionFilter = z.infer<typeof JurisdictionFilter>

export const UserFilter = z
  .enum(['user'])
  .describe('Filters based on the user. Limits to self.')
export type UserFilter = z.infer<typeof UserFilter>

const scopeByEvent = z
  // Ensure input is always an array for consistent parsing, even if a single string is provided by qs.
  .preprocess(
    (val) => (val === undefined ? undefined : [val].flat()),
    z.array(z.string()).optional()
  )
  .describe('Event type, e.g. birth, death')

```

Scope options with truncated record metadata — ([Find the full type here](https://github.com/opencrvs/opencrvs-core/blob/v2.0.0-beta/packages/commons/src/events/EventMetadata.ts))

```ts
// Simplified type for readability.
type RecordSearchScope = {
 type: 'record.search',
 options: {
    event: scopeByEvent,
    placeOfEvent: JurisdictionFilter.optional(),
    declaredIn: JurisdictionFilter.optional(),
    declaredBy: UserFilter.optional(),
    registeredIn: JurisdictionFilter.optional(),
    registeredBy: UserFilter.optional()
 }
}

const eventMetadata = {
  "id": "0bac5df6-4b5f-4bad-99eb-23fbbd09f2a7",
  "type": "birth", // Type must be in the options.event array.
    "placeOfEvent": [
    /**
     options.placeOfEvent = 'all' means the same as undefined.
     options.placeOfEvent = 'administrativeArea' ensures user's administrativeAreaId is in the array.
     options.placeOfEvent = 'location' ensures user's primaryOfficeId is in the array.

     When place of event is 'location', events that happened within administrative area (e.g. birth took place in residential address),
     in a location without location id, are filtered out.
    */
    "9e93fbbb-a904-4d5e-ac0b-f77b969b964f",
    "18c5b1a3-49e5-4ff8-8096-8c856575e6d0",
    "f7461bf7-b6d9-436a-a66d-5191e6ef6586",
    "ab1f6257-6d3f-492c-8442-21b761b0036d"
  ],
  "status": "REGISTERED",
  /** 
   NOTE: 
     1. declaredIn and declaredBy implies that record has been declared.
     2. registeredIn and registeredBy implies that record has been registered.
  */
  "legalStatuses": {
    "DECLARED": {
      /**
       options.declaredBy = 'user' ensures user's id matches the one who declared it.
      */
      "createdBy": "c05e1c4f-20fa-4e69-af72-819b535d6242",
      "createdAtLocation": [
        /**
         options.declaredIn = 'all' means the same as undefined.
         options.declaredIn = 'administrativeArea' ensures user's administrativeAreaId is in the array.
         options.declaredIn = 'location' ensures user's primaryOfficeId is in the array.
         
         Declared location is defined by the location of the user performing the action.
        */
        "9e93fbbb-a904-4d5e-ac0b-f77b969b964f",
        "18c5b1a3-49e5-4ff8-8096-8c856575e6d0",
        "f7461bf7-b6d9-436a-a66d-5191e6ef6586",
        "ab1f6257-6d3f-492c-8442-21b761b0036d"
      ],
    },
    "REGISTERED": {
      /**
       options.registeredBy = 'user' ensures user's id matches the one who registered it.
      */
      "createdBy": "c05e1c4f-20fa-4e69-af72-819b535d6242",
       /**
         options.registeredIn = 'all' means the same as undefined.
         options.registeredIn = 'administrativeArea' ensures user's administrativeAreaId is in the array.
         options.registeredIn = 'location' ensures user's primaryOfficeId is in the array.
         
         Registered location is defined by the location of the user performing the action.
       */
      "createdAtLocation": [
        "9e93fbbb-a904-4d5e-ac0b-f77b969b964f",
        "18c5b1a3-49e5-4ff8-8096-8c856575e6d0",
        "f7461bf7-b6d9-436a-a66d-5191e6ef6586",
        "ab1f6257-6d3f-492c-8442-21b761b0036d"
      ],
    }
  },
  "declaration": {},
}
```

**Example 2: Declaring records — why options are limited**\
\
As shown in the previous example, using properties like `declared*` or `registered*` implies the event has already reached that state. For an event to be declared, it must be in a `NOTIFIED` or `CREATED` state. Including `declaredBy` or `registeredIn` in a declare scope would cause it to fail the necessary access checks, so the system limits these options accordingly.

```
// Simplified type for readability.
type RecordDeclareScope = {
 type: 'record.declare',
 options: {
    event: scopeByEvent,
    placeOfEvent: JurisdictionFilter.optional(),
 }
}
```

\ <br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/users/how-record-scope-options-map-to-event-declaration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
