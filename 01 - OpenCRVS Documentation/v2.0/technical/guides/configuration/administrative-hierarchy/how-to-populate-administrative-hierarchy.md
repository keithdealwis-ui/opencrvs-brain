---
title: "How to populate administrative hierarchy"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-populate-administrative-hierarchy"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-populate-administrative-hierarchy.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e71c6a4e6028bc62e5823f6b6756fb51c3038138919b5eb6223a9113dfd41d34"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-populate-administrative-hierarchy.md).

# How to populate administrative hierarchy

## Populating administrative hierarchy

After completing all the following steps, you will be ready to seed administrative areas, locations, and users, and use them in event form fields.\ <br>

1. Specify the available administrative structures in [application configuration](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/api/application/application-config.ts)\
   \
   Specifying the available structures allows **events** to utilise administrative areas as configurable fields. Once you have specified the structure, configure translations for them in [client.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/translations/client.csv).
2. Define administrative areas in [administrative-areas.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/locations/source/administrative-areas.csv). Administrative areas form the core of your administrative hierarchy.<br>
3. Define locations in [locations.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/locations/source/locations.csv). Locations are more precise places where users are assigned and events may occur (e.g. hospitals). Since locations reference administrative areas, they must be seeded after them.<br>
4. Define user roles in [roles.ts](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/roles/roles.ts). Each user must have a role and location.<br>
5. Define users. In development environments, test users are seeded from [default-employees.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/employees/source/default-employees.csv). In production, users are seeded from [prod-employees.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/release-v2.0.0/src/data-seeding/employees/source/prod-employees.csv). Seeding multiple users is not recommended in production environments.<br>

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/how-to-populate-administrative-hierarchy.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
