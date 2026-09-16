---
title: "Registration integration"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/registration-integration"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/registration-integration.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:4b0d0f3f05c2c663ed09a8db0de8fc928f1290c05c1fd6ad6fb4215863eb4d64"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/registration-integration.md).

# Registration integration

In the OpenCRVS UI, when a registrar clicks the "Register" button on a fully complete and validated declaration, the legal authority has been given to create a birth registration. It is then possible to integrate with a National ID system, both synchronously and asynchronously.

### Synchronous integration - birth & death

Once internal audit has taken place of that action in the "workflow" microservice, the following endpoint in the configurable countryconfig microservice is called while the registration is in a `WAITING_VALIDATION` status:

```
/trigger/events/${Event.id}/actions/${ActionType.REGISTER}`
```

Refer to our [default](https://github.com/opencrvs/opencrvs-countryconfig/blob/ef1160edee76b4aa2f619d81f396c740346f6565/src/index.ts#L672) and [MOSIP](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/index.ts#L668) example.

{% hint style="warning" %}
The JWT token that is sent to this payload should be used to communicate back with OpenCRVS using a client from our toolkit: `import { createClient } from '@opencrvs/toolkit/api'`
{% endhint %}

In our example we create a birth / death registration number at this point and return the amended payload to OpenCRVS. Any interaction with a National ID system can take place here.

{% hint style="info" %}
Based on your own business rules based on submitted bio/demographics, such as age of child / parents IDs authenticated, you need to decide whether or not to interoperate with National ID, continue to register or reject the declaration.
{% endhint %}

You can access properties of the `declaration` and the submitting user (via `pendingAction`) to perform logical decision making like so:

```
export async function onBirthActionHandler(
  request: ActionConfirmationRequest,
  h: Hapi.ResponseToolkit
) {
  const token = request.auth.artifacts.token as string
  const event = request.payload

  const pendingAction = getPendingAction(event.actions)
  const declaration = deepMerge(
    aggregateActionDeclarations(event),
    pendingAction.declaration
  )

  /*
    declaration['child.dob'] 
    declaration['mother.nid'] 
    declaration['mother.verified'] !== 'authenticated'
  */
```

Using the JWT, you can process your integration and respond to OpenCRVS as you wish, progressing the declaration to a [REGISTERED](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L111) or [REJECTED](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/registration/index.ts#L172) status accordingly.

### Aynchronous integration - birth & death

It is possible to use the same endpoint asynchronously. But first, you must configure an in-external-validation workqueue in your [worqueueConfig](https://github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/api/workqueue/workqueueConfig.ts#L377C3-L399C5) and ensure that the correct users have permission to view the workqueue in [roles.ts](https://roles.tshttps/github.com/opencrvs/opencrvs-countryconfig-mosip/blob/a02aad6e0d8a8a6bfbfd31f35b77e63b409615f6/src/data-seeding/roles/roles.ts#L162C7-L162C138).

**workqueueConfig.ts**

```
{
    slug: 'in-external-validation',
    icon: 'FileText',
    name: {
      id: 'workqueues.inExternalValidation.title',
      defaultMessage: 'In external validation',
      description: 'Title of in external validation workqueue'
    },
    query: {
      flags: {
        anyOf: [
          `${ActionType.REGISTER}:${ActionStatus.Requested}`.toLowerCase()
        ]
      },
      updatedAtLocation: { type: 'exact', term: user('primaryOfficeId') }
    },
    actions: [
      {
        type: 'DEFAULT',
        conditionals: []
      }
    ]
  },
```

**roles.ts**

```
'workqueue[id=in-external-validation...
```

This configuration setting enables a work-queue "In external validation" that can hold records in a `WAITING_VALIDATION` status until an asynchronous process completes.

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fs3LutkYTD5eH4fqaiHxV%2FScreenshot%202025-06-05%20at%2018.02.55.png?alt=media&amp;token=e6592eef-2065-435c-9fe3-cc183a30bc6f" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
The JWT token that is sent to countryconfig must be stored by your asynchronous process in order to communicate back with OpenCRVS. In our MOSIP example, it is stored in an SQLite DB.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/national-id/registration-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
