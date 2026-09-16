---
title: "National ID client"
source_url: "https://documentation.opencrvs.org/v1.6/technology/interoperability/national-id-client"
markdown_url: "https://documentation.opencrvs.org/v1.6/technology/interoperability/national-id-client.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:05aaf2f1a17243d741b95f44552ef428da75fca49e0d6306d73f15639996fc09"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/technology/interoperability/national-id-client.md).

# National ID client

Business functionality associated with a National ID client and instructions to setup a MOSIP enabled National ID integration.

Civil registration provides the source of truth for any vital event that occurs in a country. As a result is usual that an integration with a country's National ID system is requested.

We have some default functionality and some functionality that is unique to integrations with [MOSIP - an OpenSource platform for foundational ID](https://mosip.io/).

When creating a National ID client, you must give it a name. If you are installing OpenCRVS alongside MOSIP, enter "MOSIP" (without quotation) for the name, otherwise you can give it any name you like and take advantage of the default functionality explained below.

{% hint style="warning" %}
**You can only have one National ID client!**
{% endhint %}

<figure><img src="https://content.gitbook.com/content/YTKQAa9NKqMdS5tq1TB3/blobs/mBCwA5xRpbgojZkZcUMn/Screenshot%202023-01-16%20at%2016.31.32.png" alt=""><figcaption></figcaption></figure>

### Default functionality

Currently OpenCRVS supports the following default National ID integration functionality:

#### Birth events:

OpenCRVS can let a National ID system know of any birth that occurs in the country so that operations can be put in place to provide a National ID number for the child.

#### Death events:

OpenCRVS can let a National ID system know of any death that occurs in the country so that operations can be put in place to invalidate a National ID number for the deceased.

The default functionality dispatches the full payload at the moment of registration via the same process utilised by the webhook client. You can consider the National ID client as identical to a [webhook](/v1.6/technology/interoperability/webhook-clients.md) client with full payload permissions. To implement the National ID client, you must configure a webhook mediator service in exactly the same way for any other [webhook](/v1.6/technology/interoperability/webhook-clients.md) client.

{% hint style="info" %}
Example code for a mediator service that subscribes to an OpenCRVS National ID webhook is our [MOSIP Mediator](https://github.com/opencrvs/mosip-mediator)
{% endhint %}

###

### MOSIP functionality

MOSIP functionality contains the default functionality with some extra functionality unique to MOSIP requirements. For a detailed explanation refer to the [MOSIP OpenCRVS integration documentation](https://docs.mosip.io/1.2.0/integrations/mosip-opencrvs-integration).

#### Birth events:

OpenCRVS can let MOSIP know of any birth that occurs in the country so that operations can be put in place to provide a National ID number for the child. MOSIP integration requires installation assistance from our core team.

The [MOSIP Mediator](https://github.com/opencrvs/mosip-mediator) will return a unique token (**UINTOKEN**) that will be saved into the child's FHIR Patient details [here](https://github.com/opencrvs/opencrvs-farajaland/blob/1d8017657d074c9e83f07c01215ab4736e513d28/src/features/mediators/mosip-openhim-mediator/handler.ts#L26) as an additional identifier. **This token is unique for the individual for life**. In this way it can be used when the individual dies to connect the birth and death event together and invalidate a death.

The [MOSIP Mediator](https://github.com/opencrvs/mosip-mediator) will also return an application ID (**MOSIP\_AID**) that can be printed on a birth certificate using the certificate handlebar **{{mosipAid}}**. A baby is too young for biometrics to be captured in National ID processing, but this application ID allows the child's National ID application to be retrieved in the future and converted into a MOSIP National ID (VID / UIN) at any time.

#### Death events:

OpenCRVS can let a National ID system know of any death that occurs in the country so that operations can be put in place to invalidate a National ID number for the deceased.

{% hint style="danger" %}
When a MOSIP enabled National ID client is set up, at the point of death, the deceased's National ID number must be captured in the application form.
{% endhint %}

The deceased's National ID number (VID / UIN) is sent in a request to the [MOSIP Token Seeder](https://docs.mosip.io/1.2.0/integrations/mosip-token-seeder) (details below). [The (VID / UIN) is authorized and if valid a UINTOKEN is returned](https://github.com/opencrvs/opencrvs-core/blob/1e5834db765d469b728f0da1d47607c1d9c3f9f4/packages/workflow/src/features/registration/fhir/fhir-bundle-modifier.ts#L677). OpenCRVS then uses the UINTOKEN to link the death with the birth event before dispatching the death webhook.

{% hint style="info" %}
**By integrating OpenCRVS with MOSIP, we achieve a person-centric, longitudinal record of life events thanks to the MOSIP Token Seeder validation.**
{% endhint %}

{% hint style="warning" %}
If there is any failure communicating with MOSIP, the event creation will not be interrupted in OpenCRVS. This is to ensure that civil registration still occurs regardless of the current health of the MOSIP installation.
{% endhint %}

#### Installing a MOSIP enabled National ID configuration

If you are integrating with MOSIP, there are a few extra configuration steps in OpenCRVS that are required when setting up your servers and deploying.

1. Refer to the [MOSIP OpenCRVS Integration Documentation](https://docs.mosip.io/1.2.0/integrations/mosip-opencrvs-integration) to prepare MOSIP for OpenCRVS integration.
2. When setting up your OpenCRVS servers, you may need to provision a Wireguard VPN, and you ***will*** need a shared Docker volume to store some secret key files that MOSIP will supply you with. You will need to uncomment [these lines in the country configuration Ansible playbook](https://github.com/opencrvs/opencrvs-farajaland/blob/1d8017657d074c9e83f07c01215ab4736e513d28/playbook.yml#L61) before running the Ansible command in [this step](/v1.6/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.2-install-dependencies.md).
3. You will need to copy the secret key files that MOSIP will provide you with onto your server in this directory. The names of these files must match whatever you use in docker-compose in the next step.

   ```
   /data/secrets/mosip
   ```
4. Before you deploy, you will need to copy the [mosiptokenseeder](https://github.com/opencrvs/opencrvs-farajaland/blob/1d8017657d074c9e83f07c01215ab4736e513d28/docker-compose.countryconfig.demo-deploy.yml#L81) block from this demo docker-compose file into one of the docker-compose files relevant for your deployment (e.g. staging, qa or production)
5. Either add a block to docker-compose to host the [MOSIP Mediator](https://github.com/opencrvs/mosip-mediator) within the OpenCRVS stack, or alternatively host the Mediator on MOSIP's Kubernetes architecture making use of the Wireguard VPN. MOSIP can provide more support regarding this step.
6. When deploying OpenCRVS alongside MOSIP, the MOSIP team will provide you with a few extra secrets that are referenced in docker compose and supplied by deployment scripts in environment variables from Terminal. The following secrets must be added to your Github [**environment secrets** ](/v1.6/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.6-deploy-automated-and-manual.md)or exported as environment variables when [deploying OpenCRVS ](/v1.6/setup/3.-installation/3.3-set-up-a-server-hosted-environment/3.3.6-deploy-automated-and-manual.md)to your server.

<table><thead><tr><th width="417">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><pre><code>TOKENSEEDER_MOSIP_AUTH__PARTNER_MISP_LK
</code></pre></td><td>A MOSIP supplied secret key. It will look something like this: "rosxZG5q..."</td></tr><tr><td><pre><code>TOKENSEEDER_MOSIP_AUTH__PARTNER_APIKEY
</code></pre></td><td>A MOSIP supplied secret key. It will look something like this: "123..."</td></tr><tr><td><pre><code>TOKENSEEDER_CRYPTO_SIGNATURE__SIGN_P12_FILE_PASSWORD
</code></pre></td><td>A MOSIP supplied secret key. It will look something like this: "rosxZG5q..."</td></tr></tbody></table>

### Future National ID functionality

There are many other use cases that can be considered for future development of a more fully featured National ID integration with OpenCRVS such as:

**OSIA support**: In 2023 we plan to support an [OSIA standard](https://osia.readthedocs.io/en/v6.1.0/) National ID integration.

**Validation**: Validating all supplied National ID numbers with a National ID system before application submission and pre-populating CR application forms with demographic data returned by the NID system for informants and parents.

**Revocation**: Occasionally a death may be wrongly registered either fraudulently or by mistake. Any revocation in OpenCRVS should be communicated to the National ID system.

We are continually improving our National ID integration capabilities and look forward to addressing functionality such as this in future versions of OpenCRVS. For more information, please get in touch at: **<team@opencrvs.org>**


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/technology/interoperability/national-id-client.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
