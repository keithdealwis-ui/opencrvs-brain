---
title: "Contributing"
source_url: "https://documentation.opencrvs.org/v1.8/developer/contributing"
markdown_url: "https://documentation.opencrvs.org/v1.8/developer/contributing.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:28dd5d1204df861451542098ec721cc1dbbe7fa8d3c67a9b5846d04ad887d8d4"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/developer/contributing.md).

# Contributing

This documentation is intended for developers working daily as part of the OpenCRVS Core team, as well as external contributors who wish to contribute occasionally.

Here you’ll find documentation on our best practices, developer workflows, and the automation we use for feature development, bug fixing, and other day-to-day development tasks.

### Raising a bug or a feature request

1. Before opening a bug or feature request, use the search tool on the [Git issues page](https://github.com/opencrvs/opencrvs-core/issues) in opencrvs-core to see if the issue request already exists.
2. Open a Git Issue in opencrvs-core and complete the full template of choice if your request does not already exist.
3. Open a [Github discussion](https://github.com/opencrvs/opencrvs-core/discussions) and link to the Git Issue in your comments.  In the discussion, please explain a bit about who you are, the project you are working on, and maybe the country associated.  With this information, we can expedite urgent requests.

{% hint style="warning" %}
We are automatically notified in our Slack when a new Github Discussion is created, so this is a great way to get our attention.
{% endhint %}

### What happens next

During the following week after receiving your Github Discussion and request, we will prioritise it and get back to you. &#x20;

If the request is a legitimate bug in opencrvs-core and affects the core business processes of birth and death registration, we will deem it a **high priority** and get back to you with a resolution pathway within 1 week.

If the request is a bug in your configuration, our community will offer some advice when we have the capacity to do so. &#x20;

If your feature request is in our backlog, but not prioritised for an upcoming release, then we will get back to you as soon as we can with a potential design and development approach.

At your own pace you can submit a hotfix or feature response in a pull-request following the [process](/v1.8/developer/contributing/submitting-a-hotfix.md) defined on the next page.

{% hint style="warning" %}
OpenCRVS is a highly curated and secure government system that must support any of our implementation countries as a Digital Public Good.  Our design guidelines can be discussed between us based on research analysis and your country's unique requirements, but the OpenCRVS Core team's decision on approach will need to cater for every country's needs.  Our decision will be final.  If you want your submission to be accepted into an official release.  You can always fork OpenCRVS to deploy unsupported changes that are unique to your needs and bypass our security and quality gates.  OpenCRVS accepts no responsibility to help bug-fix any forked code.
{% endhint %}

Your pull request will need to have adequate test coverage.  We use a fake country configuration called Farajaland in order to write [playwright end-to-end](https://github.com/opencrvs/opencrvs-farajaland/tree/develop/e2e) tests.&#x20;

We will provisionally assign a release based on discussion with you when you commence development.  The release is confirmed when your pull-request is code reviewed and merged ready for UAT testing.  If code review is not completed before the "code freeze" deadline for a release, then your pull request will be moved to the next available release.

### Contribution Champions!

[68 developers](https://github.com/opencrvs/opencrvs-core/graphs/contributors) from our regular core maintaner community have contributed features to OpenCRVS over the years.

The following developers from our global community deserve extra special kudos for already contributing critical features to OpenCRVS following the process above. &#x20;

We are hugely grateful to you for your contributions.

> *Bug fixing and developing new features can be quite challenging, especially when you're new to OpenCRVS. Thankfully, the core team and other contributors are always there to guide you, offering ideas and recommendations to help you make it work. I’m grateful for the chance to learn and grow through open collaboration, and I’m looking forward to contributing more. -* [*Onion Quimson*](https://github.com/oni-on1003) *- Philippines*

| Github Profile                         | Country                                      | Feature                                        |
| -------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| <https://github.com/oni-on1003>        | Philippines                                  | New Form UI Components                         |
| <https://github.com/Eezi>              | Finland                                      | DevOps Optimisations                           |
| <https://github.com/ak-shanith>        | [Bevolv](https://www.bevolv.co/) - Sri Lanka | MOSIP Integration, Interoperability & Bugfixes |
| <https://github.com/anjana6>           | [Bevolv](https://www.bevolv.co/) - Sri Lanka | MOSIP Integration, Interoperability & Bugfixes |
| <https://github.com/PathumN99>         | [Bevolv](https://www.bevolv.co/) - Sri Lanka | MOSIP Integration, Interoperability & Bugfixes |
| <https://github.com/Hyper3x>           | [Bevolv](https://www.bevolv.co/) - Sri Lanka | MOSIP Integration, Interoperability & Bugfixes |
| <https://github.com/tharakadadigama20> | [Bevolv](https://www.bevolv.co/) - Sri Lanka | MOSIP Integration, Interoperability & Bugfixes |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/developer/contributing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
