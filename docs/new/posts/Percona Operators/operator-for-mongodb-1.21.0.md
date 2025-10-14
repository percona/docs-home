---
date: 2025-10-15
description: >
  Percona Operator for MongoDB 1.21.0 has been released on October 14, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.21.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.21.0 has been released on October 14, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* Percona Server for MongoDB 8.0 is now the default version for deploying new clusters. This enables you to enjoy all features and improvements of the latest major version of out of the box.

* You can now monitor the health and performance of your Percona Server for MongoDB deployment and at the same time enjoy enhanced performance, new features, and improved security that the support for PMM 3 provides. Note that PMM2 support remains in the Operator. The decision what PMM version to use is made based on the configured authentication method. Read more about PMM 3 configuration in the [documentation](https://docs.percona.com/percona-operator-for-mongodb/monitoring.html){:target="_blank"}.

* In addition to arbiters and non-voting nodes, you can now deploy hidden nodes in your Percona Server for MongoDB cluster. These nodes hold a full copy of the data but remain invisible to client applications. They are good for tasks like backups and reporting, since they access the data without affecting normal traffic. Check the [documentation](https://docs.percona.com/percona-operator-for-mongodb/arbiter.html){:target="_blank"} for more information about hidden nodes configuration and voting members management by the Operator.

* The Operator now supports service account key authentication in Google Cloud Storage (GCS), inheriting this functionality from Percona Backup for MongoDB. The configuration of Google Cloud Storage with HMAC keys remains unchanged but is considered deprecated. We encourage you to switch to using service account keys after the upgrade. Read more about GCS support and configuration in the [documentation](https://docs.percona.com/percona-operator-for-mongodb/backups-storage.html){:target="_blank"}.

* Improved operational resilience and observability with persistent [cluster-level logging for MongoDB Pods](https://docs.percona.com/percona-operator-for-mongodb/debug-logs.md#cluster-level-logging){:target="_blank"}. The Operator now supports cluster-level logging ensuring that logs from your `mongod` instances are stored persistently, even across Pod restarts. Cluster-level logging is currently supported for `mongod` Pods. All other logs are ephemeral, meaning they will not persist after a Pod restart. Logs are stored for 7 days and are rotated afterwards.

* Improved backup retention configuration gives you more control over how backups are managed in storage and retained in Kubernetes. Use this new configuration in your Custom Resource:

    ```yaml
    schedule:
      - name: "sat-night-backup"
        schedule: "0 0 * * 6"
        retention:
          count: 3
          type: count
          deleteFromStorage: true
        storageName: s3-us-west
    ``` 

    Note that the legacy `keep` option is now deprecated and mapped to the new `retention` block for compatibility. If you have both `backup.schedule.keep`  and `backup.schedule.retention`  defined, the `backup.schedule.retention` takes precedence.

* Identify the current Operator version associated with Custom Resources via labels. This helps you decide if you need to upgrade it or not.

* Delegate PVC resizing to an external autoscaler by disabling the built-in resizing functionality. Set `spec.enableExternalVolumeAutoscaling` option to `true` in your Custom Resource to prevent the Operator from attempting to resize PVCs. This is useful if you use an external tool to manage volume sizes.

* Known limitation for deleting backups created with PBM versions earlier than 2.11.0. You need to delete these backups manually to free up the space. The steps are:
  
   1. Remove the finalizer from a `psmdb-backup` object.
   2. [Delete the backup](https://docs.percona.com/percona-operator-for-mongodb/backups-delete.html){:target="_blank"}.

Learn more in Percona Operator for MongoDB 1.21.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.21.0.html){:target="_blank"}.
