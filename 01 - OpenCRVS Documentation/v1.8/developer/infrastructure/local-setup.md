---
title: "Local Setup"
source_url: "https://documentation.opencrvs.org/v1.8/developer/infrastructure/local-setup"
markdown_url: "https://documentation.opencrvs.org/v1.8/developer/infrastructure/local-setup.md"
version: "v1.8"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:986ca11d43d9301d2bc088c8c1153318736c8e22a2d6f582cf4e84b17d61fd32"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.8/developer/infrastructure/local-setup.md).

# Local Setup

Setting up OpenCRVS servers locally allows infrastructure developers to experiment with provisioning and deployment automation in a safe environment, without needing to perform real deployments to remote servers. It enables quick iteration on Ansible playbooks, inventory configurations, and service orchestration, providing hands-on experience with how the infrastructure is composed and managed.

This guide will help you set up the OpenCRVS infrastructure locally for development and testing purposes. It covers all essential steps, from cloning the country configuration repository to provisioning servers.

### Prerequisites

Before you begin, ensure you meet the following requirements:

* At least **30 GB** of free disk space
* A Unix-based operating system (Linux or macOS)
* 16GB or more memory
* Make sure Python and pip are installed on your system

***

### Step 1: Clone the Country Configuration Repository

Start by cloning the [OpenCRVS Country Configuration](https://github.com/opencrvs/opencrvs-countryconfig) repository to your local machine.

#### Git Command:

```bash
git clone https://github.com/opencrvs/opencrvs-countryconfig.git
cd opencrvs-countryconfig
```

***

### Step 2: Install a Virtual Machine Manager

Depending on your operating system, install the appropriate virtualisation tool:

* **Linux**: [Multipass](https://multipass.run/)
* **macOS**: [OrbStack](https://orbstack.dev/)

These tools are used to provision lightweight virtual machines for running OpenCRVS services.

***

### Step 3: Install Ansible

Ensure [Ansible](https://www.ansible.com/) is installed to run the infrastructure provisioning scripts.\
Follow the [official Ansible installation guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) for your OS.

***

### Step 4: Run the Provisioning Notebook in VS Code

Open the provisioning Jupyter notebook in Visual Studio Code to automate the infrastructure setup process.

#### Instructions:

1. Create and activate a virtual Python environment:

   ```bash
   python3 -m venv ~/.venv/opencrvs
   source ~/.venv/opencrvs/bin/activate  
   ```
2. Install `ipykernel` in your virtual environment:

   ```bash
   pip install ipykernel
   python3 -m ipykernel install --user --name=opencrvs
   ```
3. Ensure the Jupyter extension is installed in VS Code.
4. Open the following notebook file:

   ```bash
   opencrvs-countryconfig/infrastructure/local-development/provision.ipynb
   ```
5. Select the `venv` kernel and run each cell sequentially to provision your local OpenCRVS environment.

If you haven’t used Jupyter in VS Code before, follow [this guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to get started.

***

### ✅ You're Ready!

After these steps, your local OpenCRVS environment will be up and running—ready for testing, development, or configuration exploration.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.8/developer/infrastructure/local-setup.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
