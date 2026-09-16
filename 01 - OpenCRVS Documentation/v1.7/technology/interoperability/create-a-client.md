---
title: "Create a client"
source_url: "https://documentation.opencrvs.org/v1.7/technology/interoperability/create-a-client"
markdown_url: "https://documentation.opencrvs.org/v1.7/technology/interoperability/create-a-client.md"
version: "v1.7"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:186a57a440708a270cfbdfe1bd1c32a17e56a813cc1e4f841c4911d9621935e0"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.7/technology/interoperability/create-a-client.md).

# Create a client

How to create and manage access to OpenCRVS' interoperability functionality

In order to interoperate with OpenCRVS, you must first create an official client.

Only a National System Administrator role can create a client. E.G. In our example for our fake country Farajaland, this is the user: **j.campbell**

1. Login to OpenCRVS as the user: **j.campbell**
2. Use the left navigation to select the **Configuration** > **Integrations** section.

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/3mPDHjeDwmeK9Vh0vGTw/Screenshot%202023-01-11%20at%2011.34.03.png" alt=""><figcaption></figcaption></figure>

3\. Click **+ Create client**

4\. You will see a modal overlay where you can select the type of client you wish to create.  The business functionality available for each client is explained in subsequent pages in this section of our documentation.

**The type of client you create is important and can only perform API requests associated with the business functionality relevant to that type.**  A Record Search client is not authorized to perform an Event Notification for example.&#x20;

You must give each client a unique name.

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/KsMy85STfxnsXVx8qw9J/Screenshot%202023-01-11%20at%2011.34.17.png" alt=""><figcaption><p>Creating an Event notification client</p></figcaption></figure>

5\. When you click "Create", you will be shown the authentication details for the client along with a SHA Secret used to sign, encrypt, decrypt and verify the authenticity of payloads.

{% hint style="warning" %}
**You must copy these keys now!  The Client Secret will never be displayed to you again and it cannot be retrieved from our database as it is encrypted.**
{% endhint %}

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/XLNj7B6GylklbbV7YdUN/Screenshot%202023-01-11%20at%2011.35.15.png" alt=""><figcaption></figcaption></figure>

6\. You can manage existing clients by using the **3 dots** menu after the client has been created.  You can **reveal the Client ID and SHA Secret keys** at any time and **refresh the Client Secret** to create a new one by selecting "**Reveal Keys**". &#x20;

{% hint style="warning" %}
When you refresh a Client Secret, the old secret will no longer work for authentication.
{% endhint %}

You can also temporarily "**Deactivate**" and "**Enable**" a client or alternatively "**Delete**" it.

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/lCPEq8uWBpVwbCCJihqN/Screenshot%202023-01-11%20at%2011.35.35.png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
All client behaviour is audited and is ultimately the personal responsibility of the National System Administrator of OpenCRVS that created the client.  Protect citizen data and do not expose access unnecessarily, as you may be in breach of local privacy laws.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/5MyZkLNN4YdFPLw4TgLb/Screenshot%202023-01-11%20at%2011.34.26.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/vgBjh6h3DfeeMhA5gwiP/blobs/RBfazTrhzGj46XsPrxYk/Screenshot%202023-01-11%20at%2011.34.39.png" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.7/technology/interoperability/create-a-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
