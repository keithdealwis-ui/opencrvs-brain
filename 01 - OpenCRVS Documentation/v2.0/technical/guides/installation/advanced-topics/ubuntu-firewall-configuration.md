---
title: "Ubuntu Firewall configuration"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-firewall-configuration"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-firewall-configuration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:dda075ace418b99c2e060990bf4fc91112d7f71b75e620cedc654ae315fd33ec"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-firewall-configuration.md).

# Ubuntu Firewall configuration

### Overview

The firewall follows a default-deny approach:

* All inbound traffic is denied by default.
* Only ports required for cluster operation are opened.
* Firewall rules are managed automatically by Ansible.
* Existing OpenCRVS-managed rules are removed and recreated during each deployment to ensure configuration consistency.

### Unrestricted access

* `SSH`: All nodes allow inbound SSH connections on TCP port 22.
* `HTTP/HTTPS`: Control plane node (master) allows inbound traffic on 80 and 443 ports. These ports are used by Traefik to expose OpenCRVS services.

### Kubernetes API

Control plane node allows access to the Kubernetes API server on TCP port 6443 from:

* All Kubernetes cluster nodes
* Additional CIDR ranges specified through the `kubernetes_api_allowed_cidrs` configuration option

This allows cluster components to communicate with the API server while enabling operators to restrict administrative access to trusted networks.

### Internal Cluster Communication

OpenCRVS automatically discovers all Kubernetes node IP addresses and creates firewall rules allowing communication between cluster members only.

The following ports are opened between cluster nodes:

| Port  | Protocol | Purpose                         |
| ----- | -------- | ------------------------------- |
| 6443  | TCP      | Kubernetes API Server           |
| 10250 | TCP      | Kubelet API                     |
| 10251 | TCP      | kube-scheduler                  |
| 10252 | TCP      | kube-controller-manager         |
| 179   | TCP/UDP  | Calico BGP                      |
| 4789  | UDP      | Calico VXLAN overlay networking |
| 7946  | TCP/UDP  | Cluster networking components   |
| 8472  | UDP      | VXLAN overlay networking        |

{% hint style="info" %}
`etcd` communication ports (2379 and 2380) are not exposed publicly and are intended only for control plane communication within the cluster.

To support Calico networking, inbound traffic is allowed on the following interfaces:

* `cali+`
* `vxlan.calico`
  {% endhint %}

### Configuration options

| GitHub variable/secret    | Ansible variable          | Description                                                                                                         |
| ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| KUBE\_API\_HOST           | kube\_api\_host           | Kubernetes master node IP / Hostname                                                                                |
| KUBE\_API\_ALLOWED\_CIDRS | kube\_api\_allowed\_cidrs | Subnets approved to access Kubernetes API server (master). Comma-separated list (e/g: `10.0.0.0/16,192.168.0.0/24`) |
| KUBE\_WORKER\_NODES       | n/a                       | Kubernetes worker nodes. Comma-separated list (e/g: `10.0.0.2,10.0.0.3,10.0.0.4`)                                   |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/ubuntu-firewall-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
