---
title: "APIs requiring OAuth credentials"
source_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/create-a-client"
markdown_url: "https://documentation.opencrvs.org/v1.8/technology/interoperability/create-a-client.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:0aa2caaaec7e8e35c5143d277d344ea5409fa569afc6277bf7bfb90d550902dc"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/technology/interoperability/create-a-client.md).

# APIs requiring OAuth credentials

In order to interoperate with OpenCRVS' record search, event notification and webhooks, you must first create an OAuth client.

Only a National System Administrator role can create a client. E.G. In our example for our fake country Farajaland, this is the user: **j.campbell**

1. Login to OpenCRVS as the user: **j.campbell**
2. Use the left navigation to select the **Configuration** > **Integrations** section.

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-1632d860e5c9ad8aa7d285cfe73f4ac3cd01e2db%2FScreenshot%202023-01-11%20at%2011.34.03.png?alt=media" alt=""><figcaption></figcaption></figure>

3\. Click **+ Create client**

4\. You will see a modal overlay where you can select the type of client you wish to create. The business functionality available for each client is explained in subsequent pages in this section of our documentation.

**The type of client you create is important and can only perform API requests associated with the business functionality relevant to that type.** A Record Search client is not authorized to perform an Event Notification for example.

You must give each client a unique name.

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-89b00440e5bc71e8fb556cf08142472b62bdcc1a%2FScreenshot%202023-01-11%20at%2011.34.17.png?alt=media" alt=""><figcaption><p>Creating an Event notification client</p></figcaption></figure>

5\. When you click "Create", you will be shown the authentication details for the client along with a SHA Secret used to sign, encrypt, decrypt and verify the authenticity of payloads.

{% hint style="warning" %}
**You must copy these keys now! The Client Secret will never be displayed to you again and it cannot be retrieved from our database as it is encrypted.**
{% endhint %}

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-ecd0e88ed929714ba7ef5233ea7f686df7701169%2FScreenshot%202023-01-11%20at%2011.35.15.png?alt=media" alt=""><figcaption></figcaption></figure>

6\. You can manage existing clients by using the **3 dots** menu after the client has been created. You can **reveal the Client ID and SHA Secret keys** at any time and **refresh the Client Secret** to create a new one by selecting "**Reveal Keys**".

{% hint style="warning" %}
When you refresh a Client Secret, the old secret will no longer work for authentication.
{% endhint %}

You can also temporarily "**Deactivate**" and "**Enable**" a client or alternatively "**Delete**" it.

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-1dbcdf5113e7e073b8dc75f9c8d6105aac52a6a6%2FScreenshot%202023-01-11%20at%2011.35.35.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
All client behaviour is audited and is ultimately the personal responsibility of the National System Administrator of OpenCRVS that created the client. Protect citizen data and do not expose access unnecessarily, as you may be in breach of local privacy laws.
{% endhint %}

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-464b9178965b9fee73cce785d417a0f0efbf281a%2FScreenshot%202023-01-11%20at%2011.34.39.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**The National ID client below is now deprecated in OpenCRVS v1.8.0.** Follow the National ID section in order to integrate a National ID system
{% endhint %}

<figure><img src="https://3067259618-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fesn2q91OsFQf7ZqR8thb%2Fuploads%2Fgit-blob-5e66f6c660448ecb6189bae14b567d9a43004d92%2FScreenshot%202023-01-11%20at%2011.34.26.png?alt=media" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/technology/interoperability/create-a-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
