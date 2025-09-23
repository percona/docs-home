---
date: 2025-09-23
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 0.12.0 has been released on September 23, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona Server for MySQL 0.12.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/ps/index.html){:target="_blank"} 0.12.0 has been released on September 23, 2025.

Version 0.12.0 of the Percona Operator for MySQL is still **a tech preview release**, and it is **not recommended for production environments**. You can try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/ps/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Data-at-rest encryption for MySQL 8.4](Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/ps/encryption-setup.html){:target="_blank"} makes Percona Server for MySQL 8.4 be fully supported by the Operator. This improvement empowers you to take full advantage of Percona Server for MySQL 8.4’s features while benefiting from seamless, automated lifecycle management provided by the Operator. Percona Server for MySQL 8.4 is now the default version for deploying a database cluster.

* Ensure cluster availability with PodDisruptionBudgets. You can configure a PodDisruptionBudget for MySQL, HAProxy, MySQL Router, and Orchestrator Pods, thus ensuring your cluster remains available during voluntary disruptions, such as deleting a deployment or draining a node for maintenance.

* Gain more control over backup and restore operations with the ability to configure `xtrabackup`, `xbstream`, and `xbcloud` binaries. You can apply the configuration globally or for a specific backup / restore job. Individual settings override the global ones. Learn more about fine- tuning backups and restores and how the settings are applied in our [documentation](https://docs.percona.com/percona-operator-for-mysql/ps/backups-fine-tune.html){:target="_blank"}  

* Monitor PMM Client health and status with probes - a Kubernetes diagnostics mechanism. Use the `spec.pmm.readinessProbes.*` and `spec.pmm.livenessProbes.*` Custom Resource options to fine-tune Readiness and Liveness probes for PMM Client.

* Tailor your backup strategy with the ability to define a backup source Pod. For asynchronous replication clusters, the Operator must know the cluster topology to run a backup. For this, either enable the Orchestrator in your deployment. Or specify the `sourcePod` value, if your cluster has more than one MySQL Pods. 

* Deprecation, rename and removal

    * The `.spec.initImage` field has been replaced by the `.spec.initContainer` subsection, which follows Kubernetes best practices for defining containers that run before the main containers in a Pod. The `initContainer` feature is helpful for setup tasks such as:

       - Initializing data
       - Waiting for services to become available
       - Setting permissions
       - Pulling secrets or configuration files

* The default cluster name has been changed to `ps-cluster1` to prevent possible conflicts if you have custom resources of both Percona Operator for MySQL based on Percona Server for MySQL and Percona XtraDB Cluster in the same namespace.

* The API version in CRDs is changed from `v1alpha` to `v1`. To upgrade to version 0.12.0, you must manually delete the CRDs, apply new ones and recreate the cluster. To keep the data, do the following:

    * check that the `percona.com/delete-mysql-pvc` finalizer is not enabled in `deploy/cr.yaml`
    * don't delete PVCs manually
    * Recreate the cluster with the same name. The Operator then automatically reuses the same PVCs.



Learn more in Percona Operator for MySQL based on Percona Server for MySQL 0.12.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN0.12.0.html){:target="_blank"}.
