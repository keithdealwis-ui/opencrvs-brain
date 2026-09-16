---
title: "User roles & scopes"
source_url: "https://documentation.opencrvs.org/v1.8/product-specifications/users"
markdown_url: "https://documentation.opencrvs.org/v1.8/product-specifications/users.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3bcde33ddda2fad455c432d3e22b7a8f0a2993d6fcec74dfdba757bd84a4d3ca"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/product-specifications/users.md).

# User roles & scopes

OpenCRVS supports the creation of multiple custom users with specific permissions (scopes) to control what they can and cannot do in the system. This feature allows countries to define user roles and their corresponding scopes based on their specific needs.

### Key Features

**Unlimited user role configuration**: Administrators can create and configure any number of system user roles.

**Custom role naming**: Each user role can have a custom name (e.g., *Healthcare Worker, Mayor, Registrar*).

**Scope-based permissions**: The functionalities available to each user role can be controlled by assigning specific scopes

### User Role Scopes

The following are the key scope categories available for configuration:

#### 1. Declare

• record.declare-birth – Allows a user to declare a birth.

• record.declare-death – Allows a user to declare a death.

• record.declare-marriage – Allows a user to declare a marriage.

• record.declaration-submit-incomplete – Allows a user to send incomplete declarations to an assigned office.

• record.declaration-submit-for-review – Allows a user to send complete declarations for review.

• record.declaration-submit-for-approval – Allows a user to send a declaration for approval.

#### 2. Validate

• record.declaration-submit-for-updates – Allows a user to send a declaration for updates (status: *Requires Updates*).

• record.declaration-archive – Allows a user to archive a declaration (status: *Archived*).

• record.declaration-reinstate – Allows a user to reinstate an archived declaration (reverting to the previous status).

• record.unassign-others – Allows a user to unassign another user currently assigned to the record.

• record.review-duplicates - Alloes a user to review a declaration flagged as a duplicate against the matching record/s

#### 3. Register

• record.register – Allows a user to register a record.

#### 4. Certify

• record.registration-print\&issue-certified-copies – Allows a user to print and issue a certified copy.

#### 5. Correct

• record.registration-request-correction – Allows a user to request a correction to a record.

• record.registration-correct – Allows a user to correct a record and review correction requests.

#### 6. Performance

• performance.read – Allows a user to view performance reports.

• performance.read-dashboards – Allows a user to view Metabase performance dashboards.

• performance.vital-statistics-export – Allows a user to export vital statistics to CSV.

#### 7. Search

• search.birth – Allows a user to search for all birth records.

• search.death – Allows a user to search for all death records.

• search.marriage – Allows a user to search for all marriage records.

• search.birth:my-jurisdiction – Allows a user to search for birth records in their jurisdiction.

• search.death:my-jurisdiction – Allows a user to search for death records in their jurisdiction.

• search.marriage:my-jurisdiction – Allows a user to search for marriage records in their jurisdiction.

#### 8. Config

• config.update:all – Allows a user to update configuration settings.

#### 9. Organisation

• organisation.read-locations:all – Allows a user to view all locations in the organisation.

• organisation.read-locations:my-jurisdiction – Allows a user to view only locations in their jurisdiction.

• organisation.read-locations:my-office – Allows a user to only view their office’s information.

#### 10. User Management

• user.create:all – Allows a user to create a user in any location.

• user.create:my-jurisdiction – Allows a user to create a user only in their jurisdiction.

• user.update:all – Allows a user to update user details in any location.

• user.update:my-jurisdiction – Allows a user to update user details only in their jurisdiction.

• user.read:all – Allows a user to view any user’s audit page.

• user.read:my-jurisdiction – Allows a user to view audit pages only in their jurisdiction.

• user.read:my-office – Allows a user to view user audit pages in their office.

• user.read:only-my-audit – Allows a user to view only their own audit page.\\

{% hint style="info" %}
**How to configure user roles & scopes?**\
Learn how to define and assign appropriate permissions to different user roles in your system. [3.2 Mapping offices and user types](/v1.8/setup/2.-gather-requirements/3.2-mapping-offices-and-user-types.md)
{% endhint %}

{% hint style="info" %}
**User roles & scopes in Farajaland?**\
Learn how we mapped user roles and scopes to support and improve service delivery in Farajaland [User roles](/v1.8/default-configuration/opencrvs-configuration-in-farajaland/user-role-mapping.md)
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/product-specifications/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
