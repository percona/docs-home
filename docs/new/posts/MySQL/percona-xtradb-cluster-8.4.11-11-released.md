---
date: 2026-10-05
description: >
  Percona XtraDB Cluster 8.4.11-11 has been released on October 05, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.4.11-11 has been released

<!-- more -->

[Percona XtraDB Cluster 8.4.11-11](https://docs.percona.com/percona-xtradb-cluster/8.4/){:target="_blank"} has been released on October 05, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.4/quickstart-overview.html){:target="_blank"}.

This release is based on Percona Server for MySQL 8.4.11-11.

## Percona XtraDB Cluster 8.4.11-11

!!! note "Upgrade to 9.7"

    To upgrade from Percona XtraDB Cluster 8.4 to 9.7, use 9.7.2 or newer as the target version. Upgrading from 8.4.11 to 9.7.1 is not supported.

Percona XtraDB Cluster 8.4.11-11 introduces the following improvements:

* When `pxc_strict_mode` is set to `ENFORCING` or `MASTER`, Percona XtraDB Cluster now also enables `sql_require_primary_key` globally, so tables without a primary key can no longer be created or altered. Previously, you could create such a table but could not run DML statements on it. While `pxc_strict_mode` is `ENFORCING` or `MASTER`, setting `sql_require_primary_key` to `OFF` returns an error. The server applies the setting at startup and whenever `pxc_strict_mode` changes to one of these modes. Existing connections keep their current session value, and new connections use the updated global value.

* Adds the `repl.force_sst_after_inconsistency` Galera provider option. When the option is enabled and a node is voted out of the cluster because of a data inconsistency, the node removes the `grastate.dat` file on shutdown. On the next start, the node performs a full State Snapshot Transfer (SST) instead of an Incremental State Transfer (IST), which ensures a consistent dataset. The option is disabled by default and can be changed at runtime with `wsrep_provider_options`.

## Percona Server for MySQL 8.4.11-11

Percona Server for MySQL 8.4.11-11 introduces the following new features and improvements:

* Adds OpenID Connect (OIDC) authentication and authorization. Users can authenticate with Identity tokens issued by external Identity Providers (IDPs) instead of MySQL passwords. The OIDC plugin supports multiple IDPs, maps IDP groups to MySQL roles, supports proxy users based on group membership, and refreshes JSON Web Key Set (JWKS) signing keys at runtime. Find more information in [OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/openid-connect-authentication.html) and in [Get started with OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/quickstart-openid-connect.html).

* Improves InnoDB performance for workloads limited by Least Recently Used (LRU) flush speed. The improvements reduce LRU list mutex contention, restore dedicated LRU manager threads, optimize LRU scanning, and allow single-page flushing to proceed while an LRU batch flush is running.

* Improves InnoDB buffer pool initialization on NUMA-enabled systems by using multi-threaded memory allocation. The improvement reduces initialization time and can shorten server startup for instances with large buffer pools. Starting in 8.4.11, `innodb_numa_interleave` controls only interleaved NUMA allocations. Pre-faulting buffer pool pages on startup is controlled by `innodb_buffer_pool_populate`. Both default to `ON`, so default behavior matches 8.4.10. If you set `innodb_numa_interleave=OFF` to skip pre-faulting in 8.4.10, also set `innodb_buffer_pool_populate=OFF` in 8.4.11. See [Defaults and tuning guidance for 8.4](https://docs.percona.com/percona-server/8.4/8.4-defaults-and-tuning.html#numa-interleave-and-buffer-pool-populate).

* Improves InnoDB performance for highly concurrent range-select workloads by reducing `BUF_BLOCK_MUTEX` contention when multiple threads access the same buffer pool page. The improvement increases throughput for read workloads that repeatedly access the same hot pages.

* Adds timestamps to the Group Communication System (GCS) debug trace file. The timestamps make large trace files easier to analyze and help correlate Group Replication communication events with other server activity.

## MySQL 8.4.11

Improvements and bug fixes introduced by Oracle for MySQL 8.4.11 and included in Percona Server for MySQL are the following:

* Fixed an issue that could cause an InnoDB deadlock during `B-tree` page merges while concurrent searches were running. (Bug #39129182)

* Fixed an issue where stricter InnoDB row-size validation could reject or generate warnings for table definitions accepted by earlier MySQL LTS releases. (Bug #120323, Bug #39249507)

* Fixed an issue that could produce incorrect values when adding an `AUTO_INCREMENT` column to an existing InnoDB table. (Bug #115136, Bug #37105825)

* Fixed an issue that could return incorrect results when a scalar subquery and its outer query referenced the same Common Table Expression (CTE). (Bug #120403, Bug #39321676)

* Fixed an issue that could prevent the server from starting on Oracle Linux 9 or Red Hat Enterprise Linux 9 when `innodb_redo_log_encrypt=ON` was configured. (Bug #39181231)

Find the complete list of bug fixes and changes in the [MySQL 8.4.11 release notes :octicons-link-external-16:](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-11.html).
