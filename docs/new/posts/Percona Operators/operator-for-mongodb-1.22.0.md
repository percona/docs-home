---
date: 2026-02-25
description: >
  Percona Operator for MongoDB 1.22.0 has been released on February 25, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.22.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.22.0 has been released on February 25, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* Automatic storage resizing. The Operator can automatically grow PVCs for replica sets and config servers when usage crosses a threshold, up to a maximum size you define. You get fewer full-disk outages, less manual capacity planning, and growth only when needed. Enable it in your Custom Resource:  

   ```yaml
   spec:
     storageScaling:
       enableVolumeScaling: true
       autoscaling:
         enabled: true
         triggerThresholdPercent: 80
         growthStep: 2Gi
         maxSize: "10Gi"
   ```

* [Manage system user passwords with HashiCorp Vault](https://docs.percona.com/percona-operator-for-mongodb/system-users-vault.html){:target="_blank"}. The Operator pulls passwords from Vault using either Kubernetes authentication or a Vault token, creates and updates the corresponding Kubernetes Secret, and can periodically refresh them when it changes in Vault. Suited for centralized credentials, audit-friendly rotation, and separation between DBAs and security teams.

* Ensure smooth integration with service meshes. The Operator now sets the Kubernetes `appProtocol` field to `mongo` on all MongoDB services. Service meshes such as Istio can correctly detect MongoDB traffic, so you get reliable cluster formation and mTLS without manual tweaks. You can use traffic management, observability, and security features of the mesh as intended.

* [Restore to a cluster with different replica set names](https://docs.percona.com/percona-operator-for-mongodb/backups-restore-replset-remapping.html){:target="_blank"}. You can now make physical or logical restore into a cluster whose replica set names differ from the source. Define the source→target replica set mappings as key-value pairs in your `PerconaServerMongoDBRestore` object in the `replsetRemapping` section. This makes recovery and migration between environments much more flexible.

* Automatic CRD updates with Helm. A separate Helm chart `psmdb-operator-crds` is available for CRDs. You can manage and upgrade CRDs with Helm instead of applying them manually, which fits GitOps (e.g. ArgoCD, FluxCD) and gives you versioning and rollback for CRDs. This change is fully compatible with the previous behavior, where CRDs are installed from the `crds/` folder of the main Helm chart. We keep this behavior as default for the next three releases to give you more time to adjust your workflows and [update](https://docs.percona.com/percona-operator-for-mongodb/update-crd-helm.html){:target="_blank"}.

* [Configurable log rotation for persistent logs](https://docs.percona.com/percona-operator-for-mongodb/logrotate.html){:target="_blank"}. You can tune log rotation for persistent logs: override defaults in the Custom Resource, add options via ConfigMap or Secret (e.g. for audit logs), and set rotation schedules to match your retention and operational windows.

* Configurable PBM backup start timeout. You can now configure how long the Operator waits for PBM to report that a backup has begun. Instead of relying on a fixed timeout of 120 seconds, you can tune this value to match your cluster's performance characteristics. Set the `startingDeadlineSeconds` value in the Custom Resource so slow or resource-constrained clusters have enough time for PBM to initialize, reducing false backup failures.

* Improved reliability of automation tools with the Operator. The PerconaServerMongoDB status now includes a `PBMReady` condition so you can see when PBM has finished configuring all storages. Automation tools can rely on this instead of guessing to trigger backups and other operations. Check the PBM state with `kubectl describe psmdb <cluster-name>` or `kubectl get psmdb <cluster-name> -o yaml` commands.

* A dedicated minio storage type is available for backups to MinIO and S3-compatible storage services. It uses the native MinIO SDK and can avoid connectivity or compatibility issues when the storage does not support AWS SigV4. If you issues problems with S3-compatible backups, consider switching to the minio type. Check the [storage configuration](https://docs.percona.com/percona-operator-for-mongodb/backups-storage-minio.html){:target="_blank"} for configuration examples.

* [Use Private Certificate Authorities (CA) for TLS communication with S3-compatible storage services](https://docs.percona.com/percona-operator-for-mongodb/backups-storage-minio.html#configure-tls-verification-with-custom-certificates-for-s3-storage){:target="_blank"} . You can supply a private CA bundle (e.g. from your PKI) so the Operator verifies TLS to your S3-compatible backup storage instead of skipping verification. The minio storage type is required for this feature. With this change you align with your internal standards and gain confidence in secure S3 interaction during your backup and restore flows. Create a Secret with your CA and reference it in the backup storage config via `caBundle`. 

* Use [custom environment variables](https://docs.percona.com/percona-operator-for-mongodb/env-vars-cluster.html){:target="_blank"} to parameterize and control database Pod behavior without hardcoding values in manifests. You can define them for for mongod, mongos, and logcollector to match the container behavior matches that of your platform or to pass flags and secrets without changing images. Configure custom environment variables in the Custom Resource, or via a ConfigMap or Secret, for more flexible and environment-aware deployments.

* A new `hookScript` option lets you run a custom shell script before mongod, mongos, or a pbm-agent starts, either inline or from a ConfigMap. The script can block startup on non-zero exit. Use it for things like fetching external secrets, security checks, or registering nodes elsewhere, without custom images. Supported on replica set members (including hidden, arbiter, non-voting), config servers, mongos, and pbm-agent.

* Deprecations:

    * Percona Server for MongoDB 6.0 is deprecated (6.0 is EOL) and will be removed in Operator 1.23.0.
    * PMM2 is deprecated and will be removed in two releases; plan to [migrate to PMM3]((https://docs.percona.com/percona-monitoring-and-management/3/pmm-upgrade/migrating_from_pmm_2.html){:target="_blank"}.
    * `spec.enableVolumeExpansion` and `spec.enableExternalVolumeAutoscaling` are deprecated and will be removed in 1.25.0. Use the options under `spec.storageScaling` instead (`enableVolumeScaling` and  `enableExternalAutoscaling` respectively).


Learn more in Percona Operator for MongoDB 1.22.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.22.0.html){:target="_blank"}.
