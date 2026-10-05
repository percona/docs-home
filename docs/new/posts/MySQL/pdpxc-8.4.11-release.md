---
date: 2026-10-05
description: >
  Percona Distribution for MySQL 8.4.11 using Percona XtraDB Cluster has been released on October 05, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.4.11 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.11 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on October 05, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Percona XtraDB Cluster 8.4.11-11

!!! note "Upgrade to 9.7"

    To upgrade from Percona XtraDB Cluster 8.4 to 9.7, use 9.7.2 or newer as the target version. Upgrading from 8.4.11 to 9.7.1 is not supported.

Percona XtraDB Cluster 8.4.11-11 introduces the following improvements:

* When `pxc_strict_mode` is set to `ENFORCING` or `MASTER`, Percona XtraDB Cluster now also enables `sql_require_primary_key` globally, so tables without a primary key can no longer be created or altered. Previously, you could create such a table but could not run DML statements on it. While `pxc_strict_mode` is `ENFORCING` or `MASTER`, setting `sql_require_primary_key` to `OFF` returns an error. The server applies the setting at startup and whenever `pxc_strict_mode` changes to one of these modes. Existing connections keep their current session value, and new connections use the updated global value.

* Adds the `repl.force_sst_after_inconsistency` Galera provider option. When the option is enabled and a node is voted out of the cluster because of a data inconsistency, the node removes the `grastate.dat` file on shutdown. On the next start, the node performs a full State Snapshot Transfer (SST) instead of an Incremental State Transfer (IST), which ensures a consistent dataset. The option is disabled by default and can be changed at runtime with `wsrep_provider_options`.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona XtraDB Cluster-based variation of the Percona Distribution for MySQL:

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [8.4.0-7](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-7.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [2.8.29](https://git.haproxy.org/?p=haproxy-2.8.git;a=commit;h=ee8cc4dcba99a3ddead42f0528c8a50333acfa9d){:target="_blank"} | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| Percona Toolkit         | [3.7.1-4](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-4-released-2026-07-02){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| replication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/8.4/replication-manager-for-pxc.html){:target="_blank"}  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 8.4.11 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-pxc-8.4.11.html){:target="_blank"}.
