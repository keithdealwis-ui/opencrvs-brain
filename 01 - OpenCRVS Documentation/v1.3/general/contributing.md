---
title: "Contributing"
source_url: "https://documentation.opencrvs.org/v1.3/general/contributing"
markdown_url: "https://documentation.opencrvs.org/v1.3/general/contributing.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:fefe08aa00819a400a02243cf7799ffd8c9da092a896fae98a3f58dddb259b58"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/general/contributing.md).

# Contributing

How to contribute to the Digital Public Good for CRVS

The value of open-source products as digital public goods is that an active community of contributors will help to maintain and grow the product.

We need your support to ensure that every individual on the planet is recognised, protected and provided for from birth.

The [Open Source Guides](https://opensource.guide/) website has a collection of resources for individuals, communities, and companies who want to learn how to run and contribute to an open source project. Contributors and people new to open source will find the following guides especially useful:

* [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
* [Building Welcoming Communities](https://opensource.guide/building-community/)

#### Github Discussions <a href="#gitter" id="gitter"></a>

If you need to talk to us at any time regarding technical issues or feature ideas please refer to [Github Discussions](https://github.com/opencrvs/opencrvs-core/discussions).&#x20;

### Our values <a href="#our-values" id="our-values"></a>

As you join the OpenCRVS community, we request that you collaborate in the spirit of our joint values.

#### **Better together**

> We know that the impact of our combined efforts is greater than any individual effort alone. That’s why we are passionate community builders, creating spaces where diverse opinions and voices come together too create smart solutions.
>
> We nurture meaningful partnerships built on mutual trust and friendship and grounded in a shared vision of the future.

#### **Open, always**

> We have an open attitude, ready to work on each new challenge with optimism and a fresh perspective.
>
> We are radically transparent, openly sharing our ideas, our designs, our tools, and our code.
>
> We are open-minded and curious. We actively listen to others then take action with integrity.

#### **Because we care**

> We work hard because we believe profoundly in our mission.&#x20;
>
> We care deeply about the quality of our product and its implementation, knowing that it will profoundly affect people’s lives.
>
> We act with purpose and determination because we know that time is running out to ensure we leave no one behind.

### Contributing to code <a href="#working-on-opencrvs-code" id="working-on-opencrvs-code"></a>

OpenCRVS uses [GitHub](https://github.com/opencrvs/opencrvs-core) as its source of truth. The core team will be working directly there. All changes will be public from the beginning. Please review the [contributing](https://github.com/opencrvs/opencrvs-core/blob/master/CONTRIBUTING.md) file, clone the repository and submit a pull request. The authors will review the code and merge it in if all is well. By contributing to the OpenCRVS code, you are conforming to the terms of the [license](https://www.opencrvs.org/license).

#### Reporting new issues <a href="#reporting-new-issues" id="reporting-new-issues"></a>

We use [GitHub Issues](https://github.com/opencrvs/opencrvs-core/issues) if you would like to raise a bug or propose a change or feature. If you just have a general topic of discussion, or would like some technical help, please chat with us on [Github Discussions](https://github.com/opencrvs/opencrvs-core/discussions).

#### Reporting bugs <a href="#reporting-bugs" id="reporting-bugs"></a>

We use [GitHub Issues](https://github.com/opencrvs/opencrvs-core/issues) for our public bugs. If you would like to report a problem, take a look around and see if someone already opened an issue about it, or chat with us on [Github Discussions](https://github.com/opencrvs/opencrvs-core/discussions). If you are certain this is a new, unreported bug, you can submit a bug report.

Take screenshots or record your screen. [Loom](https://www.loom.com/) is a great tool you can use to record a video and paste a link to it into your bug. Open a bug report on [Github](https://github.com/opencrvs/opencrvs-core/issues/new?assignees=\&labels=%F0%9F%91%B9Bug\&template=---bug.md\&title=) following the guidance.

#### Reporting security bugs <a href="#reporting-security-bugs" id="reporting-security-bugs"></a>

Make sure to include a detailed description of the bug. Open a bug report on [Github](https://github.com/opencrvs/opencrvs-core/issues/new?assignees=\&labels=%F0%9F%91%B9Bug\&template=---bug.md\&title=) following the guidance.

#### Proposing a change <a href="#proposing-a-change" id="proposing-a-change"></a>

If you would like to request a new feature or enhancement but are not yet thinking about opening a pull request, you ca&#x6E;**:**

1. Email us at <team@opencrvs.org> to explore the feature together.
2. File an issue with [t](https://github.com/facebook/docusaurus/issues/new?template=feature.md)he [feature template.](https://github.com/opencrvs/opencrvs-core/issues/new?assignees=\&labels=%E2%98%95%EF%B8%8F+Discussion\&template=---feature.md\&title=)
3. Join the community at <https://community.opencrvs.org/> and ask what others think about your idea.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/general/contributing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
