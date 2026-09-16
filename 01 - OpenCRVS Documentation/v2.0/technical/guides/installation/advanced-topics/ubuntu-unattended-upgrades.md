---
title: "Ubuntu unattended-upgrades"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-unattended-upgrades"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-unattended-upgrades.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:feedbd46b1549baf563c492b22a27ca83df6cdfd85964a9aeca6235a6698dab1"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-unattended-upgrades.md).

# Ubuntu unattended-upgrades

### General information

OpenCRVS infrastructure uses Ubuntu unattended-upgrades to automatically install operating system updates while preventing automatic upgrades of Kubernetes components.

The following updates are installed automatically through unattended-upgrades:

* Ubuntu package updates from the operating system repositories
* Ubuntu security updates
* Ubuntu Pro ESM application security updates (if enabled)
* Ubuntu Pro ESM infrastructure security updates (if enabled)

OpenCRVS configures unattended-upgrades to automatically remove unused kernel packages and obsolete dependencies.

Automatic server reboots are disabled by default.

Kubernetes packages are explicitly excluded from unattended-upgrades:

* kubeadm
* kubelet
* kubectl
* kubernetes-cni

Kubernetes upgrades must be performed manually using the OpenCRVS GitHub provisioning workflow.

This prevents unexpected Kubernetes version changes and allows operators to upgrade cluster nodes in a controlled manner.

### Checking upgrade status

Review unattended-upgrades logs:

```bash
sudo journalctl -u unattended-upgrades
```

View recent unattended-upgrades activity:

```bash
sudo tail -f /var/log/unattended-upgrades/unattended-upgrades.log
```

Display effective unattended-upgrades configuration:

```bash
apt-config dump | grep Unattended-Upgrade
```

Perform a dry run:

```bash
sudo unattended-upgrade --dry-run --debug
```

### Upgrading Kubernetes

Kubernetes upgrades should be performed using the OpenCRVS GitHub provisioning workflow.

The workflow upgrades Kubernetes packages and applies any required cluster changes in a controlled and supported manner.

Refer to [provision](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers.md) documentation and Release Notes for more information.

Refer to the Kubernetes upgrade documentation for version-specific instructions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-unattended-upgrades.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
