---
title: "Releases"
source_url: "https://documentation.opencrvs.org/v1.5/general/releases"
markdown_url: "https://documentation.opencrvs.org/v1.5/general/releases.md"
version: "v1.5"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:513e0af8f4f12330b537a9249428ecfe5a5e00c41640ccb926a3b5dc051cd63b"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.5/general/releases.md).

# Releases

### **OpenCRVS Release Calendar**

The OpenCRVS Core team issue product releases once every 4 months with each release receiving 6 months of bug fix (hotfix) support.

<figure><img src="https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/4XlmumEa1IvsiOP6Oxc7/opencrvs-release-calendar.png" alt=""><figcaption></figcaption></figure>

### **OpenCRVS Semantic Versioning**

| Version label                | Version number              | Description                                                                                                                                                                                                                                                                    | QA strategy                                                                                                                                                                                                                                                              | Frequency      | Supported for                |
| ---------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ---------------------------- |
| Core: Major (breaking)       | n.0.0 (e.g. 2.0.0)          | <p>Major architectural redesign, including significant functional and design changes.<br>Impacts Core + Country Resource Package + Infrastructure release.</p>                                                                                                                 | <p>Creation of new test cases for new functionality.<br>Complete regression test.<br>Most likely new test data generator.<br>Data migration testing.<br>End-to-end testing (Cypress).</p>                                                                                |                |                              |
| Core: Minor (breaking)       | x.n.0 (breaking) e.g. 1.2.0 | Introduces new changes which are not backward-compatible. These changes can be process related or technical.                                                                                                                                                                   | <p>Creation of new test cases for new functionality.<br>Complete regression test.<br>Possibly changes to test data generator.<br>Data migration testing.<br>End-to-end testing (Cypress).</p>                                                                            | Every 4 months | Duration of 2 minor versions |
| Core: Minor (non-breaking)   | x.n.0 (e.g. 1.2.0)          | Introduces new backwards compatible functionality. May include data structure or other changes that are automatically migrated. SIs can safely upgrade their system to this version without implementation changes in integrations or country configuration.                   | <p>Creation of new test cases for new functionality.<br>Regression test pack to be defined.<br>Potential changes to test data generator.<br>End-to-end testing (Cypress).</p>                                                                                            | Every 4 months | Duration of 2 minor versions |
| Core: Hotfix                 | x.x.n (e.g. 1.2.1)          | Bug fixes or minor internal changes such as performance optimisations. Developed in parallel with a Minor Release (which requires the same fixes applied).                                                                                                                     | <p>Specific tests to QA the defects.<br>Small regression / smoke-test to ensure nothing impacted.<br>End-to-end testing (Cypress).</p>                                                                                                                                   | Bi-weekly      | N/A                          |
| Dependant software component | x.x.0-n (e.g. 1.2.0-1)      | Includes country resource packages, integrations, data generators etc. indicating the core release with which they are compatible, including a patch suffix. Releases are otherwise independent of core releases and changes to these components do not affect core releasing. | <p>Specific tests to QA the defects.<br>Small regression / smoke-test to ensure nothing impacted.<br><br>In the case of Farajaland, latest compatible version is always deployed in conjunction with the core version being tested.<br>End-to-end testing (Cypress).</p> | N/A            | N/A                          |

### **OpenCRVS Gitflow and "Quality Gates"**

We follow the "[Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)" branching model with a "Quality Gate" concept (which defines specific quality assurance flows for features, beta releases, stable releases and hotfixes). It is imperative that implementers understand the concept of "Gitflow" when either contributing to core or merging in updates from the Farajaland country configuration package.

<figure><img src="https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/AVepINLDcZ3HtVLB7eCc/opencrvs-gitflow.png" alt=""><figcaption><p>OpenCRVS Gitflow</p></figcaption></figure>

Referring to the Gitflow and Quality Gate diagrams, you should be able to understand the following:

A "stable" release has undergone not only automated testing but manual regression testing.

A "beta" release has only undergone automated testing

Any git hash tagged Dockerhub image is a new "feature" that has been recently merged into the active and unstable develop branch. These images are not in an official beta or stable release but available to experimenters and the core development team nonetheless.

OWASP security penetration tests by a CREST certified 3rd party occur once every 12 months or on every major release.

<figure><img src="https://content.gitbook.com/content/l7Cjlh2y2hlCBlt6R76C/blobs/E3AzZXFH1ejGg1QzFDmO/opencrvs-release-qa.png" alt=""><figcaption><p>OpenCRVS Quality Gates</p></figcaption></figure>

### **OpenCRVS Upgrade Process**

The following video demonstrates the process of upgrading OpenCRVS using a real-world example where a country is upgrading a non-breaking hotfix release version.

{% embed url="<https://youtu.be/fqc12Qx3eyg>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.5/general/releases.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
