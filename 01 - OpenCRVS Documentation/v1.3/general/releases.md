---
title: "Releases"
source_url: "https://documentation.opencrvs.org/v1.3/general/releases"
markdown_url: "https://documentation.opencrvs.org/v1.3/general/releases.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:64aaad40d68348bb327044fd61c5a4539ec32b8893bfa65ee739eed028d46e76"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/general/releases.md).

# Releases

### **OpenCRVS Release Process & Calendar**

The following release process commences with the v1.1.0 release. You can read more about how we developed our release process, branching model and quality gates in this [blog post](https://www.opencrvs.org/resources/connect/blog/release-management-as-a-digital-public-good-what-we-have-learnt-so-far).

The OpenCRVS Core team issue product releases once every 4 months with each release receiving 6 months of bug fix (hotfix) support.

<figure><img src="https://1176971301-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6qn2vAsiooyRnf055REr%2Fuploads%2F2POlu6Ha1mbTO2JHxzhA%2Fopencrvs-release-calendar.png?alt=media&amp;token=b67e3347-b2d0-44db-97db-4e628e1aca30" alt=""><figcaption></figcaption></figure>

### **OpenCRVS Semantic Versioning**

As a digital public good we are aware that implementers may only periodically perform upgrades. It is not sustainable for us or our community to follow the strict interpretation of semantic versioning in our full-stack microservice application, where every new feature would have a dedicated minor release. Our interpretation of semantic versioning for our project should therefore be interpreted is as follows.

1. MAJOR version when we make major architectural or design changes that are not backwards compatible and without automated migrations.
2. MINOR version when we introduce backwards compatible functionality. We may also introduce automated migration scripts and migration notes to cater for any non backwards compatible features in minor releases.
3. PATCH version when we introduce backwards compatible bug fixes

Additional labels for "stable" and "beta" metadata are available as extensions to the MAJOR.MINOR.PATCH format. E.G. **v1.1.0-stable**

### **OpenCRVS Gitflow and "Quality Gates"**

We follow the "[Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)" branching model with a "Quality Gate" concept (which defines specific quality assurance flows for features, beta releases, stable releases and hotfixes). It is imperative that implementers understand the concept of "Gitflow" when either contributing to core or merging in updates from the Farajaland country configuration package.

<figure><img src="https://1176971301-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6qn2vAsiooyRnf055REr%2Fuploads%2FjdmMj5pn0VkY5eW5vadE%2Fopencrvs-gitflow.png?alt=media&amp;token=b6597f60-4724-425c-80f7-340ea6a2097b" alt=""><figcaption><p>OpenCRVS Gitflow</p></figcaption></figure>

Referring to the Gitflow and Quality Gate diagrams, you should be able to understand the following:

A "stable" release has undergone not only automated testing but manual regression testing.

A "beta" release has only undergone automated testing

Any git hash tagged Dockerhub image is a new "feature" that has been recently merged into the active and unstable develop branch. These images are not in an official beta or stable release but available to experimenters and the core development team nonetheless.

OWASP security penetration tests by a CREST certified 3rd party occur once every 12 months or on every major release.

<figure><img src="https://1176971301-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6qn2vAsiooyRnf055REr%2Fuploads%2F7xlLITpHG2PGle4ruN5F%2Fopencrvs-release-qa.png?alt=media&amp;token=94854472-6381-4a62-b9d2-fe28c9e47840" alt=""><figcaption><p>OpenCRVS Quality Gates</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/general/releases.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
