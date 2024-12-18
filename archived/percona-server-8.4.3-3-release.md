---
date: 2024-12-18
description: >
  Percona Server for MySQL 8.4.3-3 has been released on Wednesday, December 18, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.3-3 has been released

<!-- more -->

[Percona Server for MySQL 8.4.3-3](https://docs.percona.com/percona-server/8.4/index.html) has been released on Wednesday, December 18, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html).

Improvements and bug fixes introduced by Oracle for MySQL 8.4.3 and included in Percona Server for MySQL are the following:

* The query SELECT * FROM sys.innodb_lock_waits; now fetches only two locks per wait, instead of scanning all locks twice, improving performance under heavy load. Additionally, primary keys have been added to DATA_LOCKS and DATA_LOCK_WAITS. (Bug #100537, Bug #31763497)

* Changes in MySQL 8.0.33 caused performance degradation for queries using joins on InnoDB tables due to refactoring of functions that were previously inline.

* The server crashed when it tried to update columns altered with NULL as the default value using the INSTANT algorithm.

* The server could crash during DELETE or UPDATE operations if a column was dropped using the INSTANT algorithm.

* Importing a table created under a different sql_mode sometimes led to schema mismatches, risking data corruption in secondary indexes. The fix now includes integrity checks on the imported tablespace.

* Rebuilding tables with secondary indexes required more file I/O operations compared to MySQL 8.0.26, which slowed down query performance.

Learn more in Percona Server for MySQL 8.4.3-3 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.3-3.html){:target="_blank"}.

