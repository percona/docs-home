---
date: 2026-06-18
description: >
  Percona Server for MySQL 5.7.44-58 has been released on Thursday, June 18, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 5.7.44-58 has been released

<!-- more -->


[Percona Server for MySQL 5.7.44-58](https://docs.percona.com/percona-server/5.7/){:target="_blank"} has been released on Thursday, June 18, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-server/5.7/installation.html){:target="_blank"}.

This release is part of [Percona's MySQL 5.7 Post-End-of-Life (EOL) support](https://www.percona.com/post-mysql-5-7-eol-support){:target="_blank"} program. This program provides critical updates and ensures the stability for businesses relying on MySQL 5.7 beyond its official EOL. Customers can access the full release, including pre-compiled binaries, through our private repository. Community members will be able to build the release from publicly available source code, which will be released on a quarterly basis.

This release includes bug fixes ported from the 8.0 version.

* Group Replication applier pipeline validations.

* Group Replication snapshot decode validations.

* FTS index construction ignores memory limits.

* Assertion failed in `sql_planner`: `bool Optimize_table_order::greedy_search()`.

* Crash inside of the query parser/planner/resolver.

* Prevents a server hang when a large query is killed during parsing.

* Fixes a memory leak during shutdown when replaying spatial-index MBR updates during recovery.

* Fixes a regression introduced for both spatial indexes and Varchars.

Learn more in Percona Server for MySQL 5.7.44-58 [release notes](https://docs.percona.com/percona-server/5.7/release-notes/5.7.44-58.html){:target="_blank"}.
