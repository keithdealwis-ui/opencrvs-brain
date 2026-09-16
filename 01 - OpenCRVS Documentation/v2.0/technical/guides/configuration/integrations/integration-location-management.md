---
title: "Integration: Location management"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-location-management"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-location-management.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:74bff8e684587eeca96b2f150088fdedf297506b04e10461d43f4ff00a8bcc14"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-location-management.md).

# Integration: Location management

#### Introduction

Location data is one of the most critical reference datasets in OpenCRVS. Every office, health facility, and administrative area is assigned a **permanent UUID (Universally Unique Identifier)** that is used internally throughout the platform.

These UUIDs are not simply identifiers for display purposes—they form the basis of how OpenCRVS routes events, stores addresses, integrates with external systems, and preserves the integrity of historical records.

For this reason, careful planning and governance of location data is essential before a country goes live.

***

#### How locations are used

Location UUIDs are used throughout OpenCRVS to identify where events occur and where they should be processed.

Typical examples include:

* Routing declarations received from external systems to the correct registration office.
* Identifying the correct health facility when recording a place of birth or death.
* Recording residential addresses using the country's administrative hierarchy.
* Associating historical events with the office responsible for processing them.
* Supporting reporting and statistics based on geographic areas.

Because integrations rely on UUIDs rather than names, location names can change over time without affecting external systems or existing records.

***

#### Administrative hierarchies

Administrative areas are organised into a hierarchy (for example, Province → District → Ward → Village).

When individual addresses are returned from the Search API, they contain an **`administrativeAreaId`**, which identifies the **leaf-level administrative area** associated with the address.

Each administrative area also stores a **`parent_id`**, allowing applications to navigate from the leaf node back through the hierarchy to determine the complete administrative path.

This hierarchical structure enables reporting, searching, and integration without storing the full address hierarchy on every record.

***

#### Data seeding

All locations and their associated UUIDs are created during the initial **data seeding** process.

Once seeded, these UUIDs become permanent identifiers that are referenced throughout the system.

As registrations are created, every event becomes associated with one or more location UUIDs, such as:

* Registration office
* Health facility
* Administrative area of residence

These relationships remain with the event for its lifetime.

***

#### Why locations cannot be re-seeded

After a country has gone live, **the location dataset must not be re-seeded**.

Re-seeding would generate new UUIDs, breaking the relationships between existing events and their associated locations. Historical records would no longer correctly reference the offices, facilities, or administrative areas in which they were originally registered.

For this reason, location data should be considered **persistent reference data** once production use has begun.

***

#### Managing locations after go-live

Changes to location data after go-live must be performed using the OpenCRVS APIs rather than by re-running the seed process.

Supported operations include:

* Adding new administrative areas
* Adding new registration offices
* Adding new health facilities
* Updating location names
* Deactivating existing locations

Using the APIs preserves existing UUIDs while allowing the location hierarchy to evolve over time.

***

#### Deactivating locations

Locations can be deactivated using the available APIs. However, this should be undertaken with extreme caution.

Deactivated locations are no longer visible within OpenCRVS, but historical events will continue to reference the UUID of the original location.

If records need to be reassigned to a different office or administrative area, this cannot be achieved simply by deactivating a location. A **custom data migration** must be developed to update all affected historical records so that they reference the new location UUID.

Such migrations should be carefully planned, tested, and executed to preserve data integrity.

***

#### Best practices

To minimise future maintenance and avoid complex data migrations:

* Design the administrative hierarchy carefully before go-live.
* Confirm registration office and health facility structures with stakeholders.
* Avoid deleting or replacing locations after production deployment.
* Use the APIs to add or update locations while preserving existing UUIDs.
* Carefully assess the impact of deactivating any location that has historical records.

***

#### Future enhancements

OpenCRVS includes a roadmap item to support **time-aware management of administrative hierarchies**, allowing administrative boundary changes and organisational restructuring to be managed without requiring manual migration of historical data.

Until this capability is available, countries should treat production location data as long-lived reference data and manage changes through the supported APIs and carefully planned migration activities where necessary.

***

#### APIs

* [Locations](https://documentation.opencrvs.org/technical/apis/core-apis/locations)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-location-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
