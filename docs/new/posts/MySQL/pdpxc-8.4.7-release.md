---
date: 2026-01-13
description: >
  Percona Distribution for MySQL 8.4.7 using Percona XtraDB Cluster has been released on Tuesday, January 13, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.4.7 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.7 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Tuesday, January 13, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Build & packaging notes

* Percona XtraDB Cluster 8.4 adds support for Debian 13.

* Percona XtraDB Cluster 8.4 has ended support for Ubuntu 20.04.

* Amazon Linux 2023 is not supported in Percona Distribution for MySQL. We do support Amazon Linux 2023 in Percona Server for MySQL and Percona XtraBackup.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona XtraDB Cluster-based variation of the Percona Distribution for MySQL:

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [8.4.0-5](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-5.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [2.8.18](https://git.haproxy.org/?p=haproxy-2.8.git;a=commit;h=ae90be6491cfe0cb0a16bfd5b03babfaf312b0bf){:target="_blank"} | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| Percona Toolkit         | [3.7.1](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-released-2025-12-17){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| replication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/8.4/replication-manager-for-pxc.html){:target="_blank"}  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 8.4.7 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-pxc-8.4.7.html){:target="_blank"}.
