---
title: "Aggregated Data"
source_url: "https://documentation.opencrvs.org/functional/markdown/aggregated-data"
markdown_url: "https://documentation.opencrvs.org/functional/markdown/aggregated-data.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:57a255c1037c837328a6171858417395f4396893081192f1fbfe93099cc9a072"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/functional/markdown/aggregated-data.md).

# Aggregated Data

## Overview

As part of the **Functional Architecture**, the **Aggregate Data** section describes the aggregation and analytics module in OpenCRVS — how data from records and workflows is combined for reporting and statistics.

It is organised into the following modules:

* **Performance Views** — describes performance dashboards (for example, workload, timeliness, rejection rates, correction volumes) built using Metabase on top of aggregated data.
* **Vital Statistics Export** — explains how registered records are transformed into tabular exports and dashboards for vital statistics production and monitoring.
* **Person Centricity (backlog)** — shows how records can be linked around a person (for example, using UINs or probabilistic matching) to support person‑centric analytics and life‑course views.

Together, these modules describe how OpenCRVS data can be aggregated, visualised, and used for performance management and vital statistics, while keeping individual record data secure.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/functional/markdown/aggregated-data.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
