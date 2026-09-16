---
title: "User roles & scopes"
source_url: "https://documentation.opencrvs.org/v1.9/product-specifications/users"
markdown_url: "https://documentation.opencrvs.org/v1.9/product-specifications/users.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e62652873a82024be5797afa2d3eb98c2c6c872e00d757c5a4dd1c3d1d97acfd"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/product-specifications/users.md).

# User roles & scopes

OpenCRVS supports the creation of multiple custom users with specific permissions (scopes) to control what they can and cannot do in the system. This feature allows countries to define user roles and their corresponding scopes based on their specific needs.

### Key Features

**Unlimited user role configuration**: Administrators can create and configure any number of system user roles.

**Custom role naming**: Each user role can have a custom name (e.g., *Healthcare Worker, Mayor, Registrar*).

**Scope-based permissions**: The functionalities available to each user role can be controlled by assigning specific scopes

### User Role Scopes

The following are the key scope categories available for configuration:

| Scope                                    | Description                                                                                                                                                                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| record.create                            | This scope adds a custom event as an option in the event declaration form select                                                                                                                                                                                |
| record.notify                            | This scope allows a user to send incomplete declarations to an assinged office. Declarations have the status 'Notified'                                                                                                                                         |
| record.declare                           | This scope allows a user to send complete declarations to their assigned office. Declarations will have the status 'Declared'                                                                                                                                   |
| record.declared.validate                 | This scope allows a user to validate a declaration                                                                                                                                                                                                              |
| record.declared.reject                   | This scope allows a user to reject a declaration                                                                                                                                                                                                                |
| record.declared.archive                  | This scope allows a user to archive a declaration. An archived declaration has the status 'Archived'                                                                                                                                                            |
| record.archived.reinstate                | This scope allows a user to reinstate an archived declaration. Declarations will revert to the previous status before it was archived                                                                                                                           |
| record.unassign-others                   | This scope is to allow a user to unassign another user who is current assigned to the record                                                                                                                                                                    |
| record.review-duplicates                 | This scope allows a user to review declarations that have been flagged as a potential duplicate                                                                                                                                                                 |
| record.register                          | This scope allows a user to register a record. Record will have the status 'Registered'                                                                                                                                                                         |
| record.registered.print-certified-copies | This scope allows a user to print a certified copy and issue                                                                                                                                                                                                    |
| record.registered.request-correction     | This scope allows a user to request a correction to a record                                                                                                                                                                                                    |
| record.registered.correct                | This scope allows a user to correct a record and review correction requests                                                                                                                                                                                     |
| record.read                              | This scopes allows a user to view a record data                                                                                                                                                                                                                 |
| search                                   | This scope allows a user to search for record and view summary information                                                                                                                                                                                      |
| workqueue                                | This scopes defines what workqueues they see                                                                                                                                                                                                                    |
| profile.electronic-signature             | This scopes allows a user to add and update their electronic signature                                                                                                                                                                                          |
| performance.read                         | This scope allows a user to view metabase peformance dashboards                                                                                                                                                                                                 |
| config.update:all                        | This scope allows the user access to configurations options                                                                                                                                                                                                     |
| organisation.read-locations              | <p>This scope allows a user to view the Organisation, My Team menu tabs and view all locations<br>:all - view all office team pages<br>:my-jurisdiction - only view office teams pages in your jurisdiction<br>:my-office - only view your office team page</p> |
| user.create                              | <p>This scope allows a user to create a new user<br>- role - role typers the user can create<br>:all - any user<br>:my-jurisdiction - only users in the users jurisdiction</p>                                                                                  |
| user.edit                                | <p>This scope defines what user roles you can edit<br>- role - role typers the user can create</p>                                                                                                                                                              |
| user.update                              | <p>This scopes defines what user a user can update<br>all - any user<br>- :my-jurisdiction - only users in the users jurisdiction</p>                                                                                                                           |
| user.read                                | <p>This scope allows a user to view a user's profile<br>- :all - audit any user<br>- :my-office - only audit users in their office<br>- :my-jurisdiction - only audit users in their jurisdiction<br>- :only-my-audit - user can only view their audit</p>      |

{% hint style="info" %}
**How to configure user roles & scopes?**\
Learn how to define and assign appropriate permissions to different user roles in your system. [3.2 Mapping offices and user types](/v1.9/setup/2.-gather-requirements/3.2-mapping-offices-and-user-types.md)
{% endhint %}

{% hint style="info" %}
**User roles & scopes in Farajaland?**\
Learn how we mapped user roles and scopes to support and improve service delivery in Farajaland [User roles](/v1.9/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md)
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/product-specifications/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
