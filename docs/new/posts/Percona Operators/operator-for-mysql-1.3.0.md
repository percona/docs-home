---
date: 2026-10-29
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 1.3.0 has been released on October 29, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL 1.3.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/1.3.0/index.html){:target="_blank"} 1.3.0 has been released on October 29, 2026.

This release adds automatic MySQL configuration tuning, a replication type switch on a running cluster (tech preview), encrypted binlogs for point-in-time recovery, ability to manage application users via the Custom Resource, security builds for the Operator you already run, and support for Percona Server for MySQL 9.7. It also provides a number of improvements for async clusters and ClusterSet improvements.

What's new:

* Run production-ready MySQL clusters with [MySQL settings calculated automatically](https://docs.percona.com/percona-operator-for-mysql/1.3.0/autoconfig.html){:target="_blank"} based on the Pod's CPU and memory, database version and workload. The calculation covers the InnoDB buffer pool and redo log, session buffers, connection limits, and replication settings for the cluster type you run. When you change the Pod's resources or the workload, the Operator calculates those settings again. If you define MySQL settings in `spec.mysql.configuration`, a ConfigMap, or a Secret, the Operator applies those settings and skips automatic tuning. 

* [Change dynamic MySQL settings without a restart](https://docs.percona.com/percona-operator-for-mysql/1.3.0/options.html#dynamic-configuration){:target="_blank"}. Update `mysql.configuration` and the Operator applies dynamic variables with `SET GLOBAL` on every ready Pod. Static variables, runtime-blocked changes, and removed options still trigger a rolling restart. You can tune a busy cluster and respond to an incident without a configuration restart.

* [Fail over an asynchronous cluster without losing committed data](https://docs.percona.com/percona-operator-for-mysql/1.3.0/failover-async.html){:target="_blank"}. The replica chosen as the new primary fetches and applies the binary logs it is missing from the failed primary before promotion. You control the cluster behavior if the failover fails to complete: act yourself or force failover with possible data loss. This feature requires backups to be enabled for the cluster.

* [Switch replication type on a running cluster (tech preview)](https://docs.percona.com/percona-operator-for-mysql/1.3.0/change-replication-type.html){:target="_blank"}. 
Move between Group Replication and asynchronous replication without pausing and bringing the cluster back yourself. The Operator converts the topology in place: it tears down the old replication setup, recreates the MySQL and proxy workloads, and bootstraps the new type on the same PersistentVolumeClaims. Users, Secrets, and the HAProxy Service stay in place, so applications keep the same connection endpoint if they already use HAProxy. The feature is in tech preview status, so test it on staging environment first.

* [Encrypted binlogs for point-in-time recovery](https://docs.percona.com/percona-operator-for-mysql/1.3.0/backups-pitr.html){:target="_blank"}.
You can now encrypt binlogs before Percona Binlog Server uploads them. The Operator validates the Secret with your encryption keys, encrypts each new file on the way to the bucket, and decrypts it during restore. Files already in the bucket stay as they are and are applied as-is, so you can turn encryption on without emptying storage. Keep previous keys in the Secret and the Secret in the cluster to read binlogs after you disabled their encryption.

* [Manage application users via the Custom Resource](https://docs.percona.com/percona-operator-for-mysql/1.3.0/users.html#create-users-in-the-custom-resource){:target="_blank"} when you create or update the cluster. Set the username, databases to connect and grants. The Operator takes over and creates users for you. To rotate the password, change the Secret and the Operator applies it on the next reconcile.

* [Size an asynchronous cluster with an even number of instances](https://docs.percona.com/percona-operator-for-mysql/1.3.0/scaling.html#horizontal-scaling){:target="_blank"} Use the replica count that fits your workload. You can set `mysql.size` to 2, 4, 6, or any larger even count on an asynchronous cluster without `unsafeFlags.mysqlSize`. Orchestrator still needs an odd size of 3 or greater.

* Improved bootstrapping behavior for async replication clusters. A joining replica is no longer stopped by a fixed clone timeout. The Operator stops the clone only when it makes no progress. Control the timeout with the `BOOTSTRAP_CLONE_TIMEOUT` environment variable.

* Rejoin a ClusterSet replica automatically, or by annotation. The Operator automatically rejoins a replica that was paused, stopped, or crashed. When the replication channel is down, you trigger rejoin with an annotation. You decide when to rejoin, and the Operator runs the Job. For the steps, see [Rejoin a replica cluster](https://docs.percona.com/percona-operator-for-mysql/1.3.0/replication-setup.html#rejoin-a-replica-cluster){:target="_blank"}

* [Read ClusterSet replication lag from status](https://docs.percona.com/percona-operator-for-mysql/1.3.0/cr-statuses.html#per-member-cluster-status){:target="_blank"}. Each replica cluster reports replicationLagSeconds, so you can check lag with `kubectl`.

* [Restore an encrypted cluster to a point in time](https://docs.percona.com/percona-operator-for-mysql/1.3.0/backups-pitr.html){:target="_blank"}. The Operator uses your existing Vault Secret, so tablespaces stay encrypted while binlogs roll the database forward.

* Limit how long a backup waits to start or resume. Set a start deadline and a suspend deadline so a backup that waits too long ends in an error instead of staying queued.

* [Use your own ClusterIssuer with cert-manager for TLS](https://docs.percona.com/percona-operator-for-mysql/1.3.0/tls-cert-manager.html#use-an-existing-clusterissuer){:target="_blank"}. Point the Operator at the cluster-wide issuer you already use, and cert-manager signs the MySQL certificates. As a result you keep one source of truth for certificates instead of an Operator-managed CA in every database namespace.

* [Verify TLS to S3-compatible storage with your own certificate authority](https://docs.percona.com/percona-operator-for-mysql/1.3.0/backups-storage.html#configure-tls-verification-with-custom-certificates-for-s3-storage){:target="_blank"}. That matters when you use certificates from your corporate PKI, and security policy does not let you skip certificate checks. Reference your CA in the storage configuration and keep TLS verification enabled. 

* Rotate a leaf certificate without restarting MySQL. When the certificate authority stays the same, the Operator reloads the new leaf into running `mysqld` processes. You achieve MySQL availability during routine certificate renewal and fewer database Pod restarts on a cert-manager schedule.

* [Persistent logging for MySQL error log](https://docs.percona.com/percona-operator-for-mysql/1.3.0/persistent-logging.html){:target="_blank"}. The Operator now uses Fluent Bit to collect MySQL error logs and keep them on the MySQL data volume so that it survives Pod restarts. The logrotate utility rotates those files so that they don't fill the volume. This simplifies troubleshooting during accidents and gives you flexibility to apply your rotation policies.

* Receive a High or Critical vulnerability fixes without a version upgrade via security builds. A weekly scan rebuilds the Operator image you already run when it finds a High or Critical CVE. Use a numbered tag, such as `1.3.0-2`, to stay on that exact fix, or `1.3.0-latest` to pick up every later fix for this version. The database cluster keeps running. When the next Operator version ships, these images stay available, and new scans start for that version. 

* Added support for the latest major version of MySQL 9.7.

* Official DigitalOcean Kubernetes Service (DOKS) testing adds a new supported Kubernetes distribution.


Learn more in Percona Operator for MySQL based on Percona Server for MySQL [release notes](https://docs.percona.com/percona-operator-for-mysql/1.3.0/ReleaseNotes/Kubernetes-Operator-for-PS-RN1.3.0.html){:target="_blank"}.
