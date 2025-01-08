---
date: 2025-01-02
description: >
  Percona Distribution for MySQL 8.0.40 using Percona Server for MySQL has been released on Thursday, January 02, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.0.40 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.40 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Thursday, January 02, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

Improvements and bug fixes provided by Oracle for MySQL 8.0.40 and included in Percona Server for MySQL are the following:

* Changes in MySQL 8.0.33 caused queries using joins on InnoDB tables to perform worse because refactoring affected functions that were previously inline.

* The server crashed when it tried to update columns altered with NULL as the default value using the INSTANT algorithm.

* The server could crash during DELETE or UPDATE operations if a column was dropped using the INSTANT algorithm.

* Importing a table created under a different sql_mode sometimes led to schema mismatches, risking data corruption in secondary indexes. The fix now includes integrity checks on the imported tablespace.

* Rebuilding tables with secondary indexes required more file I/O operations compared to MySQL 8.0.26, which slowed down query performance.

Learn more in Percona Distribution for MySQL 8.0.40 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-ps-v8.0.40.html){:target="_blank"}.
