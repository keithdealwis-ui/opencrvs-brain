---
title: "Workflow management"
source_url: "https://documentation.opencrvs.org/v1.9/product-specifications/workflow-management"
markdown_url: "https://documentation.opencrvs.org/v1.9/product-specifications/workflow-management.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:b6ea2506e6f39805e15bc6dfe5ba55524197eb5ccaae34fcf7a509263908140f"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/product-specifications/workflow-management.md).

# Workflow management

## Workqueues

Declarations are organised in each Registration Office into separate work queues based so they can easily prioritise and manage their workload.\
\
Workqueues are configurable for each user role allowing you to configure custom record workflows

For a comprehensive understanding of the various statuses and the potential pathways a record can follow, please refer to the [Status Flow Diagram](/v1.9/product-specifications/status-flow-diagram.md)\
\
The following example workqueues have been configured for Farajaland:

### Draft

Shown if a user has `scope:record.create[event=event]` . To list all saved draft declarations

### **Notifications**

To list all notifications sent by a user or external system eg. a health system.

### Sent for review

To list all declarations that have been notified or declared by the user

### Ready for review

To list all declarations that are ready for review, potential duplicates or a correction has been requested

### **Requires updates**

To list all records that were rejected

### **Sent for approval**

To list all records validated by the user

### **Ready to print**

To list all recently registered records which have not been certified.

***

## Outbox

This workqueue is for the system to process status changes to a record. It provides all users with the freedom to continue creating and reviewing declarations without the constraint of a stable internet connection, thereby ensuring a consistent and uninterrupted workflow.

For instance, Field Agents have the ability to create declarations offline. Once internet connectivity is reestablished, the Outbox automatically synchronises these offline declarations with the server, forwarding them to the Registration Office. Likewise, a Registration Agent can review a declaration offline, send it for approval, and promptly proceed to review another declaration that they have pre-allocated.

The Outbox instills a sense of confidence among users by securely storing declarations, ensuring they are processed promptly upon reconnection to the internet. This feature effectively mitigates the risk of losing valuable data due to intermittent connectivity, providing users with peace of mind.

## Assigning records

When a user assigns a declaration to themselves, it is download to their device, allowing them to perform actions offline such as making updates and reviewing. This precautionary measure prevents potential conflicts that could arise if two users attempt to edit the same record concurrently.

When a record is assigned to a user, its ‘assigned’ status becomes visible to other system users in the workqueues, indicated using their profile icon. Only a Registrar possesses the authority to unassign a user from a record. However, executing this action will result in the loss of any modifications made by the assigned user.

In conjunction with the Outbox, this assignment feature fosters a resilient system, well-equipped to support operations in low-connectivity or offline scenarios.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/product-specifications/workflow-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
