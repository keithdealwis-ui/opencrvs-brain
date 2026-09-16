---
title: "In-form authentication / verification & E-Signet"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/in-form-authentication-verification-using-e-signet"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/in-form-authentication-verification-using-e-signet.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:67da30108edee09608a67b1d561bcb8aa6cd2816c2ae1b5881b4f8ed49487618"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/in-form-authentication-verification-using-e-signet.md).

# In-form authentication / verification & E-Signet

{% hint style="info" %}
This section assumes that you have already read the general [National ID "in-form authentication" page](/v1.8/technology/interoperability/national-id-client/in-form-authentication-verification.md).   If you have not read that page, read it first for a high level introduction to the concepts, and then return here.
{% endhint %}

Take a look at our example configuration.  Helper form field functions are imported from our NPM library to make it easy to configure offline and online (with E-Signet) plus manual entry fields if you pay close attention to the code.

Look at how these functions are used:

### idReaderFields

This [function](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/form/birth/index.ts#L240) will apply all the UI fields in your forms on the relevant pages for both QR Code reader and E-Signet redirect.

### getInitialValueFromIDReader

This [function](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/form/birth/index.ts#L259C15-L259C42) will set the initialValue (pre-population) of a form field and disable it from being edited on succesful scanning of an authentic QR code from an NID card, or successful authentication from E-Signet.

### Offline

Observe the [qrCodeConfig](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/form/common/id-reader-configurations.ts#L37) property to configure the values that will be available for form initialValues (pre-population) from the QRCode supplied by MOSIP on their National ID cards.

### Online

Observe the [esignetConfig](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/form/common/id-reader-configurations.ts#L54) property to see the environment variables that will need to be configured to enable the redirect to E-Signet.  The available E-Signet data that can be used as initialValues (pre-population) is configurable in the OPENID\_PROVIDER\_CLAIMS value.

The mosip-api package handles all communication to/from E-Signet and more environment variables are required to be set there.  All of these variables are explained in the next section on [Deployment](/v1.8/technology/interoperability/national-id-client/mosip/deployment.md).

### Routes required for integration with MOSP ID Auth SDK

In OpenCRVS, some event actions require additional confirmation from the Country Configuration API before they can be accepted. This process is known as **action confirmation**.

The MOSIP integration uses the [Action Confirmation API ](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/develop/src/api/action-confirmation.md)to communicate with the MOSIP ID Auth SDK when using the **offline** or **manual** form field options.  This is for a secondary online authentication check once the application is submitted and passes through the OpenCRVS validation, approval and registration status transitions. &#x20;

The following [routes](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/index.ts#L634) **must be added.** These routes are critically important to ensure that the record moves through the process successfully.

```
server.route({
  method: 'POST',
  path: '/events/{event}/actions/sent-notification',
  handler: mosipRegistrationForReviewHandler({
    url: env.isProd ? 'http://mosip-api:2024' : 'http://localhost:2024'
  }),
  options: {
    tags: ['api', 'custom-event'],
    description: 'Receives notifications on sent-notification action'
  }
})

server.route({
  method: 'POST',
  path: '/events/{event}/actions/sent-notification-for-review',
  handler: mosipRegistrationForReviewHandler({
    url: env.isProd ? 'http://mosip-api:2024' : 'http://localhost:2024'
  }),
  options: {
    tags: ['api', 'custom-event'],
    description:
      'Receives notifications on sent-notification-for-review action'
  }
})

server.route({
  method: 'POST',
  path: '/events/{event}/actions/sent-for-approval',
  handler: mosipRegistrationForApprovalHandler({
    url: env.isProd ? 'http://mosip-api:2024' : 'http://localhost:2024'
  }),
  options: {
    tags: ['api', 'custom-event'],
    description: 'Receives notifications on sent-for-approval action'
  }
})
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/in-form-authentication-verification-using-e-signet.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
