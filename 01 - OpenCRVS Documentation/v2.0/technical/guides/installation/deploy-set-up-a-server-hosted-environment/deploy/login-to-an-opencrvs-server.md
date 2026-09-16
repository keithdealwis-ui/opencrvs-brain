---
title: "Login to an OpenCRVS server"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/login-to-an-opencrvs-server"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/login-to-an-opencrvs-server.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:13a4c40a2dc4d97004083ae20e6c13b966f56335a99b3f062b1ad8eefbbaac2a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/login-to-an-opencrvs-server.md).

# Login to an OpenCRVS server

Now that your database is seeded with your users you should be able to browse to OpenCRVS to login.

**<https://login.\\><your-domain>**

For **development** & **qa** environments, your test employees ([default-employees.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/develop/src/data-seeding/employees/source/default-employees.csv)) can log straight into your application with 2FA and notifications disabled and the username and password that exists in the csv.

### Staging or production environments

For **staging** & **production** environments, your production National System Administrator employee ([prod-employees.csv](https://github.com/opencrvs/opencrvs-countryconfig/blob/develop/src/data-seeding/employees/source/prod-employees.csv)) must immediately login and change the csv password to a strong, minimum 12 character long password.

Then the user will be logged out and will have to login again with 2FA and notifications enabled.

{% hint style="warning" %}
This is your first test of your SMTP service. The National System Administrator should receive an email containing the 2FA code. Emails can end up in your Spam folder so please check and advise staff accordingly.
{% endhint %}

Once logged in, the National System Administrator can create team members through the user interface.

### Debugging first login issues and data-seeding

On fresh environments login issue may happen due to unsuccessful [data seeding](/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md).

Check data seed logs in Kibana **Observability > Discover** by filtering:

```
kubernetes.container.name : "data-seed"
```

Data seed is short living job and sometimes logs might be missed from Kibana, in that case check container logs by running:

```
kubectl logs job/data-seed -n opencrvs-<env>
```

`<env>` is your environment name.

Example of succesfull data seed job execution log:

```
yarn run v1.22.22
$ NODE_OPTIONS=--dns-result-order=ipv4first ts-node -r tsconfig-paths/register src/index.ts
Seeding locations
Seeding users
Done in 9.15s.
```

If for some reason data seed job was not executed or failed at installation time, please check [Seeding a server environment](/technical/guides/installation/opencrvs-maintenance-tasks/seeding-a-server-environment.md) to get more information how to re-run job.

### Debugging SMTP

If there is an issue and you are not receiving emails, this is a good opportunity to learn about monitoring and debugging your OpenCRVS installation.

To learn more about OpenCRVS monitoring and maintenance, visit the [monitoring](https://github.com/opencrvs/documentation/tree/master/v1.8.0/setup/7.-monitoring) section.

As the SMTP API was configured in the countryconfig service, you can filter the appropriate logs in Kibana in the **Observability > Discover** section like so:

```
kubernetes.container.name : "countryconfig"
```

As you browse the logs you are looking for 500 errors and you can respond to any SMTP service error messages that you see appropriately. Perhaps you need to change the Github Action secrets. [Running a deployment ](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-opencrvs-deployment.md)of OpenCRVS will refresh all microservices and so this is required when secrets are updated.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/login-to-an-opencrvs-server.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
