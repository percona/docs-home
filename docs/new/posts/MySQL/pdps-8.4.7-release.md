---
date: 2025-12-22
description: >
  Percona Distribution for MySQL 8.4.7 using Percona Server for MySQL has been released on Monday, December 22, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.4.7 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.7 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Monday, December 22, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Percona Server for MySQL 8.4.7-7

The audit log plugin has been reintroduced in Percona Server for MySQL 8.4. However, it is already marked as deprecated and is planned for removal in a future release. This deprecation is due to the availability of the [audit log filter component](https://docs.percona.com/percona-server/8.4/audit-log-filter-overview.html), which is the recommended replacement. Users should migrate to this component, which provides equivalent functionality with enhanced flexibility, performance, and filtering capabilities, ensuring continued support for auditing and compliance requirements.

## Packaging and build notes

* Percona Server for MySQL 8.4 adds support for Debian 13.

* Percona Server for MySQL 8.4 has ended support for Ubuntu 20.04.

## Known issues and limitations

* MySQL Shell is not available as a prebuilt package for Debian 11 (Bullseye) in the Percona APT repository. Recent MySQL Shell releases are built with GNU Compiler Collection (GCC) 11 or later, while Debian 11 ships with GCC 10, making these binaries incompatible.

* ProxySQL contains counters that have not been updated to use the new terminology. Unexpected results may occur. In an 8.4.x environment, the binlog reader errors out during initialization due to the use of old terminology, such as the SHOW MASTER STATUS command.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-19](https://github.com/percona/orchestrator/releases/tag/v3.2.6-19)     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [2.7.3](https://docs.percona.com/proxysql/2.7.3.html)     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona Toolkit     | [3.7.1](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-released-2025-12-17)     | The set of scripts to simplify and optimize database operation. |
| Percona XtraBackup  | [8.4.0-5](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-5.html)| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [8.4.7](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/news-8-4-7.html)    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [8.4.7](https://dev.mysql.com/doc/relnotes/mysql-router/8.4/en/news-8-4-7.html)    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 8.4.7 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-ps-8.4.7.html){:target="_blank"}.

