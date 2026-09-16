---
title: "Disk encryption"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-encryption"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-encryption.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:ffe0c4cc9bd839f176c91564ad60c7c158b1551ca3c5b2f388222681c1fcb15b"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-encryption.md).

# Disk encryption

### Disk Encryption Overview

#### Why Disk Encryption Is Needed

Disk encryption protects citizens’ data if someone gains physical access to a server or storage device.

OpenCRVS disk encryption is required only for data centres that do not already provide hardware-backed, platform-level, or equivalent disk encryption. If the hosting environment already encrypts disks securely, this OpenCRVS-level encryption may not be needed.

#### LUKS In Brief

OpenCRVS uses LUKS, the standard Linux disk encryption mechanism.

LUKS encrypts a block device or disk image and only makes its contents readable after it is unlocked with the correct passphrase. After unlock, the encrypted storage is mounted like a normal filesystem.

#### Why The Encryption Key Must Be Protected

The encryption key unlocks the citizens’ data partition.

If the encrypted disk is stolen without the key, the data remains protected. If both the disk and the key are stored together, encryption provides little protection. For this reason, the key should be stored in a safe location separate from the encrypted data whenever possible.

### OpenCRVS Encrypted Partition

OpenCRVS stores encrypted data in:

```
/cryptfs_file_sparse.img
```

At runtime, this encrypted storage is mounted to:

```
/data
```

OpenCRVS data services use `/data` after it has been mounted.

#### Encryption Key Location

For environments without a backup server, the disk encryption key is stored locally on the Kubernetes master node:

```
/root/disk-encryption-key.txt
```

For staging and production environments with a backup server, the disk encryption key is stored on the backup server in encrypted form and retrieved during boot:

```
/home/backup/disk-encryption-key.txt.enc
```

{% hint style="info" %}
Disk encryption key is encrypted with backup encryption key.

Backup encryption key is stored on Kubernetes master node to ensure there is no way to decrypt stolen backups.
{% endhint %}

#### Host Boot Order

When disk encryption is enabled, the host must start services in this order:

1. Networking starts.
2. The encrypted partition is unlocked and mounted to `/data`.
3. Kubernetes services start.

This prevents Kubernetes workloads from starting before citizens’ data storage is available.

#### Troubleshooting

Check that `/data` is mounted:

```
mountpoint /data
```

Check decrypt-on-boot logs:

```
sudo systemctl status reboot.service
sudo journalctl -u reboot.service -b
```

Check that the LUKS header accepts the expected passphrase before rebooting or changing keys.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/advanced-topics/disk-encryption.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
