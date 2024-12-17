---
date: 2024-01-17
description: >
  Percona Distribution for MySQL 8.0.35 using Percona XtraDB Cluster has been released on Wednesday, January 17, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.35 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.35 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html) has been released on Wednesday, January 17, 2024.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html).

Improvements and bug fixes provided by Oracle for MySQL 8.0.35 and included in Percona Server for MySQL are the following:

* Upgraded the linked OpenSSL library to OpenSSL 3.0.10.
* Removed the printed query string limit to display the characters for a detected deadlock section of the engine status log.
* Fixed a procession of single-character tokens by an FTS parser plugin.

**Deprecations**

A future release may remove deprecated variables and options. The usage of these deprecated items may cause a warning. We recommend migrating from deprecated variables and options as soon as possible.

This release deprecates the following variables and options:

* The `binlog_transaction_dependency_tracking` server system variable

* The `old` and `new` server system variables

* The `--character-set-client-handshake` server variable

* `INFORMATION_SCHEMA.PROCESSLIST`

* The implementation of the `SHOW PROCESSLIST` command that uses the `INFORMATION_SCHEMA.PROCESSLIST` table

* The `performance_schema_show_processlist` variable

Learn more in Percona Distribution for MySQL 8.0.35 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.35.html){:target="_blank"}.

