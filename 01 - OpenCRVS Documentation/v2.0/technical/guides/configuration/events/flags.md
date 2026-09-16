---
title: "Flags"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/flags"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/flags.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:0d6bb9d2cc928297e4677c4149169e0f2dc301cd305b94af601cb0a2c8f7517e"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/events/flags.md).

# Flags

Configuring custom flags

A **flag** is a string label that describes the state of a record at a given point in its lifecycle. Flags are never stored in the database — they are always computed from the record's accepted action history. Replaying the same actions therefore always yields the same set of flags.

Flags are surfaced in three places:

* **Conditionals** — to show, hide or enable actions and form fields, via the `flag()` helper (`flag('validated')`, `not(flag(InherentFlags.POTENTIAL_DUPLICATE))`).
* **Workqueues** — to filter records, via `anyOf` / `noneOf` (`flags: { anyOf: [InherentFlags.INCOMPLETE], noneOf: [InherentFlags.REJECTED] }`).
* **Action availability** — core uses certain flags to gate which actions can be taken on a record (for example, `PRINT_CERTIFICATE` is hidden while a correction is pending).

There are two categories of flags:

| Category          | Source                                   | Example                                                     |
| ----------------- | ---------------------------------------- | ----------------------------------------------------------- |
| **Inherent flag** | Computed by core from the action history | `incomplete`, `rejected`, `correction-requested`            |
| **Custom flag**   | Defined and managed by country config    | `validated`, `revoked`, `escalated-to-provincial-registrar` |

## Inherent flags

Inherent flags are built into OpenCRVS core and computed from the record's action history. You cannot define new ones, but you can reference them in conditionals and add or remove them from actions via the `InherentFlags` enum exported from `@opencrvs/toolkit/events`.

| Flag                                 | When set                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `InherentFlags.REJECTED`             | The most recent non-meta action is `REJECT`.                                                                 |
| `InherentFlags.CORRECTION_REQUESTED` | A `REQUEST_CORRECTION` is pending and has not yet been approved or rejected.                                 |
| `InherentFlags.POTENTIAL_DUPLICATE`  | A `DUPLICATE_DETECTED` action has been recorded and the record has not since been marked as not a duplicate. |

**Example — referencing an inherent flag in a conditional:**

```typescript
import {
  ActionType,
  ConditionalType,
  flag,
  InherentFlags,
  not
} from '@opencrvs/toolkit/events'

// On a custom action: only allow it when the record is not a potential duplicate
{
  type: ActionType.CUSTOM,
  customActionType: 'VALIDATE_DECLARATION',
  // ...
  conditionals: [
    {
      type: ConditionalType.ENABLE,
      conditional: not(flag(InherentFlags.POTENTIAL_DUPLICATE))
    }
  ]
}
```

Inherent flags can also be added or removed from an action's `flags` array using the same shape as custom flags — see [#add-or-remove-flags-from-actions](#add-or-remove-flags-from-actions "mention").

## Custom flags

Custom flags let a country model workflow states that are not covered by inherent flags — for example a "validated" step, an escalation level, or a revocation marker.

A custom flag is defined once on the [EventConfig schema](/technical/guides/configuration/events.md#eventconfig-schema) under `flags`, then added or removed by individual actions.

### Define a custom flag

A custom flag has:

* `id` — the string identifier you'll reference from actions and conditionals. It must not match an inherent flag value or the `actionType:actionStatus` action flag pattern.
* `requiresAction` — when `true`, indicates the flag is meant to be cleared by a follow-up action. This property does not affect any functionality, it is only an indicator for developers.
* `label` — translatable label shown wherever the flag is displayed.

**Example — defining custom flags on a birth event:**

```typescript
// src/events/birth/index.ts
import { defineConfig } from '@opencrvs/toolkit/events'

export const birthEvent = defineConfig({
  id: 'birth',
  // label, declaration, actions, ...
  flags: [
    {
      id: 'validated',
      label: {
        defaultMessage: 'Validated',
        description: 'Flag label for a declaration that has been validated',
        id: 'event.birth.flag.validated'
      },
      requiresAction: true
    }
  ]
})
```

### FlagConfig schema

## The FlagConfig object

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"components":{"schemas":{"FlagConfig":{"type":"object","properties":{"id":{"type":"string","description":"Custom flag identifier defined by the country config."},"requiresAction":{"type":"boolean","description":"Indicates if this flag expects an action to be performed to be cleared."},"label":{"description":"Human readable label of the flag.","$ref":"#/components/schemas/TranslationConfigOutput"}},"required":["id","requiresAction","label"],"additionalProperties":false,"description":"Configuration for a custom flag that can be added to or removed from records by event actions."},"TranslationConfigOutput":{"type":"object","properties":{"id":{"type":"string","description":"The identifier of the translation referred in translation CSV files"},"defaultMessage":{"type":"string","description":"Default translation message"},"description":{"type":"string","description":"Describe the translation for a translator to be able to identify it."}},"required":["id","defaultMessage","description"],"additionalProperties":false,"description":"Translation configuration"}}}}
```

### Add or remove flags from actions

Each action may include a `flags` array. Each entry is an [`ActionFlagConfig`](#actionflagconfig-schema):

* `id` — the flag to add or remove. May be a custom flag id (e.g. `'validated'`) or an inherent flag (e.g. `InherentFlags.REJECTED`).
* `operation` — `'add'` or `'remove'`.
* `conditional` *(optional)* — a conditional gating whether the operation is applied. If omitted, the operation is applied unconditionally whenever the action is accepted.

**Example — a custom action that sets the `validated` flag:**

```typescript
import {
  ActionType,
  ConditionalType,
  and,
  flag,
  InherentFlags,
  not,
  status
} from '@opencrvs/toolkit/events'

{
  type: ActionType.CUSTOM,
  customActionType: 'VALIDATE_DECLARATION',
  conditionals: [
    // Only show while the record is declared but not yet validated
    {
      type: ConditionalType.SHOW,
      conditional: and(status('DECLARED'), not(flag('validated')))
    }
  ],
  flags: [{ id: 'validated', operation: 'add' }],
  // label, auditHistoryLabel, icon, ...
}
```

**Example — adding a flag conditionally based on the form:**

When `conditional` is provided, the operation is only applied if the conditional evaluates to true against the record's aggregated form state at the moment the action is accepted. This is useful for flags that depend on declaration data — for example flagging a birth as a late registration if the child's date of birth is more than `N` days in the past:

```typescript
import {
  ActionType,
  and,
  field,
  not
} from '@opencrvs/toolkit/events'

{
  type: ActionType.DECLARE,
  // ...
  flags: [
    {
      id: 'approval-required-for-late-registration',
      operation: 'add',
      conditional: and(
        not(
          field('child.dob')
            .isAfter()
            .days(365)
            .inPast()
        ),
        field('child.dob').isBefore().now()
      )
    }
  ]
}
```

**Example — clearing flags when an action runs:**

The `remove` operation clears a flag if it is currently set on the record. It is a no-op otherwise. The same action may add and remove multiple flags in a single `flags` array:

```typescript
{
  type: ActionType.CUSTOM,
  customActionType: 'APPROVE_DECLARATION',
  // ...
  flags: [
    { id: InherentFlags.REJECTED, operation: 'remove' },
    { id: 'approval-required-for-late-registration', operation: 'remove' }
  ]
}
```

### ActionFlagConfig schema

## The ActionFlagConfig object

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"components":{"schemas":{"ActionFlagConfig":{"type":"object","properties":{"id":{"anyOf":[{"anyOf":[{"type":"string"},{"type":"string","enum":["incomplete","rejected","correction-requested","potential-duplicate","edit-in-progress"]}]},{"type":"string","description":"Custom flag identifier defined by the country config."}]},"operation":{"type":"string","enum":["add","remove"],"description":"Operation to perform on the flag."},"conditional":{"description":"When conditional is met, the operation is performed on the flag. If not provided, the operation is performed unconditionally.","$ref":"#/components/schemas/Conditional"}},"required":["id","operation"],"additionalProperties":false,"description":"Add or remove operation applied to a flag when the parent action is accepted. Optionally gated by a conditional."},"Conditional":{"description":"JSON schema conditional configuration"}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/events/flags.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
