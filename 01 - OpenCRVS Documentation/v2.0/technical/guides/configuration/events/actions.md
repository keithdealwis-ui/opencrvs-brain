---
title: "Actions"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/actions"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/actions.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b7092a11ab8ad7bf8e36ba435370cde30761642f1747c3e6fa9ef781272464c5"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/events/actions.md).

# Actions

Configuring actions for your event

Actions are the workflow steps users can take on a record (declare, validate, register, reject, print a certificate, and so on). You configure them on each event inside `defineConfig()` under the `actions` array. This means that the action configuration is event-specific.

[Core actions](/technical/guides/configuration/events/actions/core-actions.md) are actions defined by the OpenCRVS core and which all events must implement. In addition to core actions, an event may implement any number of [Custom actions](/technical/guides/configuration/events/actions/custom-actions.md). These actions may be freely defined by each country to meet its unique requirements.

The order of actions in the action menu on the UI is defined on the [EventConfig schema](/technical/guides/configuration/events.md#eventconfig-schema) with the `actionOrder` property. Each entry is either an `ActionType` (for core actions) or a `customActionType` string (for custom actions).

**Example:**

```typescript
export const birthEvent = defineConfig({
  id: 'birth',
  actionOrder: [
    ActionType.ASSIGN,
    ActionType.REGISTER,
    ActionType.DECLARE,
    ActionType.EDIT,
    ActionType.MARK_AS_DUPLICATE,
    'MY_CUSTOM_ACTION_TYPE',
    ActionType.REJECT,
    ActionType.ARCHIVE,
    ActionType.DELETE,
    ActionType.PRINT_CERTIFICATE,
    ActionType.REQUEST_CORRECTION,
    ActionType.UNASSIGN
  ],
  actions: [
    // 'actions' must contain all core action configurations,
    // and additionally it may contain any number of custom action configurations
  ],
  // label, declaration, title, summary, flags, ...
})
```

## Action conditionals

Every action config accepts an optional `conditionals` array which gates whether the action is shown or enabled for the current user and record. Each entry is an `ActionConditional` wrapping a conditional expression:

* `ConditionalType.SHOW` — Action is shown only when the conditional holds.
* `ConditionalType.ENABLE` — Action is shown but disabled unless the conditional holds.

When `conditionals` is omitted, the action is shown and enabled for everyone.

For available conditional helper functions, see [Conditionals](/technical/guides/configuration/events/conditionals.md)

**Example:**

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
    {
      type: ConditionalType.SHOW,
      conditional: and(status('DECLARED'), not(flag('validated')))
    },
    {
      type: ConditionalType.ENABLE,
      conditional: not(flag(InherentFlags.POTENTIAL_DUPLICATE))
    }
  ]
}
```

### ActionConditional schema

## The ActionConditional object

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"components":{"schemas":{"ActionConditional":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","const":"SHOW"},"conditional":{"$ref":"#/components/schemas/Conditional"}},"required":["type","conditional"],"additionalProperties":false,"description":"If 'SHOW' conditional is defined, the component is shown to the user only if the condition is met"},{"type":"object","properties":{"type":{"type":"string","const":"ENABLE"},"conditional":{"$ref":"#/components/schemas/Conditional"}},"required":["type","conditional"],"additionalProperties":false,"description":"If 'ENABLE' conditional is defined, the component is enabled only if the condition is met"}],"description":"Conditional gating whether an action is shown (SHOW) or enabled (ENABLE). When omitted from an action, the action is shown and enabled for everyone.","type":"object"},"Conditional":{"description":"JSON schema conditional configuration"}}}}
```

## Action triggers

For configuring action triggers, see [Action triggers](/technical/guides/configuration/action-triggers.md)

## Scopes

For configuring user scopes for actions, see [Users](/technical/guides/configuration/users.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/events/actions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
