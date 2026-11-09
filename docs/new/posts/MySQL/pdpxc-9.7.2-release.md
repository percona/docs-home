---
date: 2026-11-02
description: >
  Percona Distribution for MySQL 9.7.2 using Percona XtraDB Cluster has been released on November 02, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 9.7.2 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 9.7.2 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/9.7/index.html){:target="_blank"} has been released on November 02, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/9.7/installing.html){:target="_blank"}.

## Known issues
    
* In 9.7.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/9.7/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [9.7.1-rc1](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.1-rc1.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [3.4.7](https://git.haproxy.org/?p=haproxy-3.4.git;a=commit;h=8872a2604595140544774c2a6309a41186fc0f44){:target="_blank"} | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [3.0.9](https://docs.percona.com/proxysql/3.0.9.html){:target="_blank"}| A high performance, high-availability, protocol-aware proxy for MySQL.|
| Percona Toolkit         | [3.7.2](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-2-released-2026-10-22){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| replication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/9.7/replication-manager-for-pxc.html){:target="_blank"}  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 9.7.2-2 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/9.7/release-notes-pxc-9.7.2-2.html){:target="_blank"}.
