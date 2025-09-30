---
date: 2025-10-
description: >
  Percona Distribution for MySQL 8.4.6 using Percona XtraDB Cluster has been released on Thursday, October , 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.4.6 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.6 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Thursday, October , 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Build & packaging notes

* The official packages were built with the `WITH_LTO=ON` flag to enable the Link-Time Optimization (LTO) feature.

* This release suports Red Hat Enterprise Linux (RHEL) 10.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona XtraDB Cluster-based variation of the Percona Distribution for MySQL:

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [8.4.0-4](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-4.html)| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [2.8.15](https://git.haproxy.org/?p=haproxy-2.8.git;a=commit;h=a9aef56cb205d6d5e910530a87219900ccbd1b91) | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [3.0.1](https://docs.percona.com/proxysql/3.0.1.html)| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| Percona Toolkit         | [3.7.0-2](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-0-2-released-2025-05-14)     | The set of scripts to simplify and optimize database operation. |
| replication_manager.sh   | [1.0](replication-manager-for-pxc.md)  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 8.4.6 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-pxc-8.4.6.html){:target="_blank"}.
