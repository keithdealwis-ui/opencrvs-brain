---
title: "Roles and scopes"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/roles-and-scopes"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/roles-and-scopes.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f5ecc6b7e9132335ce604fd29a295e76e66a4125f8aa810a07b46ecad58b236d"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/users/roles-and-scopes.md).

# Roles and scopes

Each user has an assigned role. A role determines which actions the user can take. Scopes are the mechanism that grants users access to perform role-specific actions. Learn [more about scopes here](/technical/guides/configuration/users/how-to-configure-scopes.md)

At a high level, a scope has two properties:

* **Type** — which action the user can take with the scope (e.g. `record.create`, `record.read`, `user.create`).
* **Options** — the limitations under which the action can be performed (e.g. a user can only search birth events that took place in their administrativeArea: `{ type: 'record.search', options: { event: ['birth'], placeOfEvent: 'administrativeArea' } }`).

A user is always assigned to a location. The location's position in the administrative hierarchy determines the jurisdiction the scope grants. Learn [how to configure place of event](/technical/guides/configuration/administrative-hierarchy/how-to-configure-place-of-event.md).\
\
**Example 1: Jurisdiction based on administrative area** `{ placeOfEvent: 'administrativeArea' }`

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-227c230cc5e04dfeff487598b93d654a4c6d16dc%2FScreenshot%202026-05-11%20at%2015.12.06.png?alt=media" alt=""><figcaption></figcaption></figure>

The dotted lines illustrate jurisdiction. An `administrativeArea` scope covers the administrative area itself, all locations within it, and all descending areas.

\
**Example 2: Jurisdiction based on location** — `{ placeOfEvent: 'location' }`

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-d145f6c3c5835be1d5dc32eef1a4339ca9aac6a4%2FScreenshot%202026-05-14%20at%2013.57.27.png?alt=media" alt=""><figcaption></figcaption></figure>

A location scope limits the user to a single location. For example, users in District Hospital A with scope `{ type: 'record.read', placeOfEvent: 'location' }` will only see events from District Hospital A. Events from District Hospital B and C would only be visible with the `{ placeOfEvent: 'administrativeArea' }` option.

**Example 3: Different roles directly under country**

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-9099a629679da052fcbceb2103ff336ba865942c%2FScreenshot%202026-05-14%20at%2014.17.03.png?alt=media" alt=""><figcaption></figcaption></figure>

In cases such as an embassy, it is safer to create a separate role with more limited scopes. If the same roles are reused, locations outside the country will inherit the same jurisdiction as HQ Office by default.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/users/roles-and-scopes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
