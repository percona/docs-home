---
date: 2024-10-08
description: >
  Percona Distribution for MySQL 8.0.39 using Percona Server for MySQL has been released on Tuesday, October 08, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.0.39 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.39 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){.md-button} has been released on Tuesday, October 08, 2024.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){.md-button}.

Improvements and bug fixes provided by Oracle for MySQL 8.0.38, MySQL 8.0.39 and included in Percona Server for MySQL are the following:

* The server could not restart successfully after creating a large number of tables (8001 or more). This issue, Bug #36808732, is a regression of Bug #33398681.

* Enhanced performance of tablespace file scanning during startup. (Bug #110402, Bug #35200385)

* InnoDB file system operations now consistently perform an fsync on the parent directory when carrying out directory-altering tasks. (Bug #36174938)

* Worker jobs now include details about the relay log file that initiated the transaction, rather than relying on the default specified by relay_log.

Learn more in Percona Distribution for MySQL 8.0.39 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-ps-v8.0.39.html){:target="_blank"}.

