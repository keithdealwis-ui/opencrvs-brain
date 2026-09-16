---
title: "How \"user scope\" options map to user details?"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/how-user-scope-options-map-to-user-details"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/users/how-user-scope-options-map-to-user-details.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:dab9bbfdaee011092f24dae7c99b995ecad3b9641d72d971f6492a4f3bb9fa2f"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/users/how-user-scope-options-map-to-user-details.md).

# How "user scope" options map to user details?

### Managing users

\
In production environments, users are created manually by other users. The locations where a new user can be placed, and the roles they can be assigned, are controlled by the creating [user's scopes.](https://github.com/opencrvs/opencrvs-core/blob/v2.0.0-beta/packages/commons/src/scopes.ts#L250)

**Example: `LOCAL_SYSTEM_ADMIN` creating or editing another user**

```
  const localSystemAdmin = {
    id: 'LOCAL_SYSTEM_ADMIN',
    label: {
      defaultMessage: 'Administrator',
      description: 'Name for user role Administrator',
      id: 'userRole.administrator'
    },
    scopes: defineScopes([
        { type: 'user.create', options: { accessLevel: 'administrativeArea', role: ['HOSPITAL_CLERK', 'COMMUNITY_LEADER', 'REGISTRATION_AGENT', 'LOCAL_REGISTRAR', 'PROVINCIAL_REGISTRAR'] } },
        { type: 'user.edit', options: { accessLevel: 'administrativeArea', role: ['HOSPITAL_CLERK', 'COMMUNITY_LEADER', 'REGISTRATION_AGENT', 'LOCAL_REGISTRAR', 'PROVINCIAL_REGISTRAR'] } },
        { type: 'user.read', options: { accessLevel: 'administrativeArea' } },
        { type: 'user.search', options: { accessLevel: 'administrativeArea' } }
      ])
  },
```

1. **Role selection** is limited to the roles defined in the `user.create` and `user.edit` scopes.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-3b93397dc492b168c9603bbebff9c7ebd83ff26f%2FScreenshot%202026-05-22%20at%2014.39.37.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

2. **Available locations** are limited to those within the `LOCAL_SYSTEM_ADMIN`'s administrative area. [See how scopes relate to jurisdictions](/technical/guides/configuration/users/roles-and-scopes.md).

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-1c9dd826f3e15179c3bb40713d6ad3b13a4f33d4%2FScreenshot%202026-05-22%20at%2014.41.37.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

3. **Editing restrictions** — the editor must have scope coverage over the edited user's location and role, both before and after any change. This prevents an editor from moving a user outside their own jurisdiction.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/users/how-user-scope-options-map-to-user-details.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
