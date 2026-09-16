---
title: "In-form authentication / verification with E-Signet"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/in-form-authentication-verification-with-e-signet"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/in-form-authentication-verification-with-e-signet.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:73b2b46e6639dc13f923803d6565cecd6f626faf99929bcfb070717b92e38988"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/in-form-authentication-verification-with-e-signet.md).

# In-form authentication / verification with E-Signet

{% hint style="info" %}
This section assumes that you have already read the general [National ID - In-form authentication /verification](/v1.9/technology/interoperability/national-id/in-form-authentication-verification.md) section and understand the basic concepts of the fields which will render in your form when using these helper functions. If you have not read that page, read it first for a high level introduction to the concepts, and then return here.
{% endhint %}

In the countryconfig-mosip repo, observe helper functions on the [mother.ts](https://mother.tshttps/github.com/opencrvs/opencrvs-countryconfig-mosip/blob/develop/src/form/v2/birth/forms/pages/mother.ts) page ...

[A helper function that uses](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/form/v2/birth/forms/pages/mother.ts#L112) the **ID\_READER** component to render a **QR\_READER** and **LINK\_BUTTON** to redirect users to E-Signet. **QUERY\_PARAM\_READER**, **LOADER** & **HTTP** components are built in to control the subsequent *OIDP\_USERINFO* requests that E-Signet requires. **VERIFICATION\_STATUS** components broadcast the correct user experience both for E-Signet and offline QR validation.

{% hint style="success" %}
This helper function means that you do not need to code and configure any of the above components individually.
{% endhint %}

```
...getMOSIPIntegrationFields('mother', {
  existingConditionals: [
    {
      type: ConditionalType.SHOW,
      conditional: requireMotherDetails
    }
  ]
})
```

[A helper function that ensures](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/form/v2/birth/forms/pages/mother.ts#L120C5-L144C7) returned values from the requests pre-populate and disable input fields on the form.

```
connectToMOSIPIdReader(
  {
    id: 'mother.name',
    type: FieldType.NAME,
    required: true,
    configuration: farajalandNameConfig,
    hideLabel: true,
    label: {
      defaultMessage: "Mother's name",
      description: 'This is the label for the field',
      id: 'event.birth.action.declare.form.section.mother.field.name.label'
    },
    conditionals: [
      {
        type: ConditionalType.SHOW,
        conditional: and(requireMotherDetails)
      }
    ],
    validation: [invalidNameValidator('mother.name')]
  },
  {
    valuePath: 'data.name',
    disableIf: ['pending', 'verified', 'authenticated']
  }
),
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/mosip/in-form-authentication-verification-with-e-signet.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
