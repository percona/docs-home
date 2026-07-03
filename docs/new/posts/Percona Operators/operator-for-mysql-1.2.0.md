---
date: 2026-07-03
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 1.2.0 has been released on July 2, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL 1.2.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/1.2.0/index.html){:target="_blank"} 1.2.0 has been released on July 3, 2026.

This release delivers key features such as cross-site replication, encrypted backups, and automated storage resizing, which harden the Operator for production use. Additionally, it improves security with Orchestrator API authentication and Vault encryption secret validation, and includes a bunch of improvements for day-to-day operations.

New features and improvements introduced by this release include:

* Scale your Percona Server for MySQL deployment geographically with the [cross-site replication for Group Replication clusters](https://docs.percona.com/percona-operator-for-mysql/1.2.0/replication.html){:target="_blank"}. You can now link clusters into a MySQL InnoDB ClusterSet and manage the entire topology declaratively from Kubernetes with the new `PerconaServerMySQLClusterSet` Custom Resource. This means disaster recovery, migrations, and regional read scaling are simpler and more reliable, with replicas that can run in the same Kubernetes environment, in different clusters, or even outside Kubernetes altogether. The Operator takes care of automating and managing the ClusterSet lifecycle, so you can focus on your applications while knowing your replicas stay in sync with the primary.

* Protect backup data at rest in the cloud storage of your choice using [backup encryption](https://docs.percona.com/percona-operator-for-mysql/1.2.0/backups-encrypted.html){:target="_blank"}. Define encryption settings either globally for all storages or override them per storage for additional flexibility. The Operator uses Percona XtraDB Cluster's native encryption, letting you tune encryption settings to better match your security needs. 

* [Automatic storage resizing](https://docs.percona.com/percona-operator-for-mysql/1.2.0/scaling.html){:target="_blank"}. The Operator monitors disk usage on Percona Server for MySQL Pods and expands the storage automatically when the usage crosses your thresholds. As a result, you spend less time on capacity planning, save costs by expanding only when needed and avoid outages from full disks.

* Delegate PVC resizing to an external autoscaler. You can now configure the Operator to use an external storage autoscaler instead of its own resizing logic. This ability may be useful for organizations needing centralized, advanced, or cross-application scaling policies.

* [Connection details exposed in the user Secret](https://docs.percona.com/percona-operator-for-mysql/1.2.0/connection-secret.html){:target="_blank"}. The Operator now maintains a dedicated root user Secret with host, port, URI, and proxy or external LoadBalancer connection fields, updated automatically after failover. You can mount this Secret in your application Pods, reference it in your CI/CD pipeline, or use it with External Secrets. However you consume credentials today, you now have everything in one place.

* Secure Orchestrator API access with authentication. Clients must now authenticate when calling the Orchestrator HTTP API for failover and topology operations to reduce the risk of accidental or unauthorized cluster changes. The Operator handles authentication automatically for its own API calls, reading credentials from the mounted secret, so day-to-day cluster management continues to work as before. 

* Reduce troubleshooting burden with Vault encryption secret validation. When data-at-rest encryption uses HashiCorp Vault, the Operator validates the Secret at startup and reports clear status errors if it is missing or invalid. Define the encryption configuration upfront, the Operator waits until the Secret is present and valid before continuing cluster setup.

* Disable NodePort allocation for LoadBalancer Services. Turn off automatic NodePort assignment on Operator-created LoadBalancer Services to reduce attack surface and avoid port exhaustion.

* Percona Server for MySQL 8.4 has NUMA disabled by default. MySQL 8.4 enables NUMA interleaving by default, but that often causes warnings or blocked requests in Kubernetes. The Operator now disables it by default for Percona Server for MySQL 8.4, giving you cleaner logs and more predictable behavior in typical cloud environments. 

* Independent resource configuration for HAProxy sidecar containers. Set CPU and memory requests and limits for the `mysql-monit` sidecar separately from HAProxy, so lightweight sidecars are no longer over-provisioned.

* Pass binlog storage settings in the restore object for point-in-time recovery. You can now specify binlog storage directly in the `PerconaServerMySQLRestore` object when performing point-in-time recovery to a new cluster. This simplifies the cross-cluster point-in-time recovery configuration as a single restore manifest carries everything needed for the operation.

* Improve operational efficiency with the [support for concurrent cluster reconciliation](https://docs.percona.com/percona-operator-for-mysql/1.2.0/reconciliation-concurrency.html){:target="_blank"}. Process multiple clusters in parallel by tuning the `MAX_CONCURRENT_RECONCILES` environment variable, improving scalability and responsiveness in multi-cluster deployments.

* [Configurable DNS suffix for Operator connections](https://docs.percona.com/percona-operator-for-mysql/1.2.0/dns-suffix.html){:target="_blank"}. Set a custom `clusterServiceDNSSuffix` for vclusters or non-standard DNS setups so service discovery and PMM connectivity work correctly.

* Fine-tune Orchestrator failover behavior. Use the `spec.orchestrator.configuration` in the Custom resource to adjust failover settings such as promotion lag tolerance and recovery blocking per cluster. The Operator merges your settings into the Orchestrator configuration. However, Operator-managed options remain intact and are ignoed if you modify them.

* Improved PMM monitoring for multi-region and multi-namespace deployments. Assign a custom cluster name with `pmm.customClusterName` so that PMM Server groups related clusters correctly on dashboards.

* Deprecation, rename, removal

   * Deprecated spec.enableVolumeExpansion. This option still works for backward compatibility but will be removed in version 1.5.0. Use spec.storageScaling.enableVolumeScaling instead.

* Known limitation

   * Binlog Server 0.3.1 is incompatible with the previous version. To upgrade, you need to start the fresh backup and binlog collection. Refer to the [documentation](https://docs.percona.com/percona-operator-for-mysql/1.2.0/upgrade-db.html){:target="_blank"} for steps.

Learn more in Percona Operator for MySQL based on Percona Server for MySQL 1.2.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/1.2.0/ReleaseNotes/Kubernetes-Operator-for-PS-RN1.2.0.html){:target="_blank"}.
