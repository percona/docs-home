---
date: 2025-09-25
description: >
  Percona Server for MySQL 5.7.44-55 has been released on Thursday, September 25, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 5.7.44-55 has been released

<!-- more -->


[Percona Server for MySQL 5.7.44-55](https://docs.percona.com/percona-server/5.7/){:target="_blank"} has been released on Thursday, September 25, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-server/5.7/installation.html){:target="_blank"}.

This release is part of [Percona’s MySQL 5.7 Post-End-of-Life (EOL) support](https://www.percona.com/post-mysql-5-7-eol-support){:target="_blank"} program. This program provides critical updates and ensures the stability for businesses relying on MySQL 5.7 beyond its official EOL. Paying customers can access the full release, including pre-compiled binaries, through our private repository. Community members will be able to build the release from publicly available source code, which will be released on a quarterly basis.

This release includes security and non-security fixes ported from the 8.0 version.

A replication bug was fixed where a semicolon in a MySQL-specific comment could cause an incomplete entry in the binary log, which would then lead to a syntax error and replication failure on the replica. This ensures better consistency between the source and replica databases.

The `WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS` validations have been enhanced to improve the reliability and correctness of replication threads, providing more robust synchronization.

A new `--commands` option has been added to the `mysql` client. This feature allows users to disable client-side commands, which enhances security by preventing the execution of unintended commands, particularly in non-interactive mode.

A fix was implemented to prevent an unexpected server exit. This issue occurred when performing range queries on a table that included a prefixed `BLOB` or `TEXT` column within its index.

Learn more in Percona Server for MySQL 5.7.44-55 [release notes](https://docs.percona.com/percona-server/5.7/release-notes/5.7.44-55.html){:target="_blank"}.