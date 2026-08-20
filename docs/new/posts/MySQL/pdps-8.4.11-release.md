---
date: 2026-08-20
description: >
  Percona Distribution for MySQL 8.4.11 using Percona Server for MySQL has been released on Thursday, August 20, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.4.11 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.11 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Thursday, August 20, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Percona Server for MySQL 8.4.11-11

Percona Server for MySQL 8.4.11-11 introduces the following new features and improvements:

* Adds OpenID Connect (OIDC) authentication and authorization. Users can authenticate with Identity tokens issued by external Identity Providers (IDPs) instead of MySQL passwords. The OIDC plugin supports multiple IDPs, maps IDP groups to MySQL roles, supports proxy users based on group membership, and refreshes JSON Web Key Set (JWKS) signing keys at runtime. Find more information in [OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/openid-connect-authentication.html){:target="_blank"} and in [Get started with OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/quickstart-openid-connect.html){:target="_blank"}.

* Improves InnoDB performance for workloads limited by Least Recently Used (LRU) flush speed. The improvements reduce LRU list mutex contention, restore dedicated LRU manager threads, optimize LRU scanning, and allow single-page flushing to proceed while an LRU batch flush is running.

* Improves InnoDB buffer pool initialization on NUMA-enabled systems by using multi-threaded memory allocation. The improvement reduces initialization time and can shorten server startup for instances with large buffer pools.

* Improves InnoDB performance for highly concurrent range-select workloads by reducing `BUF_BLOCK_MUTEX` contention when multiple threads access the same buffer pool page. The improvement increases throughput for read workloads that repeatedly access the same hot pages.

* Adds timestamps to the Group Communication System (GCS) debug trace file. The timestamps make large trace files easier to analyze and help correlate Group Replication communication events with other server activity.

## Known issues and limitations

* Percona Distribution for MySQL 8.4.11 includes MySQL Shell 8.4.10. Starting with MySQL Shell 26.7, Oracle uses a single-version release model and has discontinued the MySQL Shell 8.4 and 9.7 release series. As a result, MySQL Shell 8.4.11 is not available. MySQL Shell 8.4.10 remains the latest release in the 8.4 series.
    
* In 8.4.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-24](https://github.com/percona/orchestrator/releases/tag/v3.2.6-24){:target="_blank"}     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona Toolkit     | [3.7.1-3](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-3-released-2026-04-17){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| Percona XtraBackup  | [8.4.0-6](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-6.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [8.4.10](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/news-8-4-10.html){:target="_blank"}    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [8.4.11](https://dev.mysql.com/doc/relnotes/mysql-router/26.7/en/news-26-7-0.html){:target="_blank"}    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 8.4.11 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-ps-8.4.11.html){:target="_blank"}.
