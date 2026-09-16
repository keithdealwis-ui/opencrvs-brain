---
title: "Guide: Certificate configuration"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-certificate-configuration"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-certificate-configuration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:26fed3f8c617e6acb2122b17b42b28b0a555b28b75e1cd30266073fa5d53b0f4"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-certificate-configuration.md).

# Guide: Certificate configuration

### 1. Introduction

This page provides **design guidelines** for certificate and certified copy templates in OpenCRVS. It focuses only on how to design a good, digital‑first certificate layout.

Use these guidelines when you are:

* Designing a new certificate or extract template.
* Redesigning a legacy paper certificate for use with OpenCRVS.
* Reviewing certificate layouts before they are exported to SVG and configured.

For how certificates work as a feature (templates, printing, workflows), see the parent **Certificates** page.

***

### 2. Digital‑first layout principles

#### 2.1 Rethink legacy certificates

Implementing a digital CRVS system is an opportunity to **simplify and modernise** certificate layouts.

* Treat the **digital registry as the source of truth**; the paper certificate is a view of that data.
* Remove elements that only exist to guide handwriting (for example, dotted lines and boxes).
* Avoid trying to mimic very flexible handwritten spaces; instead, design fixed areas that work well for typical values.
* If the existing certificate was created in tools like **Microsoft Word**, plan to **recreate** it in a proper design tool rather than importing it directly.

Aim for a clean, official design that is easy to read and easy to configure.

#### 2.2 Visual hierarchy

Make it easy for someone to quickly verify the certificate.

* Start with a clear **title** (for example, "Birth Certificate").
* Surface key identifiers prominently (for example, registration number, UIN, date of registration).
* Group related information:
  * Event details (date, place, type).
  * Person details (for example, child / deceased / spouses).
  * Parents or informant details.
  * Registration and issuing details.
* Use headings, spacing, and subtle lines to separate sections.

#### 2.3 Page size and orientation

* Prefer **A4** or **A5** so that printing and preview behave consistently.
* Choose portrait or landscape based on legal expectations and content density.
* If you need multiple pages, design them together so that margins, headings, and section ordering are consistent.<br>

OpenCRVS also supports **multi-page certificates**. This is achieved by configuring the SVG template so that it defines multiple pages within a single design (for example, by setting explicit page dimensions and adding additional page frames or artboards). At a high level, implementers:

* Design the full certificate layout across the required number of pages.
* Mark where each page should start and end inside the SVG (using separate layers, groups, or artboards, depending on the design tool).
* Place each data field once in the correct position on the relevant page.

When the template is rendered, OpenCRVS interprets this configuration, splits the SVG into multiple pages, and exports them as a multi-page PDF ready for printing.

***

### 3. Text, fonts, and readability

#### 3.1 Font choice

* Use clear, legible fonts suitable for official documents.
* Avoid overly decorative typefaces except in small areas (for example, headings or seals).
* Ensure fonts support all required character sets and languages.

#### 3.2 Font size

* Use **at least 12pt** for key data.
* Reserve smaller sizes only for secondary information (for example, footnotes or references).
* Use larger sizes for the certificate title and major section headings.

#### 3.3 Long names and text

Design with the **worst case** in mind.

* Consider the longest realistic names, places, or addresses that might appear.
* Prefer layouts where most fields can fit on a single line.
* If text must wrap, ensure there is enough vertical space and that wrapping will not collide with other fields or graphics.
* Avoid squeezing text tightly around seals, logos, or borders.

#### 3.4 Language and labels

* Use clear, unambiguous labels that match legal terminology.
* If multiple languages are required, decide whether to:
  * Show both languages inline (for example, label and value shown twice), or
  * Provide separate template variants per language.
* Keep wording concise so that labels do not dominate the layout.

***

### 4. Use of graphics, security elements, and images

#### 4.1 Security paper

If you print onto **pre‑printed security paper**:

* Add the security paper design to your svg template certificate design so it shows in preview. Add << >> to exclude it in export to pdf.
* Align text, seals, and signatures to the fixed elements of the security paper.
* Keep margins consistent so that printing aligns reliably across different printers.

#### 4.2 Logos, seals, and emblems

* Use high‑resolution **PNG** or SVG for logos and seals.
* Place key symbols (for example, coat of arms, ministry logo) prominently but without overwhelming the text.
* Ensure there is strong contrast between any overlaid text and the background.

#### 4.3 Digital signatures

* Reserve a clear area for each **digital signature** and printed name.
* Choose a consistent aspect ratio (for example, **2:1** width to height) for signature boxes.
* Leave enough white space around the signature so it remains legible when printed.

#### 4.4 Verification QR code

* Reserve a **square** area (1:1 aspect ratio) for the verification QR code.
* Place it where it is easy to scan but does not dominate the design (for example, bottom corner).
* Keep a quiet zone (clear space) around the code so scanners can read it reliably.

***

### 5. Practical tips for working in design tools

#### 5.1 Use realistic dummy data

* Populate the layout with realistic example values (long names, complex addresses, long place names).
* Check that the layout still looks good with this dummy data.

#### 5.2 Layers and grouping

* Use **layers and groups** to separate background graphics, section headings, labels, and data areas.
* Name groups meaningfully (for example, "Child details", "Registration block") to make later configuration easier.

#### 5.3 Alignment and spacing

* Use consistent margins and alignment (for example, align all labels in a column).
* Use baseline grids or layout grids in your design tool to keep spacing tidy.
* Avoid placing important text too close to page edges where printers may clip.

#### 5.4 Preparing for SVG export

Although configuration happens later, some export‑related choices affect design:

* Avoid effects that do not export cleanly to SVG (for example, complex shadows or raster effects).
* Keep the number of fonts and weights manageable.
* Ensure any text that will later be replaced by data remains as editable text (not outlines).

***

### 6. Review checklist

Before handing a design over for SVG export and configuration, check:

* \[ ] All legally required fields are present and clearly labelled.
* \[ ] The layout is readable with long names and addresses.
* \[ ] Font sizes meet accessibility and legibility expectations.
* \[ ] Logos, seals, and security elements are clear and not obstructing data.
* \[ ] Signature and QR code areas are well placed and have enough space.
* \[ ] The design works in black‑and‑white printing if colour printers are not guaranteed.
* \[ ] The page size, orientation, and margins are agreed with the implementation team.

If the design passes this checklist, it is ready to be exported to SVG and configured as a certificate template in OpenCRVS.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-certificate-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
