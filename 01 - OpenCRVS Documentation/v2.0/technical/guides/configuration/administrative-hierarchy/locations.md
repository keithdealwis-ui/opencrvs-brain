---
title: "Locations"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/locations"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/locations.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c071a40f3ab7402931b1b5f95cbe5210638393626266b1c4cf9dcc12f76276c4"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/locations.md).

# Locations

Unlike administrative areas, a location refers to a more specific point. Usually, a location is a physical place such as an office, health facility, or police station.

Locations serve two purposes:

* A precise, identifiable place where an event occurs (e.g. a mother gave birth at Ezhi District Hospital).
* A place of assignment for staff (e.g. Kunda Simbaya, Registration Agent, works at Irundu District Office).

Locations are configured within the administrative hierarchy. Learn how locations affect [roles, scopes and jurisidictions](https://app.gitbook.com/o/zub8C4BetmW3a9Bj4Cd4/s/TIJguU5Pzi7HeHrkXa4I/~/edit/~/changes/126/technical/guides/configuration/users/roles-and-scopes)

Example 1: Simple, populated administrative hierarchy

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-d70451323f02f50c6cdf5d925facfb7e1c6b9fdb%2FScreenshot%202026-05-11%20at%2014.00.46.png?alt=media" alt=""><figcaption></figcaption></figure>

Locations sit within administrative areas.

* An administrative area may have zero or more locations.
* A location may have zero or more users.

Example 2: Locations directly under country

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-98b5be76e6a4a84149f702b30642f8a5d005bb3e%2FScreenshot%202026-05-11%20at%2014.04.37.png?alt=media" alt=""><figcaption></figcaption></figure>

Locations can be placed directly under a country, without belonging to any administrative area.

Unless restricted, users assigned to locations directly under a country have jurisdiction over the entire country.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy/locations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
