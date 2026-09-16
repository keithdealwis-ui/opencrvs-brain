---
title: "Administrative hierarchy"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:bba7d0705a9c1c2627f3ad11ac4bbb31bb0f0c20d8fd0c6b912fade2130772b1"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy.md).

# Administrative hierarchy

**TL;DR**

1. A country consists of a hierarchy of administrative areas and associated office and facility locations.
2. The hierarchy structure is defined per country.
3. Not every level of the hierarchy needs to appear in every branch of the hierarchy tree (e.g. Province → Village).
4. Any level of the hierarchy may contain physical locations (e.g. hospitals, offices).
5. Each user must be assigned to a physical location.
6. Each user can belong to only one location.
7. Each location has a UUI associated, created during data seeding.
8. After going live, locations must be [managed via APIs](/technical/guides/configuration/integrations/integration-location-management.md).

### Introduction

\
In OpenCRVS, a country consists of a hierarchy of administrative areas. Administrative areas (such as provinces, districts, counties, cities, or villages) contain locations (such as CRVS offices, health facilities, or police stations). Locations serve two purposes: 1) as an identifiable place where events occur, and 2) as a place users are assigned to.<br>

The administrative hierarchy models a country's jurisdictional structure. A user's location in the hierarchy determines what they can see and do in the system.

**Example 1. Simple administrative hierarchy – Country -> Province -> District -> Village**

\
![](https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-f42cbc0b4a34846a3eb783c442e334c1e16eeb7c%2FScreenshot%202026-05-06%20at%2012.05.28.png?alt=media)<br>

In this example of a 3-level hierarchy, each administrative area contains physical location(s), and each location has one or more users assigned to it. User jurisdiction is based on [scopes](/technical/guides/configuration/users/roles-and-scopes.md) given to their role.

Administrative areas form a hierarchy independently of locations. District A is the parent of Village A. Locations belong to administrative areas but do not have their own hierarchy — District Office A is not a parent of Village Office A.\
\
If all roles have actions limited to their `administrativeArea` then:

1. The Registrar General at HQ can perform actions across the entire country — Country, Province, District, and Village.
2. The Provincial Registrar at the Provincial Office can perform actions within Province A, District A, and Village A.
3. The Registrar at the District Office can perform actions within District A and Village A.
4. The Community Leader at the Village Office can perform actions within Village A.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/administrative-hierarchy.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
