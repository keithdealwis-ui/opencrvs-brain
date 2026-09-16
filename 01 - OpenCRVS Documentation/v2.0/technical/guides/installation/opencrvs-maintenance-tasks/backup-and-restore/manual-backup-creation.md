---
title: "Manual backup creation"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-backup-creation"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-backup-creation.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:41ccdb5e738afb9198b99194c4e06afe3c546769aa15f2a2ebfe46afe8fcd18d"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-backup-creation.md).

# Manual backup creation

### Before you begin

Manual backup process assumes automated backup workflow is already configured and working properly.

Manual backup process invokes same Kubernetes cronjobs as for automated process.

Reasons for manual backup:

* Before environment reset
* Before OpenCRVS or dependencies upgrade
* Migration to new hardware or cloud
* Off-boarding from OpenCRVS

Following components are backed up:

* MongoDB
* PostgreSQL
* MinIO
* InfluxDB

### Running all components backup

1. Connect to your cluster with `kubectl`
2. Change namespace to opencrvs-deps-\<environment>:

   ```
   kubectl config set-context --current --namespace=opencrvs-deps-<environment>
   ```
3. Run following command to trigger backup jobs for all components:

   ```
   for cj in $(kubectl get cronjob -l job-type=backup -o jsonpath='{.items[*].metadata.name}'); do \
     kubectl delete job $cj-job --ignore-not-found; \
     kubectl create job --from=cronjob/$cj $cj-job; \
   done
   ```

   Example output:

   ```
   job.batch "influxdb-backup-job" deleted
   job.batch/influxdb-backup-job created
   job.batch "minio-backup-job" deleted
   job.batch/minio-backup-job created
   job.batch "mongodb-backup-job" deleted
   job.batch/mongodb-backup-job created
   job.batch "postgres-backup-job" deleted
   job.batch/postgres-backup-job created
   ```
4. Verify all jobs completed without issues:<br>

   ```
   kubectl get job -ljob-type=backup
   ```

   Example output: Check job names like `*-backup-job` without ending number, jobs with number were triggered per schedule:

   ```
   NB01NSTL012:~ vmudryi$ kubectl get job -ljob-type=backup
   NAME                       STATUS     COMPLETIONS   DURATION   AGE
   influxdb-backup-29384700   Complete   1/1           12s        6h9m
   influxdb-backup-job        Complete   1/1           12s        2m31s
   minio-backup-29384700      Complete   1/1           9s         6h9m
   minio-backup-job           Complete   1/1           10s        2m30s
   mongodb-backup-29384700    Complete   1/1           18s        6h9m
   mongodb-backup-job         Complete   1/1           16s        2m29s
   postgres-backup-29384700   Complete   1/1           12s        6h9m
   postgres-backup-job        Complete   1/1           12s        2m28s
   ```
5. SSH (Login) to backup server and verify backup was completed successfully.

### Running Single component (MongoDB) backup

1. Connect to your cluster with `kubectl`
2. Change namespace to opencrvs-deps-\<environment>:

   ```
   kubectl config set-context --current --namespace=opencrvs-deps-<environment>
   ```
3. Run following command to trigger MongoDB backup:

   ```
   kubectl create job \
     --from cronjob/mongodb-backup mongodb-backup-manual
   ```

   Example output:

   ```
   job.batch/mongodb-backup-manual created
   ```
4. Verify MongoDB backup completed successfully:

   ```
   kubectl logs -f job/mongodb-backup-manual
   ```

   Example output:

   ```
   [2025-11-12 07:01:38] Starting MongoDB backup script
   ...
   [2025-11-12 07:01:52] Encrypted backup file /tmp/mongo_backup_2025-11-12.tar.gz.enc transferred to backup host 10.2.0.3:/home/backup/production/2025-11-12
   ```

### Verify backup was created

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
   backup@tmp-backup:~$ ls -l /home/backup/production/2025-11-12
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
GET https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-backup-creation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
