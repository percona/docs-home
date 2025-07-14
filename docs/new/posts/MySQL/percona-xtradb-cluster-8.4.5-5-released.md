---
date: 2025-07-14
description: >
  Percona XtraDB Cluster 8.4.5-5 has been released on Monday, July 14, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.4.5-5 has been released

<!-- more -->

[Percona XtraDB Cluster 8.4.5-5](https://docs.percona.com/percona-xtradb-cluster/8.4/){:target="_blank"} has been released on Monday, July 14, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.4/quickstart-overview.html){:target="_blank"}.

This release is based on Percona Server for MySQL 8.4.5-5.

### Percona XtraDB Cluster 8.4.5-5

Improves State Snapshot Transfer (SST) failure diagnostics. `garbd` now uses distinct exit codes to differentiate between donor exit, SST script failure, and garbd-initiated termination, making SST issues easier to identify and debug.

### Percona Server for MySQL 8.4.5-5

* Improves the `audit_log_filter_set_user()` UDF to accept account names with wildcard characters (`'%'` and `'_'`) in the host part. For example, you can use `‘usr1@%'`, `‘usr2%192.168.0.%’`, or `'usr3@%.mycorp.com'`.

* Updates the C++ level of the KMPI library to enhance error handling capabilities.

* Improves optimizer behavior by restoring correct handling of const tables in `test_quick_select()`. A MySQL Upstream refactor (commit [9a13c1c](https://github.com/percona/percona-server/commit/9a13c1c6971f4bd56d143179ecfb34cca8ecc018){:target="_blank"}) removed the `QEP_TAB` dependency, causing `get_quick_record_count()` to no longer pass const table information. This could lead to suboptimal range scan boundaries. The applied patch resolves the issue by explicitly passing `const_tables` to `test_quick_select()`, ensuring consistent behavior with the pre-refactor logic.

* Adds changes to the list of [MyRocks variables](https://docs.percona.com/percona-server/8.4/myrocks-server-variables.html){:target="_blank"}.

### MySQL 8.4.5

Improvements and bug fixes introduced by Oracle for MySQL 8.4.5 and included in Percona Server for MySQL are the following:

* Fixed a problem where `CHECK TABLE` sometimes incorrectly reported that spatial indexes were corrupted. (Bug #37286473)

* Fixed an issue in InnoDB redo log recovery to improve data safety after a crash. (Bug #37061960)

* Corrected a problem where reading `index_id` values could lead to incorrect behavior with indexes. (Bug #36993445, Bug #37709706)

* Fixed a bug related to the `lower_case_table_names` setting that caused inconsistent behavior with table names on different systems. (Bug #32288105)

* Fixed a bug where `mysqldump` did not properly escape certain special characters in its output. (Bug #37540722, Bug #37709163)

* The `fprintf_string()` function in `mysqldump` did not use the correct quote character for escaping strings. (Bug #37607195)

Learn more in Percona XtraDB Cluster 8.4.5-5 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.4/release-notes/8.4.5-5.html){:target="_blank"}.

