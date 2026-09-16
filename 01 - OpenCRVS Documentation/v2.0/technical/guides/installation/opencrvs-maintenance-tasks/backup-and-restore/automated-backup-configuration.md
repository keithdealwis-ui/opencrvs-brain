---
title: "Automated backup configuration"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/automated-backup-configuration"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/automated-backup-configuration.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f5ff6630da4b6e2e052f7de9e5260becfcee0b557de708e69f56bc32c687431b"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/automated-backup-configuration.md).

# Automated backup configuration

### Automated backup configuration

If backup server is in your environment inventory file then add following section to `environments/<environment>/dependencies/values.yaml` and run "Deploy dependencies" workflow:

* Update `backup_server_dir` value to match with your environment name, e/g `development`
* Update `schedule` to reflect best time backup job to be started,
* Set `enabled` to `true`

```
# Backup configuration
backup:
  enabled: true
  schedule: "0 1 * * *"
  backup_server_dir: /home/backup/<environment>
```

Push your changes to GitHub and Re-[Deploy Dependencies](/technical/guides/installation/deploy-set-up-a-server-hosted-environment/deploy/running-a-dependencies-deployment.md)

If backup server was provisioned as part of any other environments or is a third-party server, then please follow guide from helm chart, see [Backup configuration](https://github.com/opencrvs/opencrvs-core/blob/develop/charts/dependencies/README.md#backup-configuration).

### Verify backup configuration

**Verify kubernetes jobs are present:**

1. Connect to your cluster with `kubectl`
2. Run following command:

   ```
   kubectl get cronjob -l job-type=backup -n opencrvs-deps-<environment>
   ```

   Example output:

   ```
   NAME              SCHEDULE    TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
   influxdb-backup   0 1 * * *   <none>     False     0        5h9m            20h
   minio-backup      0 1 * * *   <none>     False     0        5h9m            13h
   mongodb-backup    0 1 * * *   <none>     False     0        5h9m            20h
   postgres-backup   0 1 * * *   <none>     False     0        5h9m            20h
   ```

**Verify Kubernetes jobs were executed per schedule:**

Wait at least for first job execution, usually takes at to 24 hours

1. Connect to your cluster with `kubectl`
2. Run following command:

   ```
   kubectl get job -l job-type=backup -n opencrvs-deps-<environment>
   ```

   Example output:

   ```
   NAME                       STATUS     COMPLETIONS   DURATION   AGE
   influxdb-backup-29381820   Complete   1/1           9s         5h11m
   minio-backup-29381820      Complete   1/1           9s         5h11m
   mongodb-backup-29381820    Complete   1/1           31s        5h11m
   postgres-backup-29381820   Complete   1/1           13s        5h11m
   ```

Verify backup files are present on backup server

1. SSH (Login) to backup server
2. Become backup user:

   ```
   sudo -i
   su - backup
   ```
3. Check backup directory content:

   ```
   ls -l /home/backup/<environment>
   ls -l /home/backup/<environment>/<date>
   ```

   Example output:

   ```
   backup@backup-01:~$ ls -l /home/backup/production/2025-11-12
   total 25972
   -rw-r--r-- 1 backup backup    74704 Nov 12 01:00 influxdb_backup_2025-11-12.tar.gz.enc
   -rw-r--r-- 1 backup backup 26506864 Nov 12 01:00 minio_backup_2025-11-12.tar.gz.enc
   -rw-r--r-- 1 backup backup      464 Nov 12 01:00 mongo_backup_2025-11-12.tar.gz.enc
   -rw-r--r-- 1 backup backup      448 Nov 12 01:00 postgres_backup_2025-11-12.tar.gz.enc
   ```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/automated-backup-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
