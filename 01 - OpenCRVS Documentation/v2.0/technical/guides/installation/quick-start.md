---
title: "Quick Start"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/quick-start"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/quick-start.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:5e6171776d7f822b2fdc4b0393e49125cc28d03af1fb7e62178f5821b526374c"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/quick-start.md).

# Quick Start

### Create a country configuration

```
npm create @opencrvs/countryconfig@latest <project-name>
```

This command creates a country configuration package with a minimal example configuration.

### Run local development environment

Make sure all prerequisites are installed, see [opencrvs-countryconfig](https://github.com/opencrvs/opencrvs-countryconfig/#prerequisites)

Navigate to `<project-name>-countryconfig`

Start development environemnt:

```
tilt up
```

Open the Tilt UI:

```
http://localhost:10350
```

Wait until the main resources are running.

Then run the data seed task from the Tilt UI:

1. Open <http://localhost:10350>
2. Find the `2.Data-tasks` section
3. Run the `data-seed` or `clean-&-seed` resource
4. Wait until the job completes

Open OpenCRVS: <http://opencrvs.localhost>

Thats it! 🎉

### Further reading on data seeding

Data seeding is the process of installing into OpenCRVS databases, the reference data for general configuration of the application. Seeding is a one-time process. A server or your localhost must be entirely cleared of all data before it can be seeded again.

Data seeding uses a temporary superuser and our APIs to create all of the above. This superuser is created in data migrations that run when OpenCRVS starts up. At the end of data seeding, the superuser is deactivated.

On a deployed server environment, Github Action workflows perform this task. You will learn about them later when provisioning a server.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/quick-start.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
