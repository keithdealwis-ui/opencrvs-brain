---
title: "Release notes"
source_url: "https://documentation.opencrvs.org/releases/release-notes"
markdown_url: "https://documentation.opencrvs.org/releases/release-notes.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:4eea29486f04c851906b895b1295b0683efbbe6789f0ef0c93915c168fe74238"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/releases/release-notes.md).

# Release notes

## Introduction

OpenCRVS release notes document changes, improvements, and fixes delivered in each version. These notes help implementation teams understand what has changed, plan migrations, and take advantage of new features.

Each release includes breaking changes, new features, improvements, and bug fixes. Review the notes carefully before upgrading to ensure compatibility with your country configuration.

***

## Config inputs

{% file src="/files/B0tLWhMmCiucz0Znm2RF" %}

***

## Releases

### v2.1 (Upcoming Q3 2026)

#### **Key highlights**

* Support for custom form fields on action dialogs ([#11951](https://github.com/opencrvs/opencrvs-core/issues/11951))
* Support for `notifiedIn` and `notifiedBy` properties on scopes ([#11875](https://github.com/opencrvs/opencrvs-core/issues/11875))
* Add legal statuses: "Registered (Inactive)" and "Revoked", and related core actions ([#11952](https://github.com/opencrvs/opencrvs-core/issues/11952))
* Add audit log retrieval endpoint ([#11909](https://github.com/opencrvs/opencrvs-core/issues/11909))
* ...and miscellaneous bug fixes and improvements

***

### v2.0

**Release date: 25th of June 2026**

**Core changelog:** [**https://github.com/opencrvs/opencrvs-core/blob/develop/CHANGELOG.md#200-release-candidate**](https://github.com/opencrvs/opencrvs-core/blob/develop/CHANGELOG.md#200-release-candidate)

**Countryconfig changelog:** [**https://github.com/opencrvs/opencrvs-countryconfig/blob/develop/CHANGELOG.md#200**](https://github.com/opencrvs/opencrvs-countryconfig/blob/develop/CHANGELOG.md#200)

**opencrvs-demoland source:**

{% file src="/files/uJDEWZ8wvuFXmYUGuEOF" %}

**Test report:** [**https://docs.google.com/spreadsheets/d/1r2CFnnhpKcwO5z-tgcFlPirrmGfH8dZxCTXSSHXBs38/edit?usp=sharing**](https://docs.google.com/spreadsheets/d/1r2CFnnhpKcwO5z-tgcFlPirrmGfH8dZxCTXSSHXBs38/edit?usp=sharing)

#### **Key highlights**

* **Redesigned administrative hierarchy and jurisdiction.** A country is now modelled as a hierarchy of **administrative areas** (e.g. province → district → village) that *contain* physical **locations** (CRVS offices, health facilities). Read more: [Administrative structure](/functional/markdown/workflows/administrative-structure.md) and [Administrative hierarchy](/technical/guides/configuration/administrative-hierarchy.md)
* **Verifiable credentials for life events.** OpenCRVS can now issue digitally signed credentials through an external issuer. Two forms are available: a digital SD-JWT credential (OpenID4VC) delivered to the citizen's wallet, and a verifiable QR code on printed birth certificates. Signing is handled by an issuer you operate and manage independently. Read more: [Verifiable Credentials](/functional/markdown/records/verifiable-credentials.md) and [Verifiable Credentials](/technical/guides/configuration/integrations/verifiable-credentials.md)
* **Biographic updates via MOSIP.** The integration now supports sending birth corrections to MOSIP via a new \`updateBiographics\` endpoint, enabling a child's biographic data to be created or updated in the identity system during amendment flows. Read more: [MOSIP Registration Integration](/technical/guides/configuration/integrations/mosip-registration-integration.md)
* **Custom actions.** Beyond the core actions, each event can now define its own **custom actions**. Read more: [Custom actions](/technical/guides/configuration/events/actions/custom-actions.md)
* **Redesigned record editing**. The editing of a previously notified or declared record has been reworked to a completely new "Edit" action flow.
* **Technical architecture rework.** The technical architecture has been simplified, drastically reducing the amount of required services ran on k8s or docker-swarm.

#### Improvements

* **Configurable record flags.** Actions can add or remove flags on a record, so workqueues and status indicators are driven by configuration rather than core code.
* **Kubernetes deployment.** OpenCRVS can now be deployed to any Kubernetes cluster using the Helm charts shipped in `opencrvs-core`. Docker Swarm remains supported until v2.1.
* **Improved offline/online recovery.** The app now recovers automatically if the network changes or drops while it is still initialising.
* **Performance improvements.** Performance improvements to e.g. workqueue load times.

#### **Breaking changes**

* **Webhook integration client removed.** The Webhook integration client and its `webhooks` service have been removed and are not migrated automatically. Country configurations that previously relied on webhook subscriptions must instead react to events via Action triggers in the country configuration code. Any webhook-style fan-out to external systems must be implemented inside those handlers.
* **Event Notification API endpoint renamed.** `POST /api/events/events/notifications` has been renamed to `POST /api/events/events/{eventId}/notify`. Existing integration clients must update their request paths. A new single-request convenience endpoint `POST /api/events/events/notify` is also available for system clients that need to create and notify in one call.
* **Auth service is no longer exposed on its own subdomain.** The public `auth.{hostname}` Traefik route has been removed — the auth service is now reachable only through the gateway proxy at `gateway.{hostname}/auth/*`. Remove the `auth.*` DNS record and TLS certificate from your deployment. The gateway's `/auth/authenticate-super-user` route is now rate limited on a constant key (it previously keyed on a `username` field that super user auth does not send).
* **Configuration model rewritten.** Events, forms, workflows, and actions are now defined in TypeScript with the `@opencrvs/toolkit` package (`defineConfig`).
  * These required changes can be automatically applied to an existing country config using `yarn opencrvs upgrade`, see [Version upgrades](/technical/guides/version-upgrades.md#step-2-update-code-and-test-locally)
* **Other configuration changes.** `InherentFlags.PENDING_CERTIFICATION` has been removed (implement it as a custom flag instead); workqueue configuration uses `action: { … }` rather than `actions: [ … ]` and no longer accepts `'DEFAULT'`; and `FieldType.PARAGRAPH` no longer takes a `fontVariant` — use the new `FieldType.HEADING` where a heading style is needed.
  * These required changes can be automatically applied to an existing country config using `yarn opencrvs upgrade`, see [Version upgrades](/technical/guides/version-upgrades.md#step-2-update-code-and-test-locally)

#### **Bug fixes**

* A broad set of fixes and improvements across the record workflows, record search, notifications, and deployment accompanies.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/releases/release-notes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
