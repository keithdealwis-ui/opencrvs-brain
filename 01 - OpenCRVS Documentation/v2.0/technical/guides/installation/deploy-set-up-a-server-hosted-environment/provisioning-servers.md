---
title: "Provisioning servers"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:8c73f2babb4a33bc9fd1bca4e535b48d3c62b66e16e6bc8940068730c1ed300a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers.md).

# Provisioning servers

## 4.3.3 Provisioning servers

Now that your Github environments are set up you can proceed to provision your servers using our automated ["Ansible"](https://www.ansible.com/) powered actions.

The Provision environment action will automate a large number of installation and sysadmin [tasks](https://github.com/opencrvs/infrastructure/tree/develop/infrastructure/server-setup/tasks) on your servers. Refer to the directories in order to understand each task.

{% hint style="danger" %}
**IMPORTANT SERVER ACCESS NOTE**: As a security step, the Ansible script will disable root SSH access to your server and all password access for SSH users. [SSH key](https://www.ssh.com/academy/ssh-keys) authentication is then enforced using the public keys for the users in your inventory files.

Additionally. SSH users will be required to install [**Google Authenticator**](https://en.wikipedia.org/wiki/Google_Authenticator) and use a 2FA code to access. SSH access procedures to a server after Provisioning completes. This is explained here. Refer to [SSH Access](/technical/guides/installation/advanced-topics/ssh-access.md)
{% endhint %}

{% hint style="warning" %}
Provision scripts includes Kubernetes cluster upgrade playbook (see tags `all` and `k8s`). OpenCRVS application will not be available during cluster upgrades.
{% endhint %}

### Provision infrastructure

Click on the "Actions" tab in Github and select the "Provision environment" action. Click the "Run workflow" button.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-3db32900c40f1c9e3c2955174e95cfd8cd8859f8%2Fimage%20(16).png?alt=media" alt=""><figcaption></figcaption></figure>

* In the "Machine to provision" select your target environment, E/g: "**qa**".
* In the "Select group tag you want to execute" select, choose "**all**". All other options will work properly after first provision
* Click the green "Run workflow" button to commence the provisioning of this server.
* If you have enabled the approval step for production environments, an issue will open requiring your list of users to approve the running of the action by commenting as described within the issue. See below ...

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-abd9c27db32ae777351beb06e364abb20cc5c7e4%2FScreenshot%202026-02-27%20at%2015.08.00.png?alt=media" alt=""><figcaption><p>An automated issue will open requiring approval for any action to run in an environment where this process has been enabled.</p></figcaption></figure>

The process can take anything up to around **20-30** minutes to complete.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-5fa9fad580425a3ba43599aaffa4c387d1fd5670%2FScreenshot%202024-11-13%20at%2008.13.37.png?alt=media" alt=""><figcaption><p>Github Action logs can help you debug any issues. In this example a package installation was interrupted - perhaps due to a random Network error. ChatGPT can help you understand any errors you may encounter and potential steps to resolve them. Error messages often explain to you the solution required.</p></figcaption></figure>

If you see a red cross, it means that a certain step failed and requires to be debugged. There might be a problem with your data center, your Ansible inventory files, your Github environment secrets, or there may be network connectivity issues.

{% hint style="info" %}
Ansible will perform a huge amount of Ubuntu commands that you would normally be required to run manually one-by-one. It saves you a large amount of time.

If the Provision action fails, try re-running it before investigating further, as failures could be due to network conditions. If it fails at the same point each time, then a legitimate bug requires investigation.

You will need experience with Ubuntu and confidence with servers to debug any issues. In the above example, the solution was as simple as SSH-ing into the server and running the command as instructed in the error message, then re-running the Provision action again.

Reach out in [Github Discussions](https://github.com/opencrvs/opencrvs-core/discussions) if you have a question.
{% endhint %}

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-989bb5b8fa8aff73243960cd56f2b6b3f7f00257%2FScreenshot%202024-11-13%20at%2008.38.28.png?alt=media" alt=""><figcaption><p>Success!</p></figcaption></figure>

If the server provisioning works, you will eventually see a green tick to mark that the server provisioned successfully.

## Provision verification steps

* [ ] Kubernetes self-hosted runner is visible under **Settings → Actions → Runners** on GitHub.
* [ ] You should be able to ssh (login) on the server with any user account defined under `users` section of the inventory file.
* [ ] You should have access to kubernetes cluster after ssh (login). Command to verify: `kubectl config current-context` and locally, check [Kubernetes cluster access](/technical/guides/installation/advanced-topics/kubernetes-cluster-access.md)

## Ansible tasks explained

In the "Select group tag you want to execute" select, when you choose "**all**", you are instructing Ansible to run every one of the infrastructure task commands listed in the [**infrastructure/server-setup/tasks**](https://github.com/opencrvs/opencrvs-countryconfig/tree/develop/infrastructure/server-setup/tasks) directory and explained in this [list](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers/ansible-tasks-when-provisioning.md).

It is possible for you to choose to run any one of these tasks individually at any time, such as an example given when refreshing [static TLS certificates](/technical/guides/installation/advanced-topics/tls-ssl-configuration-for-traefik/static-tls-certificates.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
