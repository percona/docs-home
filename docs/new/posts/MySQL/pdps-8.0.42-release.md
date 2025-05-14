---
date: 2025-05-
description: >
  Percona Distribution for MySQL 8.0.42 using Percona Server for MySQL has been released on Wednesday, May , 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona Server for MySQL
---

# Percona Distribution for MySQL 8.0.42 using Percona Server for MySQL has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.42 using Percona Server for MySQL](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Wednesday, May , 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

### Percona Server for MySQL 8.0.42-33

* Improves the `audit_log_filter_set_user()` UDF to accept account names with wildcard characters (`'%'` and `'_'`) in the host part. For example, you can use `‘usr1@%'`, `‘usr2%192.168.0.%’`, or `'usr3@%.mycorp.com'`.

* Updates the C++ level of the KMPI library to enhance error handling capabilities.

* Improves optimizer behavior by restoring correct handling of const tables in `test_quick_select()`. A MySQL Upstream refactor (commit [9a13c1c](https://github.com/percona/percona-server/commit/9a13c1c6971f4bd56d143179ecfb34cca8ecc018){:target="_blank"}) removed the `QEP_TAB` dependency, causing `get_quick_record_count()` to no longer pass const table information. This could lead to suboptimal range scan boundaries. The applied patch resolves the issue by explicitly passing `const_tables` to `test_quick_select()`, ensuring consistent behavior with the pre-refactor logic.

This release adds the following changes to the list of [MyRocks variables](https://docs.percona.com/percona-server/8.0/variables.html){:target="_blank"}. 

**Adds new MyRocks variables**

* [`--rocksdb_bulk_load_compression_parallel_threads`](https://docs.percona.com/percona-server/8.0/variables.html#rocksdb_bulk_load_compression_parallel_threads){:target="_blank"}
* [`--rocksdb_bulk_load_enable_unique_key_check`](https://docs.percona.com/percona-server/variables.html#rocksdb_bulk_load_enable_unique_key_check){:target="_blank"}
* [`--rocksdb_debug_skip_bloom_filter_check_on_iterator_bounds`](https://docs.percona.com/percona-server/variables.html#rocksdb_debug_skip_bloom_filter_check_on_iterator_bounds){:target="_blank"}
* [`--rocksdb_enable_udt_in_mem`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_udt_in_mem){:target="_blank"}
* [`--rocksdb_invalid_create_option_action`](https://docs.percona.com/percona-server/variables.html#rocksdb_invalid_create_option_action){:target="_blank"}
* [`--rocksdb_io_error_action`](https://docs.percona.com/percona-server/variables.html#rocksdb_io_error_action){:target="_blank"}
* [`--rocksdb_table_stats_skip_system_cf`](https://docs.percona.com/percona-server/variables.html#rocksdb_table_stats_skip_system_cf){:target="_blank"}
* [`--rocksdb_use_io_uring`](https://docs.percona.com/percona-server/variables.html#rocksdb_use_io_uring){:target="_blank"}
* [`--rocksdb_enable_instant_ddl`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_instant_ddl){:target="_blank"}
* [`--rocksdb_enable_instant_ddl_for_append_column`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_instant_ddl_for_append_column){:target="_blank"}
* [`--rocksdb_enable_instant_ddl_for_column_default_changes`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_instant_ddl_for_column_default_changes){:target="_blank"}
* [`--rocksdb_enable_instant_ddl_for_drop_index_changes`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_instant_ddl_for_drop_index_changes){:target="_blank"}
* [`--rocksdb_enable_instant_ddl_for_table_comment_changes`](https://docs.percona.com/percona-server/variables.html#rocksdb_enable_instant_ddl_for_table_comment_changes){:target="_blank"}

**Changes default values of MyRocks variables**

* [`--rocksdb_disable_instant_ddl`](https://docs.percona.com/percona-server/variables.html#rocksdb_disable_instant_ddl){:target="_blank"} - the default value is changed from `ON` to `OFF`.

* [`--rocksdb_file_checksums`](https://docs.percona.com/percona-server/variables.html#rocksdb_file_checksums){:target="_blank"} - the data type is changed from `Boolean` to `ENUM`. Also, the default value is changed from `OFF` to `CHECKSUM_OFF`.

* [`--rocksdb_compaction_readahead_size`](https://docs.percona.com/percona-server/variables.html#rocksdb_compaction_readahead_size){:target="_blank"} - the default value is changed from `0` (zero) to `2097152`.

**Deprecates MyRocks variable**

* [`--rocksdb_disable_instant_ddl`](https://docs.percona.com/percona-server/variables.html#rocksdb_disable_instant_ddl){:target="_blank"} - this variable is being deprecated and is expected to be removed in a future release.

**Removes MyRocks variables**

* [`--rocksdb-access-hint-on-compaction-start`](https://docs.percona.com/percona-server/variables.html#rocksdb_access_hint_on_compaction_start){:target="_blank"}
* [`--rocksdb_large_prefix`](https://docs.percona.com/percona-server/variables.html#rocksdb_large_prefix){:target="_blank"}
* [`--rocksdb_strict_collation_check`](https://docs.percona.com/percona-server/variables.html#rocksdb_strict_collation_check){:target="_blank"}
* [`--rocksdb_strict_collation_exceptions`](https://docs.percona.com/percona-server/variables.html#rocksdb_strict_collation_exceptions){:target="_blank"}

### MySQL 8.0.42

Improvements and bug fixes provided by Oracle for MySQL 8.0.42 and included in Percona Server for MySQL are the following:

* Fixed a problem where `CHECK TABLE` sometimes incorrectly reported that spatial indexes were corrupted. (Bug #37286473)

* Fixed an issue in InnoDB redo log recovery to improve data safety after a crash. (Bug #37061960)

* Corrected a problem where reading `index_id` values could lead to incorrect behavior with indexes. (Bug #36993445, Bug #37709706)

* Fixed a bug related to the `lower_case_table_names` setting that caused inconsistent behavior with table names on different systems. (Bug #32288105)

Learn more in Percona Distribution for MySQL 8.0.42 using Percona Server for MySQL [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-ps-v8.0.42.html){:target="_blank"}.
