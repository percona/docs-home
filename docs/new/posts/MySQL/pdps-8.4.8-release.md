---
date: 2026-03-12
description: >
  Percona Distribution for MySQL 8.4.8 using Percona Server for MySQL has been released on Thursday, March 12, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.4.8 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.8 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Thursday, March 12, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Known issues and limitations
    
* In 8.4.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-20](https://github.com/percona/orchestrator/releases/tag/v3.2.6-20){:target="_blank"}     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona Toolkit     | [3.7.1](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-released-2025-12-17){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| Percona XtraBackup  | [8.4.0-5](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-5.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [8.4.8](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/news-8-4-8.html){:target="_blank"}    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [8.4.8](https://dev.mysql.com/doc/relnotes/mysql-router/8.4/en/news-8-4-8.html){:target="_blank"}    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 8.4.8 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-ps-8.4.8.html){:target="_blank"}.

