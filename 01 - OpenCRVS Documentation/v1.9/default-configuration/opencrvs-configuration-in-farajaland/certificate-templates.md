---
title: "Certified Copies templates"
source_url: "https://documentation.opencrvs.org/v1.9/default-configuration/opencrvs-configuration-in-farajaland/certificate-templates"
markdown_url: "https://documentation.opencrvs.org/v1.9/default-configuration/opencrvs-configuration-in-farajaland/certificate-templates.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e739798d729f40c7731f65c9604fe7738f008c03159b5b2c351158d350e03e03"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/default-configuration/opencrvs-configuration-in-farajaland/certificate-templates.md).

# Certified Copies templates

The following certified copies templates have been configured to support the business requirments of Farajaland.

Two types of certified copies have been configured:

* **Certificate**
  * Issued upon registration
  * Short form version of the digital record
  * Fee: Free
* **Certified Copy**
  * Can be request after the certificate has been issued.
  * Long form version of the digital record
  * Fee: $10

### Birth certificate

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-ae6a71696d37e69ebeec70dba39369deef58fb71%2FFarajaland-birth-certificate-v2.png?alt=media" alt=""><figcaption></figcaption></figure>

### Death certificate

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-d49b5a3179c29471cdd8bdd7e177bdb8771177df%2FFarajaland-death-certificate-v2.png?alt=media" alt=""><figcaption></figcaption></figure>

### Marriage certificate

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-4daa256ec68f82ae62f07b1ca5e0c76f86cc5df3%2FFarajaland-marriage-certificate-v2.png?alt=media" alt=""><figcaption></figcaption></figure>

In the **Country Configuration Files** in the [Release Notes](https://github.com/opencrvs/documentation/tree/master/v1.9.0/general/v1.8-release-notes) you will find the svgs created for Farajaland certified copies


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/default-configuration/opencrvs-configuration-in-farajaland/certificate-templates.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
