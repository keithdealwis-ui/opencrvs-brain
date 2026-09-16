---
title: "Guide: Form configuration"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-form-configuration"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-form-configuration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:728f1c4e3adf227e522de3df8fdf4fde73751629e40c610d361395509e459acc"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-form-configuration.md).

# Guide: Form configuration

Designing good forms in OpenCRVS helps users complete registrations quickly and ensures that high‑quality data is captured at source. Use the guidelines below when designing or reviewing any form.

#### 1. Be clear why you are capturing each data point

For every input, ask: **Why do we need this?**

* Is it required to complete the registration workflow?
* Is it only needed for statistics or reporting?
* How will it appear in dashboards, exports, or vital statistics reports?

If you cannot explain how a field will be used, strongly question whether it should be on the form at all.

#### 2. Organise questions into focused pages

Keep users focused on one topic at a time by grouping fields into **pages** such as:

* Child details
* Mother details
* Father details
* Informant details
* Event details (birth / death / marriage)

Use **conditional logic** to show or hide whole pages when they are only relevant in some scenarios. For example, only show "Father details" if the user confirms that the father is legally recognised in the registration.

#### 3. Use conditional fields to simplify the experience

Make the form feel smart by only showing fields when they are genuinely needed.

Examples:

* Show the **Medically Certified Cause of Death** inputs only when the user confirms that a medical practitioner has established the cause of death.
* Ask for **facility details** only when the place of occurrence is a health facility.
* Reveal **late registration justification** fields only when the declaration is beyond a configured time limit.

Always ask yourself: *What can the system infer from existing answers so that the user does not have to think about it or see irrelevant fields?*

#### 4. Reuse and copy data so users do not type it twice

Look for opportunities to re‑use information already captured.

Examples:

* If the **informant is the mother**, copy the mother’s name and contact details into the informant section automatically.
* If the **mother and father share the same address**, provide a checkbox such as "Same address as mother" that copies the address fields in the background.
* If the **declaration location** is the same as the **place of occurrence**, provide an option to copy that address instead of re‑entering it.

Use conditional checkboxes and selects to trigger this copying behind the scenes so the user experiences fewer fields and less typing.

#### 5. Prefer selects and reference lists for statistical data

Where possible, avoid free‑text inputs for values that need to be analysed.

Use **select** fields backed by well‑defined reference lists for things like:

* Occupation
* Birth attendant type
* Place of occurrence
* Cause of death groupings
* Registration channel (facility, field agent, office, etc.)

Free‑text answers quickly lead to inconsistent, messy data that is hard to aggregate and compare. Define and maintain a controlled list of options instead.

#### 6. Validate entries to protect data quality

For any free‑text or numeric field, define **validation rules** to catch obvious errors at the point of entry.

Questions to ask:

* Can this **date** be in the future?
* What is the **minimum and maximum** time between the child’s date of birth and the mother’s date of birth?
* What is the realistic **range for weight at birth**?
* Are there formats we should enforce (for example, phone numbers, national IDs, certificate numbers)?

Apply validation rules that are strict enough to prevent bad data, but not so strict that valid real‑world cases are blocked.

#### 7. Separate registration data from supporting documents

Keep the electronic declaration form focused on the **data needed for registration**. Anything that functions as evidence or proof should usually be uploaded as a **supporting document**, not captured as extra fields.

Examples:

* Proof of birth or death certificates signed by a health professional
* Medically certified cause‑of‑death forms
* Attestation letters from community leaders

If, for example, the signature of the birth attendant is required on a legacy paper form, consider designing a dedicated **proof of birth** template that is uploaded as a supporting document instead of recreating the whole paper form in the digital declaration.

#### 8. Minimise cognitive load and reading effort

Beyond the individual fields, review the overall experience:

* Use **simple, direct labels** and help text that frontline staff can easily understand.
* Avoid long paragraphs inside the form; prefer short hints or tooltips.
* Keep related fields close together and in a logical order that matches how the informant tells their story.
* Remove any questions that are not strictly needed or that duplicate information captured elsewhere.

#### 9. Test with real users and iterate

Before finalising a form configuration:

* Run through sample scenarios with registrars and health workers.
* Ask them where they hesitate, guess, or feel that information is being requested twice.
* Capture their feedback and adjust pages, conditional logic, wording, and validation rules accordingly.

Forms should evolve as policies and practices change. Treat this guidance as a living checklist that you revisit whenever you add new data points or re‑design a workflow.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/gathering-requirements/design-and-specification/guides/guide-form-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
