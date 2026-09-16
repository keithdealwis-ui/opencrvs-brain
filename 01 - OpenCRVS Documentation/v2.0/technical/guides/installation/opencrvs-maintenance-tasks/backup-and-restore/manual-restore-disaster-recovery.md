---
title: "Manual restore / Disaster recovery"
source_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-restore-disaster-recovery"
markdown_url: "https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-restore-disaster-recovery.md"
version: "v2.0"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:930d857730424523c21b3cfc634bcd18351d37add3389e377884794c883691ca"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-restore-disaster-recovery.md).

# Manual restore / Disaster recovery

### Before you begin

Manual restore process assumes automated backup workflow was already configured and at least one working backup copy exists.

Following components are supported by restore process:

* MongoDB
* PostgreSQL
* MinIO
* InfluxDB

Manual restore process invokes same Kubernetes cronjobs as for automated process. Manual restore process can be executed on environment with configured automated restore or even without automated restore configured.

Usually reasons for manual restore:

* After environment reset
* After OpenCRVS or dependencies upgrade/rollback when data was corrupted
* Migration to new hardware or cloud
* Disaster recovery

**Following restore scenarios are available:**

* **Manual restore when Automated restore is configured** on the cluster and operator needs to manually restore datastores. Scenario applies to staging environment. Restore
* **Manual restore / Disaster recovery. Scenario applies to any environment.**

### Manual restore when Automated restore is configured

{% hint style="info" %}
Its recommended to configure connection to cluster as described at [Add new cluster to your default kubeconfig](/technical/guides/installation/advanced-topics/kubernetes-cluster-access.md#option-3-add-new-cluster-to-your-default-kubeconfig) before running this task.
{% endhint %}

1. From your laptop SSH (login) to backup server and make sure latest backup exists, if for some reasons backup is not there, please follow **Manual restore** scenario.
2. Connect to your cluster with `kubectl`
3. Change namespace to opencrvs-deps-\<environment>:

   ```
   kubectl config set-context --current --namespace=opencrvs-deps-<environment>
   ```
4. Run following command to trigger restore jobs for all components:

   ```
   for cj in $(kubectl get cronjob -l job-type=restore -o jsonpath='{.items[*].metadata.name}'); do \
     kubectl delete job $cj-job --ignore-not-found; \
     kubectl create job --from=cronjob/$cj $cj-job; \
   done
   ```

   Example output:<br>

   ```
   job.batch/influxdb-restore-job created
   job.batch/minio-restore-job created
   job.batch/mongodb-restore-job created
   job.batch/postgres-restore-job created
   ```
5. Verify all jobs completed without issues:

   ```
   kubectl get job -ljob-type=restore
   ```

   Example output: Check job names like `*-restore-job` without ending number, jobs with number were triggered per schedule:

   ```
   NAME                        STATUS     COMPLETIONS   DURATION   AGE
   influxdb-restore-29384640   Complete   1/1           10s        7h16m
   influxdb-restore-job        Complete   1/1           9s         2m3s
   minio-restore-29384640      Complete   1/1           11s        7h16m
   minio-restore-job           Complete   1/1           8s         2m2s
   mongodb-restore-29384640    Complete   1/1           16s        7h16m
   mongodb-restore-job         Complete   1/1           15s        2m1s
   postgres-restore-29384640   Complete   1/1           11s        7h16m
   postgres-restore-job        Complete   1/1           10s        2m
   ```

### Manual restore / Disaster recovery

{% hint style="info" %}
Its recommended to configure connection to cluster as described at [Add new cluster to your default kubeconfig](/technical/guides/installation/advanced-topics/kubernetes-cluster-access.md#option-3-add-new-cluster-to-your-default-kubeconfig) before running this task.
{% endhint %}

* From your laptop SSH (login) to backup server
* Find backup that needs to be restored in remote directory `/home/backup/<environment>/`
* Note backup folder name, it should have following format: `YYYY-MM-DD`, e/g 2025-10-23 (Year-Month-Day).
* From your laptop connect to your cluster with `kubectl`
* Change namespace to opencrvs-deps-\<environment>:

  ```
  kubectl config set-context --current --namespace=opencrvs-deps-<environment>
  ```
* Make sure following kubernetes secrets exist:
  * `backup-server-ssh-credentials`
  * `backup-encryption-secret`
* Generate values files from helm release:

  ```
  helm get values opencrvs-deps > /tmp/opencrvs-deps.$(date +%F).yaml
  ```
* Run following command to trigger restore jobs for all components:

  ```bash
  jobs=(influxdb minio mongo postgres)
  for job in ${jobs[@]}; do
    echo "Starting $job service..."
    kubectl delete job ${job}-restore --ignore-not-found;
    helm template \
    --set restore.enabled=true \
    --set restore.cronjob=false \
    --set backup_encryption_secret=backup-encryption-secret \
    --set env.RESTORE_DATE=<YYYY-MM-DD: PUT YOUR DATE> \
    -s templates/${job}-restore-cronjob.yaml \
    -f /tmp/opencrvs-deps.$(date +%F).yaml \
    oci://ghcr.io/opencrvs/opencrvs-dependencies-chart | k apply -f -
  done
  ```

  Example output:

  ```
  job.batch/influxdb-restore-job created
  job.batch/minio-restore-job created
  job.batch/mongodb-restore-job created
  job.batch/postgres-restore-job created
  ```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/technical/guides/installation/opencrvs-maintenance-tasks/backup-and-restore/manual-restore-disaster-recovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
