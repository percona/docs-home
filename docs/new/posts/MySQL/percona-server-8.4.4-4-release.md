---
date: 2025-03-18
description: >
  Percona Server for MySQL 8.4.4-4 has been released on Tuesday, March 18, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.4-4 has been released

<!-- more -->

[Percona Server for MySQL 8.4.4-4](https://docs.percona.com/percona-server/8.4/index.html){:target="_blank"} has been released on Tuesday, March 18, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html){:target="_blank"}.

### Percona Server for MySQL 8.4.4-4

* Improves the [Data masking](https://docs.percona.com/percona-server/8.4/data-masking-overview.md) performance by introducing an internal term cache. The new cache speeds up lookups for `gen_blocklist()` and `gen_dictionary()` functions by storing dictionary data in memory. However, if the dictionary table is modified directly (outside of the proper functions), the cache may become out of sync. To fix this, use the `new masking_dictionaries_flush()` function.

    Changes also affect row-based replication: dictionary changes on the source server are replicated, but the term cache on the replica doesn’t update immediately. To address this, a new system variable, `component_masking_functions.dictionaries_flush_interval_seconds`, can be set to automatically refresh the cache at specified intervals, helping replicas stay in sync.

    Find more detailed information in the [Data masking overview](https://docs.percona.com/percona-server/8.4/data-masking-overview.md) and in the [Data masking component functions](https://docs.percona.com/percona-server/8.4/data-masking-function-list.md).

* Improves the behavior of `audit_log_filter_set_user` to support wildcards in the hostname.

### MySQL 8.4.4

Improvements and bug fixes introduced by Oracle for MySQL 8.4.4 and included in Percona Server for MySQL are the following:

* Fixed an assertion in debug builds where certain IO buffer serializations caused system hangs. (Bug #37139618)

* Resolved a failure when dropping the primary key and adding a new `AUTO_INCREMENT` column as the primary key in descending order using the `INPLACE` algorithm resulted in failure. (Bug #36658450)

* Fixed incorrect results, including missing rows, in queries that used a descending primary key with the `index_merge` optimization. (Bug #106207, Bug #33767814)

* Addressed a replication channel issue where MySQL failed to stop the channel properly when large transactions were being processed, and `STOP REPLICA` was requested. This issue also prevented graceful server shutdown, requiring process termination or system restart. (Bug #115966, Bug #37008345)

Learn more in Percona Server for MySQL 8.4.4-4 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.4-4.html){:target="_blank"}.

