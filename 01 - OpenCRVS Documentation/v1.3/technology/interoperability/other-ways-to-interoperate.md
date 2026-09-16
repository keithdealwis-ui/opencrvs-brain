---
title: "Other ways to interoperate"
source_url: "https://documentation.opencrvs.org/v1.3/technology/interoperability/other-ways-to-interoperate"
markdown_url: "https://documentation.opencrvs.org/v1.3/technology/interoperability/other-ways-to-interoperate.md"
version: "v1.3"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:e3e88310600544b7310388804dc06e732f91548804170d324bf477009760372f"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.3/technology/interoperability/other-ways-to-interoperate.md).

# Other ways to interoperate

Direct interoperability with OpenHIM

It is possible to expose the interoperability layer: [OpenHIM](http://openhim.org/docs/introduction/about) for direct integration with OpenCRVS' Hearth database.

{% hint style="warning" %}
Exposing OpenHIM for API access bypasses the auditing capabilities that are native to OpenCRVS. You must consider the risk and develop your own audit trail to track custom API access to citizen data should you expose OpenHIM. OpenHIM's logging history is configured to refresh after 30 days.  You should fully understand [OpenHIM](http://openhim.org/docs/introduction/about) before proceeding.
{% endhint %}

{% hint style="danger" %}
**Before exposing OpenHIM, consider getting in touch with us at** [**team@opencrvs.org**](mailto:team@opencrvs.org) **in order to request an API feature.  We could develop a client for you that protects citizen data with a native OpenCRVS audit trail.**
{% endhint %}

#### Expose OpenHIM via a Traefik whitelist

In order to expose OpenHIM to be accessible on the public internet, you must comment in [these lines in the docker-compose.deploy.yml file.](https://github.com/opencrvs/opencrvs-core/blob/ced5cf02ebe66994e0151b4cedf17c5091dce74e/docker-compose.deploy.yml#L844)

You must enter a comma separated list of trusted IP addresses to the whitelist property.

You need to create a [DNS](/v1.3/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.5-setup-dns-a-records.md) record to expose the *api.\<your-domain>* endpoint to OpenHIM.

Now you can create your own microservice [Mediator](http://openhim.org/docs/dev-guide/developing-mediators/) and register it with OpenHIM following the [OpenHIM documentation.](http://openhim.org/docs/dev-guide/developing-mediators/)

#### What are OpenHIM Mediators?

[Mediators](http://openhim.org/docs/dev-guide/developing-mediators/) are separate microservices that run independently to OpenCRVS and perform additional mediation tasks for a particular use case. The common tasks within a mediator are as follows:

* **Message format adaptation** - this is the transformation of messages received in a certain format into another format (eg. HL7 v2 to HL7 v3 or MHD to XDS.b).
* **Message orchestration** - this is the execution of a business function that may need to call out to one or more other service endpoint on other systems. (eg. Enriching a message with a client’s unique identifier retrieved from a client registry then sending the enriched message to a shared health record).

Mediators can be built using any platform that is desired (some good options are pure Java using our mediator engine, Node.js, Apache Camel, Mule ESB, or any language or platform that is a good fit for your needs). The only restriction is that the mediator MUST communicate with the OpenHIM-core in a particular way.

Mediators must register themselves with the OpenHIM-core, accept request from the OpenHIM-core and return a specialised response to the OpenHIM-core to explain what that mediator did.

If you are interested in developing your own mediators, read the [OpenHIM Documentation](http://openhim.org/docs/dev-guide/developing-mediators/)

### Security guidance

{% hint style="warning" %}
**OpenCRVS FHIR Resources contain sensitive patient data.** When you are writing your mediator, it is your responsibility as an OpenCRVS implementor in your nation to ensure that you security check the accessing client. The following steps are essential:
{% endhint %}

#### Mediator authorisation to OpenCRVS data

1. The mediator's exposed client endpoints must be protected by SSL so that data is encrypted in transit.
2. The endpoints must enforce JWT authentication.
3. The endpoints must check the scope of the JWT before permitting any further requests for business functions you feel are relevant to that scope.
4. Once the mediator has been written, tested and peer reviewed, it must be penetration tested by an equivalent independent, [CREST](https://www.crest-approved.org/) equivalent certified penetration testing organisation before deployment.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.3/technology/interoperability/other-ways-to-interoperate.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
