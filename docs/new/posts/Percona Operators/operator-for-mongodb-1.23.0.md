---
date: 2026-07-22
description: >
  Percona Operator for MongoDB 1.23.0 has been released on July 22, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.23.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.23.0 has been released on July 22, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [ClusterSync migration and replication](https://docs.percona.com/percona-operator-for-mongodb/clustersync.html){:target="_blank"}. Moving a live MongoDB deployment onto the Operator no longer means a long dump-and-restore window or fragile hand-built replication. With Percona ClusterSync for MongoDB (PCSM) managed by the Operator, you declare source and target in a dedicated `PerconaServerMongoDBClusterSync` Custom Resource. The Operator runs PCSM to clone existing data and then keep the target current while the app is still connected to the source.

   When the replication lag is decent to cut over, finalize the replication and re-point the app to the target. As a result, migration is measured in seconds, without you securing a maintenance window sized to your data set. The same flow works for leaving Atlas or another hosted service, keeping a continuous non-production or disaster-recovery replica, or syncing hybrid-cloud copies.

* Run semantic queries and RAG in the Operator (tech preview). You can now store and query vector data alongside regular documents in Percona Server for MongoDB thus having a single system for tickets, catalogs, or internal docs that power AI answers. This feature is in tech preview and requires Percona Server for MongoDB 8.3.

   Enable search in the Custom Resource and have the Operator deploy and manage the search `mongot` process, wire authentication and TLS, and keep the index in sync for replica sets and sharded clusters. Your apps keep using the same MongoDB connection string they already use, so you add semantic search without a second client or a second set of credentials. See our [documentation](https://docs.percona.com/percona-operator-for-mongodb/vector-search.html){:target="_blank"} to learn more.


* Take multi-terabyte backups off the network path with [PVC snapshot backups](https://docs.percona.com/percona-operator-for-mongodb/backups-snapshots.html){:target="_blank"} (tech preview). PVC snapshots copy volumes at the storage layer in seconds or minutes regardless of the data size. Restores are correspondingly faster as well. Snapshots work with encrypted and TLS-enabled clusters and use fewer cluster resources because there is no long data transfer job. Pair frequent snapshots for local recovery with streamed object-storage backups for cross-site replication and disaster recovery setups. This feature is in tech preview stage. Try it out in staging or testing environment. Snapshot portability and retention semantics depend on your CSI driver, so test restores before you rely on them.

* Simplify connection management with the Operator-generated [connection string Secrets](https://docs.percona.com/percona-operator-for-mongodb/connection-secrets.html){:target="_blank"}. The Operator publishes ready-to-use MongoDB URIs for `databaseAdmin` and custom users in dedicated connection secrets, that reflect your topology and are automatically updated once the configuration changes. This enables you to mount these Secrets directly in Deployments, Jobs, or CI pipelines instead of maintaining separate connection logic.

* [Workload Identity support for GCS backups](https://docs.percona.com/percona-operator-for-mongodb/backups-storage-gcp.html#automate-access-to-google-cloud-storage-using-workload-identity){:target="_blank"}. Instead of managing  service-account JSON keys in a Secret, bind Workload Identity and let PBM use short-lived cloud credentials instead. This hardens your security policy towards backups and simplifies credential governance across environments.

* Native OCI and Alibaba OSS backup destinations. Keep backups in the cloud you already run on. Store them natively in [Oracle Cloud Infrastructure Object Storage](https://docs.percona.com/percona-operator-for-mongodb/backups-storage-oci.html){:target="_blank"} or [Alibaba Cloud OSS](https://docs.percona.com/percona-operator-for-mongodb/backups-storage-oss.html){:target="_blank"} without the need for an S3-compatible endpoint as a workaround. This way you reduce latency and benefit from fewer cross-cloud hops.

* [Restore a collection under a different name](https://docs.percona.com/percona-operator-for-mongodb/backups-restore-new-name.html){:target="_blank"} to recover without overwriting live data. Restore the collection side by side, compare or validate the data, then merge what you need back into production. The Operator automates the full flow through the Restore Custom Resource, so you don't need to exec into pods or run PBM manually. You get safer partial recovery with less operational risk and a clear, trackable restore status.

* External nodes as arbiters enable you to maintain quorum across regions without deploying a third full data‑bearing replica. By adding a node to the `externalNodes` list and marking it as `arbiterOnly: true`, you designate it as a lightweight external arbiter that provides a tie‑breaker vote from another site.

* Fit MongoDB into your platform PKI by using your own cert-manager ClusterIssuer and fine-tuning TLS policy for the Operator. Point the Operator at that ClusterIssuer instead of letting it create its own CA chain. Use the  `certManagementPolicy: userProvidedOnly` to take a full control over a certificate lifecycle to ensure that a briefly missing Secret doesn't regenerate certificates and break apps.

* Ease API pressure on large fleets by [fine-tuning reconciliation interval](https://docs.percona.com/percona-operator-for-mongodb/reconciliation-concurrency.html){:target="_blank"}. Set the required `RECONCILE_INTERVAL` value instead of the fixed 5s default to reduce chatter when clusters are stable.

* RKE2 and full ARM64 support - Run the Operator where your platform already is. Official RKE2 testing adds a new supported Kubernetes distribution, while full ARM64 images broaden architecture coverage across modern cloud and edge environments.


Learn more in Percona Operator for MongoDB 1.23.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.23.0.html){:target="_blank"}.
