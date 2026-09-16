---
title: "Event Notification clients"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/event-notification-clients"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/event-notification-clients.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8a11bf092ce9884ca89c845dc4474a2d8ab4fc358b48eea0316d909481fa074d"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/event-notification-clients.md).

# Event Notification clients

Submitting full or partial event applications into OpenCRVS from an external service such as a health institution or public portal.

An **Event Notification client** can submit full or partial events to an OpenCRVS office. You can find the technical documentation for the Event Notification APIs in our [Swagger documentation](https://api.opencrvs.org/develop/events/).

{% hint style="info" %}
You can use our [Postman collections](https://github.com/opencrvs/opencrvs-countryconfig/tree/master/postman) to test the Event Notification API functionality. Specifically, use the **Event Notification - v1.9.0** collection. [Postman](https://www.postman.com/) is a tool you can download to test API access before building your integrations.
{% endhint %}

The following images and examples use the fictional country [Farajaland](https://github.com/opencrvs/documentation/blob/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/default-configuration/intro-to-farajaland.md) and its birth registration configuration. Your actual events and workflows may vary depending on your country’s configuration.

[![](https://github.com/opencrvs/documentation/raw/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/.gitbook/assets/Screenshot%202023-01-11%20at%2015.39.53.png)](https://github.com/opencrvs/documentation/blob/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/.gitbook/assets/Screenshot%202023-01-11%20at%2015.39.53.png)

An Event Notification in the Farajaland 'In Progress' view

When Event Notifications are received in OpenCRVS, they are audited and logged as being received from an automated client. **Events submitted via the Event Notification API are saved with the status `NOTIFIED`.**

[![](https://github.com/opencrvs/documentation/raw/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/.gitbook/assets/Screenshot%202023-01-11%20at%2015.40.23.png)](https://github.com/opencrvs/documentation/blob/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/.gitbook/assets/Screenshot%202023-01-11%20at%2015.40.23.png)

Record audit view for an Event Notification

### Submitting an Event Notification

To submit an Event Notification, your client must first request an [authorization token](https://github.com/opencrvs/documentation/blob/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/technology/interoperability/authenticate-a-client.md) using your `client_id` and `client_secret`.

#### Event Notification Requests

Using the token in the Authorization header, an event is notified via two sequential API requests:

1. `POST /api/events/events` to initialize the event
2. `POST /api/events/events/notifications` to submit full or partial event data and trigger the notification

The example below demonstrates how to submit a simple birth declaration based on the [Farajaland](https://github.com/opencrvs/documentation/blob/0f41a2a0f97263259ea0116062255abd71e4bcf3/v1.9.0/default-configuration/intro-to-farajaland.md) configuration. This example will contain the child's name and date of birth details.

```
POST /api/events/events
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "type": "v2.birth",
  "transactionId": "{{uuid}}",
  "dateOfEvent": {
    "fieldId": "child.dob"
  }
}
```

{% hint style="info" %}
This request will return a response containing the event ID in the `id` field. You must use this `eventId` in the subsequent request.
{% endhint %}

Once the event is initialized, you can submit the notification:

```
POST /api/events/events/notifications
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "eventId": "{{eventId}}",
  "transactionId": "{{uuid}}",
  "declaration": {
    "child.firstname": "Jane",
    "child.surname": "Doe",
    "child.dob": "{{yyyy-MM-dd}}"
  },
  "annotation": {},
  "createdAtLocation": "{{officeId}}", // Retrievable from the location API - See "APIs for system administrators"
  "type": "NOTIFY"
}
```

For full API details, refer to the [Swagger documentation](https://api.opencrvs.org/develop/events/).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/event-notification-clients.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
