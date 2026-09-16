---
title: "SSH access"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ssh-access"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ssh-access.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:6bb348280ada003247a84235f2573f3c7873d9eac731e085165d06e523cf4d8a"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ssh-access.md).

# SSH access

### Managing ssh access

{% hint style="info" %}
`yarn environment:init` script automatically handles this configuration you, check the [Create a Github Environment](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/create-a-github-environment.md) step.
{% endhint %}

SSH Access is configured at inventory file (`infrastructure/server-setup/inventory/<environment>.yml`)

Configuration file has special section `users`, following options are available:

* name: OS login user name
* ssh\_keys: List of public ssh keys for user, all keys are added to `~/.ssh/authorized_keys`
* state: Enable or disable remote access for the user. Allowed values are:
  * `present`: user is allowed to login
  * `absent`: user account is disabled
* role:
  * `operator`: grant read only access to OS and full access to kubernetes cluster
  * `admin`: grant full access to OS and kubernetes cluster

Here is example of configuration file for user `bob`:

```yaml
# users: Add as many users as you wish
users:
# Configuration example
- name: bob
  ssh_keys:
    - "ssh-ed25519 AAA...Q bob@opencrvs.org"
    - "ssh-ed25519 AAA...Q bob@aol.com"
  state: present
  # Allowed states:
  # - present: user is allowed to login
  # - absent: user account is disabled

  role: admin
  # Allowed roles:
  # - operator: grant read only access to OS and full access to kubernetes cluster
  # - admin: grant full access to OS and kubernetes cluster
```

### 2FA SSH Access

Now that your servers are provisioned you can SSH in using either the IP address or the domain, plus your username as it is configured in inventory files. The first time you do so you will be required to set up 2FA for your server administrators.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-bbb8e187e1403a02e7497ec9ca9000222120a76e%2FScreenshot%202024-02-13%20at%2015.51.38.png?alt=media" alt=""><figcaption></figcaption></figure>

You must have the Google Authenticator app on your mobile phone. You can download this from the Google Play Store or Apple App Store.

Scan the QR code to add the server as an option in Google Authenticator, then enter the 6-digit 2FA code that is generated to access the server.

For all the initial set-up questions that are asked, accept defaults by typing "y"

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-0685bc52f2a6dde4ebb12da39ff127c94c960eca%2FScreenshot%202024-02-13%20at%2015.52.40.png?alt=media" alt=""><figcaption><p>QR Code for Google Authenticator</p></figcaption></figure>

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-0493d52aa78fd4ca9b5b93fcb4d0c84a2fc67ea4%2FScreenshot%202024-02-13%20at%2015.52.57.png?alt=media" alt=""><figcaption><p>Accept defaults</p></figcaption></figure>

You will also notice that root SSH access is now disabled as a security posture.

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-8a73b230f7cfbfd5a968bc47ae60246326ad85c3%2FScreenshot%202024-02-13%20at%2015.57.53.png?alt=media" alt=""><figcaption></figcaption></figure>

### Removing SSH Access for a user

If a server administrator needs to be removed from having SSH access to a server, these are the steps you need to take:

1. In the inventory file for the server, find the user block for the user you wish to remove and set the value **state** to **absent**: \[TODO: fix screenshot]

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-64abeba393d7629ac25a2169223aca23ae893908%2FScreenshot%202024-11-13%20at%2018.31.49.png?alt=media" alt=""><figcaption></figcaption></figure>

```
state: absent
```

2. Commit the updated inventory file to Git
3. Run the Provision action for the environment with just the "**users**" task selected. It is quicker and less intensive than selecting "all"

<figure><img src="https://3593002492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTIJguU5Pzi7HeHrkXa4I%2Fuploads%2Fgit-blob-4c0f2f3eb83883ff21e75fea2b6730ca9f1a38f1%2FScreenshot%202024-11-13%20at%2018.34.42.png?alt=media" alt=""><figcaption><p>Running the users task updates all users on the server. If a user is marked as absent, they will be deactivated</p></figcaption></figure>

4. Now the user will no longer have SSH access to the server
5. You can delete their block entirely from inventory files and commit the file to Git if you wish.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ssh-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
