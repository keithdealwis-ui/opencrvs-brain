---
title: "How to limit location and administrative area options in event declaration"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-limit-location-and-administrative-area-options-in-event-declaration"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-limit-location-and-administrative-area-options-in-event-declaration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:6837bd7e604a64fe5fea4a071e35e054639f13b8c04a115b2f2254bc13e3f4de"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-limit-location-and-administrative-area-options-in-event-declaration.md).

# How to limit location and administrative area options in event declaration

Scopes serve two purposes: keeping the system secure by granting only the necessary access, and making declarations easy and intuitive to fill in. In this example, a `HOSPITAL_CLERK` can only declare births at their own location.

[See other roles to help you configure your own.](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/roles/roles.ts#L199)\
\
**Example: `HOSPITAL_CLERK`**<br>

**Step 1: Configure the role**

```
  const hospitalClerk = {
    id: 'HOSPITAL_CLERK',
    label: {
      defaultMessage: 'Hospital Official',
      description: 'Name for user role Hospital Official',
      id: 'userRole.hospitalClerk'
    },
    scopes: defineScopes([
      { type: 'record.create', options: { placeOfEvent: 'location' } },
      { type: 'record.read', options: { placeOfEvent: 'location' } },
      { type: 'record.declare', options: { placeOfEvent: 'location' } },
      { type: 'record.notify', options: { placeOfEvent: 'location' } },
    ])
  }
```

**Step 2: Configure the event form**

[See the full event example for context.](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/events/birth/forms/pages/child.ts)

<pre><code><strong>// 1. Other dropdown options are not shown for the HOSPITAL_CLERK. Only HEALTH_FACILITY is visible.
</strong>const placeOfBirthOptions = [
  {
    value: PlaceOfBirth.HEALTH_FACILITY,
    label: placeOfBirthMessageDescriptors.HEALTH_FACILITY,
    ]
  },
  {
    value: PlaceOfBirth.PRIVATE_HOME,
    label: placeOfBirthMessageDescriptors.PRIVATE_HOME,
    conditionals: [
      {
        type: ConditionalType.SHOW,
        conditional: not(user.hasRole('HOSPITAL_CLERK'))
      }
    ]
  },
  {
    value: PlaceOfBirth.OTHER,
    label: placeOfBirthMessageDescriptors.OTHER.defaultMessage,
    conditionals: [
      {
        type: ConditionalType.SHOW,
        conditional: not(user.hasRole('HOSPITAL_CLERK'))
      }
    ]
  }
] satisfies SelectOption[]

// 2. Configure select with options.
const child =  {
    id: 'child.placeOfBirth',
    type: FieldType.SELECT,
    options: placeOfBirthOptions
  },
    // 3. Configure 
    {
      id: 'child.birthLocation',
      type: FieldType.LOCATION,
      // 4. Field is only shown when HEALTH_FACILITY is selected.
      conditionals: [
        {
          type: ConditionalType.SHOW,
          conditional: field('child.placeOfBirth').isEqualTo(
            PlaceOfBirth.HEALTH_FACILITY
          )
        }
      ],
      configuration: {
      // 5. By default any type of location is included. Now we filter by "HEALTH_FACILITY" type
        locationTypes: ['HEALTH_FACILITY'],
        // 6. Another filter which further limits options only to what user's record.scope has.
        allowedLocations: user.jurisdiction(
          user.scope('record.create').attribute('placeOfEvent')
        )
      }
    }
</code></pre>

<div><figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-a129eeda3f9de0a767d12fb03e840688ab4ef17e%2FScreenshot%202026-05-22%20at%209.52.05.png?alt=media" alt=""><figcaption></figcaption></figure> <figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-f0258f7fccf012288f623e218268d82cfefac7eb%2FScreenshot%202026-05-22%20at%209.51.50.png?alt=media" alt=""><figcaption></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-limit-location-and-administrative-area-options-in-event-declaration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
