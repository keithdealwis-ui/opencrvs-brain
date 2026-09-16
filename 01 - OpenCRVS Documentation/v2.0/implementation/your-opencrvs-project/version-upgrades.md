---
title: "Version upgrades"
source_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/version-upgrades"
markdown_url: "https://documentation.opencrvs.org/implementation/your-opencrvs-project/version-upgrades.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e63a18a688b4c1d6a31b55d2b4445f61e083202338f73ef01e3eeaa4d127b714"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/implementation/your-opencrvs-project/version-upgrades.md).

# Version upgrades

### 1. Introduction

Keeping OpenCRVS up to date ensures that your system remains secure, reliable and supported. Regular upgrades allow you to benefit from bug fixes, security patches, performance improvements and new functionality as the OpenCRVS platform evolves.

This page provides a high-level overview of why regular upgrades are important and how to plan them. The detailed technical procedures for upgrading OpenCRVS are covered in the [version upgrade](/technical/guides/version-upgrades.md) guides.

**Where this sits:** Maintaining your OpenCRVS deployment is an ongoing operational activity that begins after Go-live and continues throughout the lifetime of the system.

***

### 2. Why regular upgrades matter

OpenCRVS is actively developed and improved. Each release may include:

* Security updates and hotfixes
* Bug fixes and performance improvements
* New features and capabilities
* Improvements to existing functionality
* Platform and dependency updates

Regular upgrades help ensure that your implementation continues to benefit from these improvements while remaining compatible with the supported OpenCRVS platform.

**Don't wait too long between upgrades.** The further an implementation falls behind, the more complex and time-consuming future upgrades become. Keeping pace with releases makes maintenance simpler and reduces operational risk.

***

### 3. How upgrades are managed

OpenCRVS follows a regular release process. Before planning an upgrade, review the release notes to understand what has changed and whether any preparation is required.

At a high level, upgrading OpenCRVS consists of:

**Monitor new releases** — review each OpenCRVS release to understand new features, bug fixes and any actions required for your implementation.

**Plan the upgrade** — assess the changes, determine an appropriate upgrade window and identify any testing that will be required before deploying to production.

**Test before production** — apply the upgrade to a non-production environment first (QA and staging) and verify that your country configuration, integrations and business processes continue to work as expected.

**Deploy to production** — once validated, deploy the upgrade to the production environment using the documented upgrade procedures.

***

### 4. Stay informed

To plan upgrades effectively, implementation teams should stay informed about the OpenCRVS roadmap and upcoming releases.

We recommend that Technical System Administrators and implementation teams:

* follow OpenCRVS communications and release announcements
* attend community webinars and product update sessions
* review the published release notes for every new version
* monitor the OpenCRVS GitHub Releases page for newly published versions

Understanding what is coming allows you to plan upgrades alongside your normal operational activities, rather than reacting only when support ends.

***

### 5. Supported versions

OpenCRVS officially maintains support for the current minor release and the immediately preceding minor release.

For example, if the current release is **2.0**, the supported versions are:

* **2.0** (current)
* **1.9** (previous minor release)

Older minor versions are no longer actively maintained and will not receive new hotfixes or security updates.

Keeping your implementation within the supported release window is essential to ensure you continue to receive maintenance updates and can obtain support from the OpenCRVS community.

***

### 6. When your system is up to date

Your implementation is being maintained effectively when:

* you regularly review new OpenCRVS releases
* upgrades are planned as part of normal operational maintenance
* new versions are tested before deployment to production
* your production system remains within the supported release window
* implementation teams stay informed through OpenCRVS communications and community updates

***

### 7. Resources and support

The [version upgrade guides](/technical/guides/version-upgrades.md) provide detailed instructions for upgrading OpenCRVS between supported releases.

To stay informed about upcoming changes:

* Follow OpenCRVS product communications and community webinars.
* Review the published roadmap and release announcements.
* Monitor the GitHub Releases page for every new OpenCRVS release: <https://github.com/opencrvs/opencrvs-core/releases>.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/implementation/your-opencrvs-project/version-upgrades.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
