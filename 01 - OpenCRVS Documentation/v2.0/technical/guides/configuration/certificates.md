---
title: "Certificates"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/certificates"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/certificates.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:88a2b553f879045530a465f1f79c35a1ea8969801d00d8b60295086001c2d305"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/certificates.md).

# Certificates

Configuring your printable PDF documents

Certificates in OpenCRVS are printable PDF documents generated from registered event records. They are built from SVG templates that use Handlebars syntax — a familiar `{{expression}}` format — to pull in record data at print time. Core handles the rendering pipeline; everything else (which templates exist, what data they show, how they look) is configured in countryconfig.

The three topics below cover the building blocks you need to design and configure certificate templates:

* [**Built-in helpers and template variables**](/technical/guides/configuration/certificates/built-in-helpers-and-template-variables.md) — the data and helper functions that core makes available in every template out of the box.
* [**Custom Handlebars.js helpers**](/technical/guides/configuration/certificates/custom-handlebars.js-helpers.md) — how to write country-specific helper functions for formatting, translation, and logic that the built-in helpers don't cover.
* [**Multi-page certificate templates**](/technical/guides/configuration/certificates/multi-page-certificate-templates.md) — how to structure an SVG file that renders as multiple PDF pages.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/certificates.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
