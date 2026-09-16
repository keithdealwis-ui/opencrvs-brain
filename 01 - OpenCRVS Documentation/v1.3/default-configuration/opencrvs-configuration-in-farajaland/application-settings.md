---
title: "Application settings"
source_url: "https://documentation.opencrvs.org/v1.3/default-configuration/opencrvs-configuration-in-farajaland/application-settings"
markdown_url: "https://documentation.opencrvs.org/v1.3/default-configuration/opencrvs-configuration-in-farajaland/application-settings.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b22badf74c7ae67864b7b02a7e2ff2c54e0026c77b0db4003fbf82c77327cb16"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/default-configuration/opencrvs-configuration-in-farajaland/application-settings.md).

# Application settings

The following application settings have been used in the Farajaland OpenCRVS configuration to support the country context.

| Setting                                              | Farajaland value                                                                                                                                                                                                                    | Notes                                                                                        |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Name of application                                  | Farajaland CRS                                                                                                                                                                                                                      |                                                                                              |
| Government logo                                      | <img src="https://1176971301-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6qn2vAsiooyRnf055REr%2Fuploads%2Fgit-blob-e5ce89f12145b02f77ba040933e87a34cf52a07b%2Fimage.png?alt=media" alt="" data-size="line"> |                                                                                              |
| Currency                                             | United States dollar                                                                                                                                                                                                                |                                                                                              |
| Phone number                                         | ^0(7\|9)\[0-9]{8}$                                                                                                                                                                                                                  | This RegEx represents a 10 figure number starting with 07 or 09                              |
| Unique Identification Number (UIN) e.g. National ID  | ^\[0-9]{9}$                                                                                                                                                                                                                         | This RegEx represents a 9 digit number                                                       |
| Legally specified time period for birth registration | Within 30 days                                                                                                                                                                                                                      |                                                                                              |
| Late registration of birth                           | Between 30 days and 365 days                                                                                                                                                                                                        |                                                                                              |
| Delayed registration of birth                        | After 365 days                                                                                                                                                                                                                      |                                                                                              |
| Fees for on-time registration of birth               | $ 0                                                                                                                                                                                                                                 |                                                                                              |
| Fees for late registration of birth                  | $ 5.50                                                                                                                                                                                                                              | Requesting fees for birth registration is not advised, however it is possible in the system. |
| Fees for delayed registration of birth               | $ 15.00                                                                                                                                                                                                                             | Requesting fees for birth registration is not advised, however it is possible in the system. |
| Legally specified time period for death registration | Within 45 days                                                                                                                                                                                                                      |                                                                                              |
| Delayed registration of death                        | After 45 days                                                                                                                                                                                                                       |                                                                                              |
| Fees for on-time registration of birth               | $ 0                                                                                                                                                                                                                                 |                                                                                              |
| Fees for delayed registration of birth               | $ 15.00                                                                                                                                                                                                                             | Requesting fees for birth registration is not advised, however it is possible in the system. |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/default-configuration/opencrvs-configuration-in-farajaland/application-settings.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
