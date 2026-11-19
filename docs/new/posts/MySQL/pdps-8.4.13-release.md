---
date: 2026-11-23
description: >
  Percona Distribution for MySQL 8.4.13 using Percona Server for MySQL has been released on Monday, November 23, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.4.13 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.4.13 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.4/index.html){:target="_blank"} has been released on Monday, November 23, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.4/installing.html){:target="_blank"}.

## Percona Server for MySQL 8.4.13-13

Percona Server for MySQL 8.4.13-13 introduces the following new features and improvements:

* Adds the [Keyring Encrypted File component](https://docs.percona.com/percona-server/8.4/use-percona-keyring-encrypted-file.html){:target="_blank"}.

* Adds support for Password-Based Key Derivation Function 2 (PBKDF2), a stronger method for protecting passwords, backported from Percona Server for MySQL 9.7.

* Adds improved MyRocks statistics that can be shared with the query optimizer, helping it choose better query plans.

* Adds support for proxied users with long group names or IDs in the OpenID Connect (OIDC) authentication plugin. The OIDC plugin also ships with an installation script, so you no longer have to install and configure the plugin manually.

* Adds support for regular expressions in Audit Log Filter component filters. The Audit Log Filter also logs query text in UTF-8 instead of the client character set, so JSON logs and `audit_log_read()` output no longer contain invalid UTF-8.

* Adds a “dropping table” thread state, so `DROP TABLE` operations are no longer shown as “checking permissions”.

* Improves performance under heavy concurrent workloads by reducing contention on internal block mutexes and by improving how InnoDB tracks read-write lock holders.

## Known issues and limitations

* Percona Distribution for MySQL 8.4.13 includes MySQL Shell 26.10.0. Starting with MySQL Shell 26.7, Oracle uses a single-version release model and has discontinued the MySQL Shell 8.4 and 9.7 release series. As a result, MySQL Shell 8.4.13 is not available. MySQL Shell 26.10.0 is backward compatible with all currently supported MySQL Server versions, including MySQL 8.4.

* In 8.4.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component           | Version   | Description                                |
| ------------------- | --------- | -------------------------------------------|
| Orchestrator        | [3.2.6-26](https://github.com/percona/orchestrator/releases/tag/v3.2.6-26.1){:target="_blank"}     | The replication topology manager for Percona Server for MySQL|
| ProxySQL            | [2.7.3-1.6](https://docs.percona.com/proxysql/2.7.3.html){:target="_blank"}     | A high performance, high-availability, protocol-aware proxy for MySQL|
| Percona Toolkit     | [3.7.1-4](https://docs.percona.com/percona-toolkit/release_notes.html#v3-7-1-4-released-2026-07-02){:target="_blank"}     | The set of scripts to simplify and optimize database operation. |
| Percona XtraBackup  | [8.4.0-8](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-8.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers|
| MySQL Shell         | [26.10.0](https://dev.mysql.com/doc/relnotes/mysql-shell/26.10/en/news-26-10-0.html){:target="_blank"}    | An advanced client and code editor for MySQL Server|
| MySQL Router        | [8.4.13-13](https://dev.mysql.com/doc/relnotes/mysql-router/26.10/en/news-26-10-0.html){:target="_blank"}    | Lightweight middleware that provides transparent routing between your application and back-end MySQL servers|

Learn more in Percona Distribution for MySQL 8.4.13 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.4/release-notes-ps-8.4.13.html){:target="_blank"}.
