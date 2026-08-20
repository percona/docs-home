---
date: 2026-08-05
description: >
  Percona Distribution for MySQL 9.7.1 using Percona Server for MySQL has been released on Wednesday, August 05, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 9.7.1 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 9.7.1 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/9.7/index.html){:target="_blank"} has been released on Wednesday, August 05, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/9.7/installing.html){:target="_blank"}.

## Builds and packaging

* Percona Server for MySQL releases include a mixture of Profile-Guided Optimization (PGO) and non-PGO builds. Where PGO is enabled, the compiler uses runtime profiling data from representative workloads to guide optimization, which can improve throughput and reduce latency compared with non-PGO builds.

* See [Profile-Guided Optimization (PGO) and non-PGO builds](https://docs.percona.com/percona-server/9.7/pgo.md) for benefits, considerations, and which build is published for each platform.

* In Percona Server for MySQL 9.7.1-1 only, Debian and Ubuntu (APT) packaging was reorganized to align more closely with upstream MySQL. Several packages were split into separate components, which may affect upgrades and dependency resolution compared with earlier Percona Server releases. The APT packages are:

    * percona-server-client-core
    * percona-server-client-plugins
    * percona-server-client
    * percona-server-common
    * percona-server-server-core
    * percona-server-server
    * percona-telemetry-agent

## Known issues

* This release does not include the Percona Toolkit component. We will add it once a Percona Toolkit version compatible with MySQL {{vers}} becomes available.
    
* In 9.7.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/9.7/en/replication-options-replica.html#sysvar_terminology_use_previous) system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-23](https://github.com/percona/orchestrator/releases/tag/v3.2.6-23)     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [3.0.9](https://docs.percona.com/proxysql/3.0.9.html)     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona XtraBackup  | [9.7.1-rc1](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.1-rc1.html)| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [9.7.1](https://dev.mysql.com/doc/relnotes/mysql-shell/9.7/en/news-9-7-1.html)    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [9.7.1](https://dev.mysql.com/doc/relnotes/mysql-router/9.7/en/news-9-7-1.html)    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 9.7.1 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/9.7/release-notes-ps-9.7.1-1.html){:target="_blank"}.

