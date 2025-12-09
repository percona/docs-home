---
date: 2025-12-10
description: >
  Percona Distribution for MySQL 8.0.44 using Percona XtraDB Cluster has been released on Wednesday, December 10, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.44 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.44 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Wednesday, December 10, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

## Packaging and build notes

* Percona XtraDB Cluster 8.0 does not support Debian 13 or Red Hat Enterprise Linux 10.

* Percona XtraDB Cluster 8.0 has ended support for Ubuntu 20.04.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona XtraDB Cluster-based variation of the Percona Distribution for MySQL:

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [8.0.35-34](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-34.0.html)| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [2.8.15](https://git.haproxy.org/?p=haproxy-2.8.git;a=commit;h=a9aef56cb205d6d5e910530a87219900ccbd1b91) | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html)| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| Percona Toolkit         | [3.7.0-2](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-0-2-released-2025-05-14)     | The set of scripts to simplify and optimize database operation. |
| relication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/8.0/replication-manager/replication-manager-for-pxc.html)  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 8.0.44 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.44.html){:target="_blank"}.

