---
date: 2026-03-12
description: >
  Percona Server for MySQL 8.4.8-8 has been released on Thursday, March 12, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.8-8 has been released

<!-- more -->

[Percona Server for MySQL 8.4.8-8](https://docs.percona.com/percona-server/8.4/index.html){:target="_blank"} has been released on Thursday, March 22, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html){:target="_blank"}.

### MySQL 8.4.8

Improvements and bug fixes introduced by Oracle for MySQL 8.4.8 and included in Percona Server for MySQL are the following:

* The warning associated with redo logging being disabled is no longer present, as the underlying condition that triggered the warning has been eliminated. (Bug #37645185)

* A problem affecting the handling of large insert operations has been corrected, improving stability during bulk data loads. (Bug #38208188)

* An error that could arise when running certain SQL statements has been resolved. (Bug #38573285)

* Issues encountered when generating table definitions via `SHOW CREATE TABLE` have been fixed. (Bug #38448700)

* Bug #38298692 was addressed as part of the same fix set as Bug #38448700, resolving related inconsistencies in table metadata handling. (Bug #38298692)

* Performance regressions affecting queries that rely on regular expression matching have been corrected. (Bug #114056, Bug #36326728)

* The bundled OpenSSL dependency has been updated, addressing the issue tracked under Bug #38632932. (Bug #38632932)

* A concurrency flaw in InnoDB that could occur when executing SQL through the `que_eval_sql` interface has been removed. (Bug #118705, Bug #38310595)

* A timing issue that allowed binary logs to be removed before persisted expiration settings were fully applied has been fixed. (Bug #38554467)

* A fault affecting clustered environments, where multiple instances could lose connectivity under specific conditions, has been corrected. (Bug #38380392)

* Several defects that prevented connections from closing properly when using the Thread Pool have been resolved. (Bug #38170188, Bug #36782728, Bug #38549372)

* An issue that caused gaps in GTID sequences when the `replica_skip_errors` option was enabled has been fixed. (Bug #28590993)

Find the complete list of bug fixes and changes in the [MySQL 8.4.8 release notes :octicons-link-external-16:](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-8.html){:target="_blank"}.

Learn more in Percona Server for MySQL 8.4.8-8 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.8-8.html){:target="_blank"}.
