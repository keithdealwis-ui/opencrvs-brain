---
title: "Conditionals"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/conditionals"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/events/conditionals.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:166ee7318550de7a87bb60b9a39e1f3627ed8b3367e823d3e3ae15738fac048c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/events/conditionals.md).

# Conditionals

Configuring conditionals

A **conditional** is a rule that OpenCRVS evaluates at runtime to decide whether something is visible, enabled, valid, or should otherwise take effect for the current user and record.

You write conditionals using helpers exported from `@opencrvs/toolkit/events`. Under the hood, the helpers compile down to JSON-Schema, which means the same expression can be reused in many places — for example, the same `field('father.dob').isBefore().now()` expression is valid both as a field-show conditional and as a validator.

Conditionals are used in six places:

| Use site                   | What it controls                                                        | See                                                                                                  |
| -------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Field `conditionals`       | Whether a form field is shown, enabled, or displayed on review          | [Form fields](/technical/guides/configuration/events/declaration-and-forms/form-fields.md)           |
| Field `validation`         | Whether the field's value is valid                                      | [Form validations](/technical/guides/configuration/events/declaration-and-forms/form-validations.md) |
| Action `conditionals`      | Whether an action is shown or enabled                                   | [Actions](/technical/guides/configuration/events/actions.md#action-conditionals)                     |
| Action flag `conditional`  | Whether a flag is added or removed when the action is accepted          | [Flags](/technical/guides/configuration/events/flags.md)                                             |
| Workqueue filters          | Whether a record appears in a queue                                     | [Workqueues](/technical/guides/configuration/workqueues.md)                                          |
| Event summary conditionals | Whether a summary row is displayed or hidden on the event overview page | [Events](/technical/guides/configuration/events.md#eventconfig-schema)                               |

## Combinators

Combinators compose conditionals into larger expressions. They work on any conditional, regardless of what it checks.

| Helper         | Description                           |
| -------------- | ------------------------------------- |
| `and(...c)`    | All sub-conditions must hold.         |
| `or(...c)`     | At least one sub-condition must hold. |
| `not(c)`       | The sub-condition must not hold.      |
| `alwaysTrue()` | Always evaluates to true.             |
| `never()`      | Always evaluates to false.            |

**Example:**

```typescript
import {
  and,
  flag,
  InherentFlags,
  not,
  status
} from '@opencrvs/toolkit/events'

// The record is DECLARED and is not flagged as a potential duplicate
and(
  status('DECLARED'),
  not(flag(InherentFlags.POTENTIAL_DUPLICATE))
)
```

## Field-value conditionals

Use `field(fieldId)` to inspect the value of a form field. The returned object is a chain — call one of the methods below to produce a conditional. For nested values, chain `.get(path)` first (e.g. `field('applicant.address').get('country').isEqualTo('FAR')`).

| Method                              | Description                                                                |
| ----------------------------------- | -------------------------------------------------------------------------- |
| `.isEqualTo(value \| field)`        | Value equals the given literal or the value of another field.              |
| `.isFalsy()`                        | Value is `undefined`, `null`, `false`, or an empty string.                 |
| `.isUndefined()`                    | Value is undefined.                                                        |
| `.inArray(values)`                  | Value is one of the strings in the array.                                  |
| `.isBetween(min, max)`              | Numeric value is within `[min, max]`.                                      |
| `.isGreaterThan(value \| field)`    | Numeric value is strictly greater than the given value.                    |
| `.isLessThan(value \| field)`       | Numeric value is strictly less than the given value.                       |
| `.matches(pattern)`                 | String value matches the given regular expression.                         |
| `.isValidEnglishName()`             | String value is a valid Latin-script name.                                 |
| `.isValidAdministrativeLeafLevel()` | Administrative area value resolves to the lowest configured level.         |
| `.isBefore()` / `.isAfter()`        | Date comparisons — see [#date-conditionals](#date-conditionals "mention"). |
| `.get(path)` / `.getByPath(path[])` | Drill into a nested value before applying a check.                         |
| `.asDob()` / `.asAge()`             | Shortcuts for `.get('dob')` and `.get('age')`.                             |

**Example — show one field based on another:**

```typescript
import { ConditionalType, field } from '@opencrvs/toolkit/events'

{
  id: 'child.birthLocation',
  type: FieldType.LOCATION,
  // ...
  conditionals: [
    {
      type: ConditionalType.SHOW,
      conditional: field('child.placeOfBirth').isEqualTo('HEALTH_FACILITY')
    }
  ]
}
```

### Date conditionals

Date fields support a chained API for comparing against the current date, an absolute date, or another date field:

```typescript
// Father's DOB is before today
field('father.dob').isBefore().now()

// Mother's DOB is before child's DOB
field('mother.dob').isBefore().date(field('child.dob'))

// Child's DOB is no more than 365 days in the past
field('child.dob').isAfter().days(365).inPast()

// Mother's DOB is at least 14 years before the child's DOB
field('mother.dob').isBefore().days(14 * 365).fromDate(field('child.dob'))
```

The available chain steps for `.isBefore()` and `.isAfter()`:

* `.now()` — compares against today.
* `.date(date | field)` — compares against an absolute `YYYY-MM-DD` date or another date field.
* `.days(N).inPast()` / `.inFuture()` — N days before/after today.
* `.days(N).fromDate(date | field)` / `.fromNow()` — N days before/after the given date.

## User conditionals

Use the `user` helper to check who is currently signed in.

| Helper                             | Description                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| `user.hasRole(role)`               | User has the given role (for example `'LOCAL_REGISTRAR'`).   |
| `user.hasScope(scope)`             | User token contains the given scope.                         |
| `user.isOnline()`                  | The client is currently online.                              |
| `user.locationLevel(adminLevelId)` | User is assigned to the given administrative location level. |

**Example — only enable registration for registrars:**

```typescript
import {
  ActionType,
  ConditionalType,
  or,
  user
} from '@opencrvs/toolkit/events'

{
  type: ActionType.REGISTER,
  conditionals: [
    {
      type: ConditionalType.ENABLE,
      conditional: or(
        user.hasRole('REGISTRATION_AGENT'),
        user.hasRole('LOCAL_REGISTRAR')
      )
    }
  ]
}
```

## Record-state conditionals

Three helpers inspect the current state of the record:

* `status(statusValue)` — record is in the given state. Valid statuses: `CREATED`, `NOTIFIED`, `DECLARED`, `REGISTERED`, `ARCHIVED`.
* `flag(flagValue)` — record has the given flag set. See [Flags](/technical/guides/configuration/events/flags.md) for the list of inherent flags and how to define custom ones.
* `event.hasAction(actionType)` — record's action history contains an action of the given type. Chainable with `.minCount(n)` or `.maxCount(n)` to assert a specific number of occurrences, and `.withFields({ ... })` / `.withTemplate(id)` to narrow on action-payload fields.

**Example — show a custom action only while the record is declared and not yet validated:**

```typescript
import {
  ActionType,
  ConditionalType,
  and,
  flag,
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
    }
  ]
}
```

**Example — only allow the first certificate print:**

```typescript
import { ActionType, ConditionalType, event, not } from '@opencrvs/toolkit/events'

{
  type: ActionType.PRINT_CERTIFICATE,
  conditionals: [
    {
      type: ConditionalType.SHOW,
      conditional: not(event.hasAction(ActionType.PRINT_CERTIFICATE))
    }
  ]
}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/events/conditionals.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
