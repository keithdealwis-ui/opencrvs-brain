---
title: "Registration integration"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/registration-integration"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/registration-integration.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:c3806e931b00ba175bbdf3fa8d301e8cfb2d052e406862f1a183c763296bb0a0"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/registration-integration.md).

# Registration integration

Using MOSIP's Packet Manager API for asynchronous integration at the point of registration

{% hint style="info" %}
This section assumes that you have already read the general [National ID registration integration page](/v1.8/technology/interoperability/national-id-client/registration-integration.md).   If you have not read that page, read it first for a high level introduction to the concepts, and then return here.
{% endhint %}

### Asynchronous integration

MOSIP integration can only work asynchronously, so ensure that you have enabled the external validation workqueue and prepare to configure the endpoints we described in the link above.

Note how we customise the event-registration endpoint in order to follow whatever configuration requirements exist for the country and prepare the payload for the **mosip-api** middleware that will authenticate with MOSIP, and submit data using. the MOSIP Packet Manager API at [this](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/4fa62771a1faea01f87c2fb0db80824e8f594fe7/src/index.ts#L445) point in the code:

```
handler: async (request, h) => {
  const url = env.isProd ? 'http://mosip-api:2024' : 'http://localhost:2024'
  const result = await verify({ url, request })
  const bundle = request.payload as fhir3.Bundle

  if (shouldForwardToIDSystem(request.payload as fhir3.Bundle, result)) {
    const payload =
      getEventType(bundle) === 'BIRTH'
        ? fhirBirthToMosip(bundle)
        : fhirDeathToMosip(bundle)

    logger.info(
      'Passed country specified custom logic check for id creation. Forwarding to MOSIP...'
    )

    return mosipRegistrationHandler({
      url,
      headers: request.headers,
      payload
    })(request, h)
  } else {
    logger.info(
      'Failed country specified custom logic check for id creation. Bypassing id system...'
    )
    return eventRegistrationHandler(request, h)
  }
}
```

Lets delve into the example functions we have written to explain the logic.

### shouldForwardToIDSystem

There will be edge cases in your civil registration and foundational identity business processes where you do not always want to create a MOSIP National ID at the point of birth, or inform MOSIP at death,  depending on the demographic data completed by the informant.  This function examines the payload according to these **purely example rules**.  You should configure these according to the laws and processes relevant to your country:

* In this example, we are only creating a National ID at birth if any of the parents or informant have successfully completed "in-form authentication", using QR Code or E-Signet
* At death, we are only informing MOSIP that the deceased has passed if the spouse has successfully completed "in-form authentication", using QR Code or E-Signet
* We are only creating a National ID at birth automatically from the cvil registration if the child is under 10 years of age.  If the child is over 10, then to create a National ID, they will be required to do so directly in MOSIP and submit their biometrics.

### fhirBirthToMosip / fhirDeathToMosip

Every country has a different form configuration with different questions and sections and different requirements regarding the demographic data points that are required by MOSIP. &#x20;

The configurability of the systems are key selling points of both MOSIP & OpenCRVS. &#x20;

The OpenCRVS form data is expressed in the FHIR standard and therefore must be converted into a format that is understandable by the MOSIP Packet Manager API.  That is the purpose of these mapping functions.  You should customise them to suit the form that you have configured and the MOSIP data requirements that your country has decided to configure.

### mosipRegistrationHandler

This function is imported from our NPM library into your countryconfig repo and calls the mosip-api middleware.  The mosip-api middleware creates and stores an Application ID (AID) along with the Birth Registration Number and sends the full payload with this metadata to MOSIP. &#x20;

For reference, this logic is here:&#x20;

{% embed url="<https://github.com/opencrvs/mosip/blob/9c43d0f902416935b04a95344819fc43b5b44d62/packages/mosip-api/src/routes/event-registration.ts#L89>" %}

The metadata is stored in an SQLLite database.  MOSIP processes asynchronously, so the mosip-api has to subscribe to MOSIP WebSub status updates which will contain a credential issuance with the metadata,  so OpenCRVS can identify the credential with the correct application. &#x20;

In the case of birth for example, when the status of the MOSIP application is successful and a credential is issued, the mosip-api can retrieve the record from the SQLLite database, append the VID and inform OpenCRVS Core that MOSIP registration is completed.

### confirmRegistration mutation on MOSIP WebSub credential issuance

The mosip-api will call the confirmRegistration mutation automatically when the credential is received and decoded. &#x20;

For reference, the logic is here:

{% embed url="<https://github.com/opencrvs/mosip/blob/9c43d0f902416935b04a95344819fc43b5b44d62/packages/mosip-api/src/routes/websub-credential-issued.ts#L35>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/mosip/registration-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
