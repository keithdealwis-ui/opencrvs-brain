---
title: "Registration integration"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/registration-integration"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/registration-integration.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f86e6983f18085dda60ece3ff58aa7d4d97cd0ffad0476ae94970295d48f4fcf"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/registration-integration.md).

# Registration integration

Interoperating with a National ID system at the point of registration, both synchronously and asynchronously.

In the OpenCRVS UI, when a registrar clicks the "Register" button on a fully complete and validated declaration, the legal authority has been given to create a birth registration.  It is then possible to integrate with a National ID system, both synchronously and asynchronously.

### Synchronous integration - birth & death

Once internal audit has taken place of that action in the "workflow" microservice, the following endpoint in the configurable countryconfig microservice is called while the registration is in a `WAITING_VALIDATION` status:

```
/event-registration
```

The entire registration data payload is sent to [this endpoint](https://github.com/opencrvs/opencrvs-countryconfig/blob/4d9b0081e38f11325ff47cecc3a51df85b50cffb/src/index.ts#L431) as a FHIR Bundle.

{% hint style="warning" %}
The JWT token that is sent to this payload can be used in asynchronous operations explained below.
{% endhint %}

In our example we create a birth / death registration number at this point and return the amended payload to OpenCRVS.  Any synchronous interaction with a National ID system can take place here.

If a 200 is returned from this handler, the record will proceed to register, gaining a `REGISTERED` status, and appear in the Ready To Print work queue.

If any error occurs such as a 500, the record will be placed in a `REJECTED` status with the reason being equal to whatever error code or message is available.  &#x20;

The following library can return a graceful rejection message.

```typescript
@hapi/boom badImplementation
```

&#x20; &#x20;

### Aynchronous integration - birth & death

It is possible to use the same endpoint asynchronously.  But first, the following setting must be set to true in [application-config.ts](/v1.8/setup/3.-installation/3.2-set-up-your-own-country-configuration/3.2.5-set-up-application-settings.md):

```typescript
EXTERNAL_VALIDATION_WORKQUEUE: true
```

This configuration setting enables a work-queue "In external validation" that can hold records in a `WAITING_VALIDATION` status until an asynchronous process completes.

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2FToXgb49QHE1VWkl5dUXe%2FScreenshot%202025-06-05%20at%2018.02.55.png?alt=media&amp;token=f79263df-f1de-4e13-9c7b-4b10e42df80b" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
The JWT token that is sent to the /event-registration endpoint & the birth / death registration number that is generated here, must be stored by your asynchronous process and used in the next operation.
{% endhint %}

Using the JWT, you can call the gateway microservice GraphQL endpoint `confirmRegistration` resolver.

You can decode the JWT and retrieve the internal record uuid - the variable `id` used in the payload.

```
POST https://gateway.<your_domain>/graphql
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "operationName": "confirmRegistration",
  "query": "mutation confirmRegistration(
        $id: ID!
        $details: ConfirmRegistrationInput!
      ) {
        confirmRegistration(id: $id, details: $details)
      }",  
  "variables": {
      "id":"<record uuid from JWT>",
      "details": {
        "identifiers": [{
          "type": "NATIONAL_ID",
          "value": "<optionally store created natonal id at birth for use in OpenCRVS search / certificate>"
        }],
        "registrationNumber": "<Birth / Death Registration Number>",
        "comment": "<optionally store an audit log comment>",
      }
  }
}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/national-id-client/registration-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
