---
title: "Provision settings"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers/provision-settings"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers/provision-settings.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:68333b4b16ff22641636681f7442e7c2f453ab9fc0bf0e254ef4461dfb6c4acd"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers/provision-settings.md).

# Provision settings

## Advanced Provision Configuration

OpenCRVS infrastructure provisioning can be customised using the following configuration file:

```
infrastructure/server-setup/group_vars/all.yml
```

This file contains advanced Ansible configuration used during:

* server provisioning
* Kubernetes installation
* backup configuration
* disk encryption setup
* networking configuration
* Kubernetes cluster tuning

Most deployments can use the default values provided by the repository.\
Advanced users may customise these values to adapt provisioning for their infrastructure requirements.

### Examples Common configuration options

{% hint style="info" %}
This file contains many additional variables and configuration options not documented here.\
Refer directly to:

```
infrastructure/server-setup/group_vars/all.yml
```

for the complete list of supported variables.
{% endhint %}

#### Kubernetes Version

Defines versions for:

* kubeadm
* kubelet
* kubectl

```yaml
kubernetes_version: "v1.35"
```

Changing this value upgrades the Kubernetes components installed during provisioning. **Downgrades are not supported to ensure environment stability**.

#### Kubernetes Eviction Policy

OpenCRVS recommends configuring Kubernetes eviction policies using absolute disk sizes instead of percentages.

This helps prevent:

* unexpected pod evictions
* failed upgrades
* disk exhaustion

Example:

```yaml
eviction_hard_nodefs: "10Gi"
eviction_hard_imagefs: "10Gi"

eviction_soft_nodefs: "20Gi"
eviction_soft_imagefs: "20Gi"
```

Recommended minimum:

* 10Gi free disk space for stable operation
* 20Gi soft threshold for proactive cleanup

### Backup Configuration

Backup retention can be configured using:

```yaml
amount_of_backups_to_keep: 7
```

This example keeps one week of backups.

### Disk Encryption Configuration

Example encryption configuration:

```yaml
disk_encryption_key_path: /root/disk-encryption-key.txt
data_file_path: /cryptfs_file_sparse.img
```

> \[!WARNING]\
> The example configuration stores encryption keys locally on the server.\
> Production environments should use a Hardware Security Module (HSM) or external secret management solution.

### Minimum Disk Space Requirement

Provisioning validates available disk space before Kubernetes installation.

```yaml
min_free_disk_size: "30g"
```

This helps avoid installation failures caused by insufficient storage.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/deploy-set-up-a-server-hosted-environment/provisioning-servers/provision-settings.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
