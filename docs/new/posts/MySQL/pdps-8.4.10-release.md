---
date: 2026-06-30
description: >
  Percona Distribution for MySQL 8.4.10 using Percona Server for MySQL has been released on Tuesday, June 30, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.4.10 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.10 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Tuesday, June 30, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Builds and packaging

* Percona Server for MySQL releases include a mixture of PGO and non-PGO builds. Where Profile-Guided Optimization (PGO) is enabled, the compiler uses runtime profiling data from representative workloads to guide optimization, which can improve throughput and reduce latency compared with non-PGO builds.

* See [Profile-Guided Optimization (PGO) and non-PGO builds](https://docs.percona.com/percona-server/8.4/pgo.html){:target="_blank"} for benefits, considerations, and which build you receive for your platform.

## Known issues and limitations
    
* In 8.4.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-22](https://github.com/percona/orchestrator/releases/tag/v3.2.6-22)     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html)     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona Toolkit     | [3.7.1-3](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-3-released-2026-04-17)     | The set of scripts to simplify and optimize database operation. |
| Percona XtraBackup  | [8.4.0-6](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-6.html)| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [8.4.10](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/news-8-4-10.html)    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [8.4.10](https://dev.mysql.com/doc/relnotes/mysql-router/8.4/en/news-8-4-10.html)    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 8.4.10 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-ps-8.4.10.html){:target="_blank"}.

