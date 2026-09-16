---
title: "Integration: Health notifications / Self-service portal"
source_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-health-notifications-self-service-portal"
markdown_url: "https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-health-notifications-self-service-portal.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8cf2a9dd02b0243f8d2f756bec271138fcd839e35764be5352055fb637a39262"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-health-notifications-self-service-portal.md).

# Integration: Health notifications / Self-service portal

Submitting full or partial event applications into OpenCRVS from an external service such as a health institution or public portal.

An **Event Notification client** can submit full or partial events to an OpenCRVS office.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-ed1204c67e53ee721e513c777a0ed5d260283171%2FScreenshot%202026-06-30%20at%2009.42.48.png?alt=media" alt=""><figcaption></figcaption></figure>

When Event Notifications are received in OpenCRVS, they receive the status "Notified", are audited and logged as being received from an automated client, and appear within the Notifications workqueue.

#### Submitting an Event Notification

With an authorised token, first [create an event](https://documentation.opencrvs.org/technical/apis/core-apis/events#post-events).

{% hint style="info" %}
This request will return a response containing the event ID in the `id` field. You must use this `eventId` in the subsequent request.
{% endhint %}

#### Event Notification Requests

Once the event is creaeted, you can submit the [notification](https://documentation.opencrvs.org/technical/apis/core-apis/events#post-events-eventid-notify).

#### Example API integration: DHIS2 Annual Conference 2026

During a demonstration at the [DHIS2](https://dhis2.org/) Annual Conference 2026, [OpenFN](https://www.openfn.org/) ran a cron job to monitor new "Tracked Entities" in DHIS2 every 24 hours, then transform the entities into an OpenCRVS Event Notification payload. &#x20;

The demonstration used hardcoded CRVS\_OFFICE and HEALTH\_FACILITY ids.  These can be dynamically retrieved via the OpenCRVS [Location](/technical/apis/core-apis/locations.md) API.

This [repository](https://github.com/opencrvs/event-notification-integration) contains example code to submit the notification to OpenCRVS.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/configuration/integrations/integration-health-notifications-self-service-portal.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
