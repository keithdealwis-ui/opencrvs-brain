---
title: "Advanced search"
source_url: "https://documentation.opencrvs.org/technical/apis/toolkit/configuration/advanced-search"
markdown_url: "https://documentation.opencrvs.org/technical/apis/toolkit/configuration/advanced-search.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:cd84149afce7ac2455b2b384317cdbfd7ad38247a454d2ceb88ce2b66ba59856"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/apis/toolkit/configuration/advanced-search.md).

# Advanced search

Advanced search fields are built with `field` and `event` from `@opencrvs/toolkit/events`. Each call returns a builder with `.exact()`, `.range()`, `.fuzzy()`, or `.within()`.

***

#### `field` (advanced search)

Configures a declaration form field for advanced search.

**Signature**

```ts
function field(
  fieldId: string,
  options?: {
    options?: SelectOption[]
    conditionals?: FieldConditional[]
    validations?: ValidationConfig[]
    searchCriteriaLabelPrefix?: TranslationConfig
  }
): AdvancedSearchFieldBuilder
```

**Parameters**

| Parameter                           | Type                  | Description                                                                        |
| ----------------------------------- | --------------------- | ---------------------------------------------------------------------------------- |
| `fieldId`                           | `string`              | ID of the declaration form field to expose in search.                              |
| `options.options`                   | `SelectOption[]?`     | Override dropdown options for the search input.                                    |
| `options.conditionals`              | `FieldConditional[]?` | Override visibility conditionals; pass `[]` to always show the field.              |
| `options.validations`               | `ValidationConfig[]?` | Override validations for the search input.                                         |
| `options.searchCriteriaLabelPrefix` | `TranslationConfig?`  | Prefix shown before the field label in search result summaries (e.g. `"Child's"`). |

The returned builder exposes four terminal methods:

| Method      | Match type         | Use for                             |
| ----------- | ------------------ | ----------------------------------- |
| `.exact()`  | Exact              | IDs, select fields, gender          |
| `.range()`  | Date range         | Dates of birth, registration dates  |
| `.fuzzy()`  | Fuzzy text         | Names                               |
| `.within()` | Location hierarchy | Administrative area location fields |

**Example 1 — name field with prefix and no validations**

```ts
import { field } from '@opencrvs/toolkit/events'

field('child.name', {
  searchCriteriaLabelPrefix: { id: 'prefix.child', defaultMessage: "Child's", description: '' },
  validations: [],
  conditionals: []
}).fuzzy()
```

**Example 2 — select field with custom options**

```ts
field('child.placeOfBirth', {
  options: [
    { value: 'HEALTH_FACILITY', label: { id: 'place.facility', defaultMessage: 'Health facility', description: '' } },
    { value: 'PRIVATE_HOME', label: { id: 'place.home', defaultMessage: 'Private home', description: '' } }
  ]
}).exact()
```

***

#### `event` (advanced search)

Configures an event metadata field (tracking ID, status, registration date, location) for advanced search.

**Signature**

```ts
function event(fieldId: EventFieldIdInput): AdvancedSearchFieldBuilder
```

**Parameters**

| `fieldId` value                                 | Description                             |
| ----------------------------------------------- | --------------------------------------- |
| `'trackingId'`                                  | The tracking ID assigned at creation.   |
| `'status'`                                      | Current registration status.            |
| `'legalStatuses.REGISTERED.acceptedAt'`         | Date of registration.                   |
| `'legalStatuses.REGISTERED.createdAtLocation'`  | Office where the record was registered. |
| `'legalStatuses.REGISTERED.registrationNumber'` | The official registration number.       |
| `'updatedAt'`                                   | Last modification date.                 |

**Example 1 — search by registration date range**

```ts
import { event } from '@opencrvs/toolkit/events'

event('legalStatuses.REGISTERED.acceptedAt').range()
```

**Example 2 — search by registering office (within the location hierarchy)**

```ts
event('legalStatuses.REGISTERED.createdAtLocation').within()
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/apis/toolkit/configuration/advanced-search.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
