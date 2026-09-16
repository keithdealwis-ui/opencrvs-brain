---
title: "Design principles"
source_url: "https://documentation.opencrvs.org/general/opencrvs/design-principles"
markdown_url: "https://documentation.opencrvs.org/general/opencrvs/design-principles.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:208f40d82d8db66803e0012f7c85526b56f11b686da25267f834afa41e75e1e1"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/general/opencrvs/design-principles.md).

# Design principles

### 1. Intoduction

We continue to stand by our original product commitments for OpenCRVS, and these help steer the strategic direction of the product:\
\
Product commitments:

1. **Fully open-source**, with no license fees or ties to specific vendors
2. **Configurable** for all country contexts
3. **Interoperable** with other government systems
4. **Highly accessible** to ensure inclusion, even in remote areas
5. **Safe and secure** to keep personal data protected
6. **Easy to deploy and use** in low-resource settings
7. **Enabling new models** of civil registration that can help achieve universal registration

***

### 2. Our design principles

We are passionate about designing a product that fulfills our mission: to make civil registration easy and valuable for everyone by making high-quality and cost-effective digital systems widely available and sustainable.

Our design principles provide a clear framework for all those working on OpenCRVS to make design decisions that affect how the product works.

#### 2.1. Start with users' needs

Listen to, engage with, and observe users. Spend time to understand their needs, assume nothing, and work with your users to create designs.

#### 2.2. Prioritise offline

Every product feature must work offline and in areas of low connectivity. Where connectivity is required to complete an action, tell the user what's happening and always consider the loading state.

#### 5.3. Give guidance throughout

The user shouldn't have any questions about what to do—it should be intuitive. Make the product simple and offer clear guidance every step of the way.

#### 5.4. Test, learn, and iterate

The best way to develop new features is to get an early version into the hands of users, then listen → learn → iterate.

#### 5.5. Enable rights

We want to empower and protect those who use and are served by OpenCRVS. Is what you are designing likely to exclude or discriminate against anyone? How can this be avoided?

#### 5.6. Be consistent

Every part of the product should look and feel part of the whole. Always use the component library.

#### 5.7. Be hyper-accessible

Our users are from across the world with varying levels of digital literacy. Whatever we design must be intuitive, legible, and as accessible as possible.

#### 5.8. Words matter

Every word should be understood by users, with no room for ambiguity. When drafting text, avoid administrative language and test it with local users.

#### 5.9. Design with data

Use data generated from the system to inform design improvements.

#### 5.10. Consider other contexts

OpenCRVS is a global product. Consider the variability of what you are designing—will it work in other countries and contexts, and how will it be easily configured


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/general/opencrvs/design-principles.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
