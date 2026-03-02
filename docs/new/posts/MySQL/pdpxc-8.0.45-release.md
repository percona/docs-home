---
date: 2026-03-02
description: >
  Percona Distribution for MySQL 8.0.45 using Percona XtraDB Cluster has been released on Monday, March 02, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.45 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.45 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Monday, March 02, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

## MySQL 8.0.45

Improvements and bug fixes provided by Oracle for MySQL 8.0.45 and included in Percona Server for MySQL are the following:

* InnoDB redo logging error messages now include the current LSN and redo log capacity information. New warning and error codes were added, and the MONITOR output has been enhanced to include redo log capacity details. (Bug #37645185)

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona XtraDB Cluster-based variation of the Percona Distribution for MySQL:

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [8.0.35-35](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-35.0.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [2.8.18](https://git.haproxy.org/?p=haproxy-2.8.git;a=commit;h=b6e928141b16d2a5adbfa331e0639fa02305fc8a){:target="_blank"} | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| Percona Toolkit         | [3.7.1](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-released-2025-12-17){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| relication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/8.0/replication-manager/replication-manager-for-pxc.html){:target="_blank"}  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 8.0.45 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.45.html){:target="_blank"}.

