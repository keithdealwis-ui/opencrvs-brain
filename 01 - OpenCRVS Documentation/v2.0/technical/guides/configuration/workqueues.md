---
title: "Workqueues"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/workqueues"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/workqueues.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:cc6e6d572b980532fe3c7ee8f041cfedfc52d1f50ee8c73e6b37643c75a88174"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/workqueues.md).

# Workqueues

Configuring workqueues

{% hint style="info" %}
This is technical documentation. For the functional overview of workqueues, see [Workqueues](/functional/markdown/workflows/workqueues.md)
{% endhint %}

A **workqueue** is a filtered list of records shown in the OpenCRVS UI. Each workqueue applies a query against the event index and presents the matching records in a table.

<div align="center"><figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-f67f8181f213ef7311a09139a1a25f9be5c40f3f%2FScreenshot%202026-05-20%20at%2014.38.43.png?alt=media" alt="" width="563"><figcaption><p>A list of configured workqueues</p></figcaption></figure></div>

### Default workqueues

OpenCRVS core provides two workqueues that you do not need to configure. They are not affected by the `workqueue` scope's `ids` list — their visibility is determined by the role's record scopes instead.

| Workqueue  | Shown when                             | Contents                                                                                                                                                    |
| ---------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Drafts** | The role has the `record.create` scope | Records the user has started filling in but not yet submitted. Stored locally on the client until declared.                                                 |
| **Outbox** | The role has any `record.*` scope      | Records the user has triggered actions on that are queued for synchronization with the server. Useful for offline work — the queue drains once back online. |

### Configuring workqueues

Workqueues are configured in the countryconfig under `src/api/workqueue/workqueueConfig.ts`.

Wrap your workqueue array in `defineWorkqueues()` from `@opencrvs/toolkit/events`. The helper parses each entry against `WorkqueueConfig` and warns about common misconfigurations.

{% hint style="info" %}
**Note:** Access to any workqueue requires the **`record.search`** scope. The scope's options further narrow which records the user actually sees inside the workqueue, so a user might only be able to access a subset of the workqueue's matching records.
{% endhint %}

**Example workqueue config from** [**`src/api/workqueue/workqueueConfig.ts`**](https://github.com/opencrvs/opencrvs-countryconfig/blob/develop/src/api/workqueue/workqueueConfig.ts)**:**

```typescript
// src/api/workqueue/workqueueConfig.ts
import {
  ActionType,
  EventStatus,
  InherentFlags,
  defineWorkqueues,
  user
} from '@opencrvs/toolkit/events'

export const Workqueues = defineWorkqueues([
  {
    slug: 'assigned-to-you',
    icon: 'PushPin',
    name: {
      id: 'workqueues.assignedToYou.title',
      defaultMessage: 'Assigned to you',
      description: 'Title of assigned to you workqueue'
    },
    query: { assignedTo: { type: 'exact', term: user('id') } },
    action: { type: ActionType.READ }
  },
  {
    slug: 'pending-registration',
    icon: 'PenNib',
    name: {
      id: 'workqueues.pendingRegistration.title',
      defaultMessage: 'Pending registration',
      description: 'Title of pending registration workqueue'
    },
    query: {
      status: { type: 'exact', term: EventStatus.enum.DECLARED },
      flags: {
        anyOf: ['validated'],
        noneOf: [InherentFlags.POTENTIAL_DUPLICATE]
      },
      'legalStatuses.DECLARED.createdAtLocation': {
        type: 'within',
        location: user('primaryOfficeId')
      }
    },
    action: { type: ActionType.READ }
  }
])
```

### Controlling visibility of workqueues

A configured workqueue is only visible to users whose role grants the **`workqueue` scope** for its `slug`. The scope carries an `ids` option listing the slugs the role may see.

```typescript
// src/data-seeding/roles/roles.ts
{
  id: 'REGISTRATION_AGENT',
  // ...
  scopes: defineScopes([
    // ... other scopes
    {
      type: 'workqueue',
      options: {
        ids: [
          'assigned-to-you',
          'recent',
          'requires-completion',
          'in-external-validation',
          'pending-validation',
          'pending-updates',
          'pending-approval',
          'pending-certification',
          'pending-issuance',
          'correction-requested'
        ]
      }
    }
  ])
}
```

Notes:

* A workqueue defined in `workqueueConfig.ts` but not listed in any role's `workqueue` scope is never shown.
* Two roles may share the same workqueue by listing the same slug in both — there is no per-role override of the underlying query. To give different roles a different view, define separate workqueues with different slugs.
* The Outbox and Drafts workqueues are not affected by `ids` — they appear automatically.

For the full scope configuration, see [Users](/technical/guides/configuration/users.md).

### WorkqueueConfig schema

## The WorkqueueConfig object

```json
{"openapi":"3.1.0","info":{"title":"OpenCRVS API","version":"2.0.0"},"components":{"schemas":{"WorkqueueConfig":{"type":"object","properties":{"slug":{"type":"string","description":"Determines the url of the workqueue."},"name":{"description":"Title of the workflow (both in navigation and on the page)","$ref":"#/components/schemas/TranslationConfigOutput"},"query":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","const":"and"},"clauses":{"type":"array","items":{"type":"object","properties":{"eventType":{"type":"string"},"status":{"anyOf":[{"$ref":"#/components/schemas/AnyOfStatusOutput"},{"$ref":"#/components/schemas/ExactStatusOutput"}]},"createdAt":{"$ref":"#/components/schemas/DateConditionOutput"},"updatedAt":{"$ref":"#/components/schemas/DateConditionOutput"},"legalStatuses.DECLARED.createdAtLocation":{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},"legalStatuses.DECLARED.createdByRole":{"$ref":"#/components/schemas/AnyOfOutput"},"legalStatuses.REGISTERED.createdAt":{"$ref":"#/components/schemas/DateConditionOutput"},"legalStatuses.REGISTERED.createdAtLocation":{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},"legalStatuses.REGISTERED.createdByRole":{"$ref":"#/components/schemas/AnyOfOutput"},"legalStatuses.REGISTERED.registrationNumber":{"$ref":"#/components/schemas/ExactOutput"},"createdAtLocation":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false}]},"updatedAtLocation":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false}]},"updatedByUserRole":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"assignedTo":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"createdBy":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"createdByUserType":{"$ref":"#/components/schemas/ExactUserTypeOutput"},"updatedBy":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"trackingId":{"$ref":"#/components/schemas/ExactOutput"},"flags":{"$ref":"#/components/schemas/ContainsFlagsOutput"},"data":{"$ref":"#/components/schemas/QueryInputOutput"}},"additionalProperties":false}}},"required":["type","clauses"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"or"},"clauses":{"type":"array","items":{"type":"object","properties":{"eventType":{"type":"string"},"status":{"anyOf":[{"$ref":"#/components/schemas/AnyOfStatusOutput"},{"$ref":"#/components/schemas/ExactStatusOutput"}]},"createdAt":{"$ref":"#/components/schemas/DateConditionOutput"},"updatedAt":{"$ref":"#/components/schemas/DateConditionOutput"},"legalStatuses.DECLARED.createdAtLocation":{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},"legalStatuses.DECLARED.createdByRole":{"$ref":"#/components/schemas/AnyOfOutput"},"legalStatuses.REGISTERED.createdAt":{"$ref":"#/components/schemas/DateConditionOutput"},"legalStatuses.REGISTERED.createdAtLocation":{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},"legalStatuses.REGISTERED.createdByRole":{"$ref":"#/components/schemas/AnyOfOutput"},"legalStatuses.REGISTERED.registrationNumber":{"$ref":"#/components/schemas/ExactOutput"},"createdAtLocation":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false}]},"updatedAtLocation":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","location"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false}]},"updatedByUserRole":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"assignedTo":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"createdBy":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"createdByUserType":{"$ref":"#/components/schemas/ExactUserTypeOutput"},"updatedBy":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string"},{"type":"object","properties":{"$userField":{"type":"string","enum":["id","name","role","fullHonorificName","device","firstname","middlename","surname","signature","avatar","primaryOfficeId","administrativeAreaId"]},"$location":{"type":"string"}},"required":["$userField"],"additionalProperties":false}]}},"required":["type","term"],"additionalProperties":false},"trackingId":{"$ref":"#/components/schemas/ExactOutput"},"flags":{"$ref":"#/components/schemas/ContainsFlagsOutput"},"data":{"$ref":"#/components/schemas/QueryInputOutput"}},"additionalProperties":false}}},"required":["type","clauses"],"additionalProperties":false}],"type":"object"},"action":{"description":"Workqueue call-to-action button configuration. This determines the quick action button shown on each event card and the action taken when the button is clicked.","type":"object","properties":{"type":{"type":"string","enum":["READ","DELETE","DECLARE","REGISTER","EDIT","REJECT","MARK_AS_DUPLICATE","ARCHIVE","UNARCHIVE","PRINT_CERTIFICATE","REQUEST_CORRECTION"]}},"required":["type"],"additionalProperties":false},"columns":{"default":[{"label":{"id":"workqueues.dateOfEvent","defaultMessage":"Date of Event","description":"Label for workqueue column: dateOfEvent"},"value":{"$event":"dateOfEvent"}},{"label":{"id":"workqueue.default.column.modifiedAt","defaultMessage":"Last updated","description":"This is the label for the workqueue column"},"value":{"$event":"updatedAt"}}],"type":"array","items":{"$ref":"#/components/schemas/WorkqueueColumnOutput"}},"icon":{"type":"string","enum":["Archived","Assigned","Briefcase","Certified","Close","Collapse","Draft","DuplicateYellow","Expand","ExternalValidate","FilledCheck","InReview","Offline","Registered","RequiresUpdates","Sent","Validated","WaitingApproval","ChartActivity","Activity","Archive","ArchiveTray","ArrowLeft","ArrowRight","Buildings","Circle","CaretDown","CaretLeft","CaretRight","ChartBar","ChartLine","ChatCircle","CheckSquare","Compass","Check","Copy","Database","DotsThreeVertical","ArrowCounterClockwise","MagnifyingGlassMinus","MagnifyingGlassPlus","Export","Eye","EyeSlash","Envelope","File","FileLock","FileSearch","FileMinus","FilePlus","FileText","FileX","Handshake","Gear","GitBranch","IdentificationCard","List","ListBullets","Lock","MagnifyingGlass","MapPin","Medal","NotePencil","Paperclip","PaperPlaneTilt","Pen","PenNib","Pencil","PencilSimpleLine","Phone","Plus","Printer","SignOut","Stamp","Star","Target","TextT","Trash","UploadSimple","User","UserPlus","Users","WarningCircle","X","ChatText","CircleWavyCheck","CircleWavyQuestion","ArchiveBox","ArrowCircleDown","FileArrowUp","FileDotted","Files","PencilLine","PencilCircle","UserCircle","Clock","QrCode","Webcam","Sun","DeviceTabletCamera","Globe","Fingerprint","PushPin","Timer"]},"emptyMessage":{"$ref":"#/components/schemas/TranslationConfigOutput"}},"required":["slug","name","query","columns","icon"],"additionalProperties":false,"description":"Configuration for workqueue."},"TranslationConfigOutput":{"type":"object","properties":{"id":{"type":"string","description":"The identifier of the translation referred in translation CSV files"},"defaultMessage":{"type":"string","description":"Default translation message"},"description":{"type":"string","description":"Describe the translation for a translator to be able to identify it."}},"required":["id","defaultMessage","description"],"additionalProperties":false,"description":"Translation configuration"},"AnyOfStatusOutput":{"type":"object","properties":{"type":{"type":"string","const":"anyOf"},"terms":{"type":"array","items":{"type":"string","enum":["CREATED","NOTIFIED","DECLARED","REGISTERED","ARCHIVED"]}}},"required":["type","terms"],"additionalProperties":false},"ExactStatusOutput":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"type":"string","enum":["CREATED","NOTIFIED","DECLARED","REGISTERED","ARCHIVED"]}},"required":["type","term"],"additionalProperties":false},"DateConditionOutput":{"anyOf":[{"$ref":"#/components/schemas/ExactDateOutput"},{"$ref":"#/components/schemas/RangeDateOutput"},{"$ref":"#/components/schemas/TimePeriodOutput"}]},"ExactDateOutput":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"anyOf":[{"type":"string","format":"date","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))$"},{"type":"string","format":"date-time","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))T(?:(?:[01]\\d|2[0-3]):[0-5]\\d(?::[0-5]\\d(?:\\.\\d+)?)?(?:Z))$"}]}},"required":["type","term"],"additionalProperties":false},"RangeDateOutput":{"type":"object","properties":{"type":{"type":"string","const":"range"},"gte":{"anyOf":[{"type":"string","format":"date","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))$"},{"type":"string","format":"date-time","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))T(?:(?:[01]\\d|2[0-3]):[0-5]\\d(?::[0-5]\\d(?:\\.\\d+)?)?(?:Z))$"}]},"lte":{"anyOf":[{"type":"string","format":"date","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))$"},{"type":"string","format":"date-time","pattern":"^(?:(?:\\d\\d[2468][048]|\\d\\d[13579][26]|\\d\\d0[48]|[02468][048]00|[13579][26]00)-02-29|\\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\\d|30)|(?:02)-(?:0[1-9]|1\\d|2[0-8])))T(?:(?:[01]\\d|2[0-3]):[0-5]\\d(?::[0-5]\\d(?:\\.\\d+)?)?(?:Z))$"}]}},"required":["type","gte","lte"],"additionalProperties":false},"TimePeriodOutput":{"type":"object","properties":{"type":{"type":"string","const":"timePeriod"},"term":{"type":"string","enum":["last7Days","last30Days","last90Days","last365Days"]}},"required":["type","term"],"additionalProperties":false},"AnyOfOutput":{"type":"object","properties":{"type":{"type":"string","const":"anyOf"},"terms":{"type":"array","items":{"type":"string"}}},"required":["type","terms"],"additionalProperties":false},"ExactOutput":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"type":"string"}},"required":["type","term"],"additionalProperties":false},"ExactUserTypeOutput":{"type":"object","properties":{"type":{"type":"string","const":"exact"},"term":{"type":"string","enum":["user","system"]}},"required":["type","term"],"additionalProperties":false},"ContainsFlagsOutput":{"type":"object","properties":{"anyOf":{"type":"array","items":{"anyOf":[{"anyOf":[{"type":"string"},{"type":"string","enum":["incomplete","rejected","correction-requested","potential-duplicate","edit-in-progress"]}]},{"type":"string","description":"Custom flag identifier defined by the country config."}]}},"noneOf":{"type":"array","items":{"anyOf":[{"anyOf":[{"type":"string"},{"type":"string","enum":["incomplete","rejected","correction-requested","potential-duplicate","edit-in-progress"]}]},{"type":"string","description":"Custom flag identifier defined by the country config."}]}},"allOf":{"type":"array","items":{"anyOf":[{"anyOf":[{"type":"string"},{"type":"string","enum":["incomplete","rejected","correction-requested","potential-duplicate","edit-in-progress"]}]},{"type":"string","description":"Custom flag identifier defined by the country config."}]}}},"additionalProperties":false},"QueryInputOutput":{"anyOf":[{"oneOf":[{"$ref":"#/components/schemas/FuzzyOutput"},{"$ref":"#/components/schemas/ExactOutput"},{"$ref":"#/components/schemas/RangeOutput"},{"$ref":"#/components/schemas/WithinOutput"},{"$ref":"#/components/schemas/AnyOfOutput"}],"type":"object","discriminator":{"propertyName":"type","mapping":{"fuzzy":"#/components/schemas/FuzzyOutput","exact":"#/components/schemas/ExactOutput","range":"#/components/schemas/RangeOutput","within":"#/components/schemas/WithinOutput","anyOf":"#/components/schemas/AnyOfOutput"}}},{"type":"object","propertyNames":{"type":"string"},"additionalProperties":{"$ref":"#/components/schemas/QueryInputOutput"}}]},"FuzzyOutput":{"type":"object","properties":{"type":{"type":"string","const":"fuzzy"},"term":{"type":"string"}},"required":["type","term"],"additionalProperties":false},"RangeOutput":{"type":"object","properties":{"type":{"type":"string","const":"range"},"gte":{"type":"string"},"lte":{"type":"string"}},"required":["type","gte","lte"],"additionalProperties":false},"WithinOutput":{"type":"object","properties":{"type":{"type":"string","const":"within"},"location":{"type":"string"}},"required":["type","location"],"additionalProperties":false},"WorkqueueColumnOutput":{"type":"object","properties":{"label":{"$ref":"#/components/schemas/TranslationConfigOutput"},"value":{"type":"object","properties":{"$event":{"type":"string","enum":["id","type","status","createdAt","dateOfEvent","placeOfEvent","createdBy","createdByUserType","updatedByUserRole","createdAtLocation","updatedAtLocation","updatedAt","assignedTo","updatedBy","trackingId","legalStatuses","flags","title","outbox"]}},"required":["$event"],"additionalProperties":false}},"required":["label","value"],"additionalProperties":false,"description":"Configuration for a single workqueue column. The value references an event metadata key (e.g. `dateOfEvent`, `status`, `trackingId`)."}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/workqueues.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
