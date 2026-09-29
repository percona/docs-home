---
date: 2026-08-20
description: >
  Percona Server for MySQL 8.4.11-11 has been released on Thursday, August 20, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.11-11 has been released

<!-- more -->

[Percona Server for MySQL 8.4.11-11](https://docs.percona.com/percona-server/8.4/index.html){:target="_blank"} has been released on Thursday, August 20, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html){:target="_blank"}.

## Percona Server for MySQL 8.4.11-11

Percona Server for MySQL 8.4.11-11 introduces the following new features and improvements:

* Adds OpenID Connect (OIDC) authentication and authorization. Users can authenticate with Identity tokens issued by external Identity Providers (IDPs) instead of MySQL passwords. The OIDC plugin supports multiple IDPs, maps IDP groups to MySQL roles, supports proxy users based on group membership, and refreshes JSON Web Key Set (JWKS) signing keys at runtime. Find more information in [OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/openid-connect-authentication.html){:target="_blank"} and in [Get started with OpenID Connect authentication](https://docs.percona.com/percona-server/8.4/quickstart-openid-connect.html){:target="_blank"}.

* Improves InnoDB performance for workloads limited by Least Recently Used (LRU) flush speed. The improvements reduce LRU list mutex contention, restore dedicated LRU manager threads, optimize LRU scanning, and allow single-page flushing to proceed while an LRU batch flush is running.

* Improves InnoDB buffer pool initialization on NUMA-enabled systems by using multi-threaded memory allocation. The improvement reduces initialization time and can shorten server startup for instances with large buffer pools.

* Improves InnoDB performance for highly concurrent range-select workloads by reducing `BUF_BLOCK_MUTEX` contention when multiple threads access the same buffer pool page. The improvement increases throughput for read workloads that repeatedly access the same hot pages.

* Adds timestamps to the Group Communication System (GCS) debug trace file. The timestamps make large trace files easier to analyze and help correlate Group Replication communication events with other server activity.

## MySQL 8.4.11

Improvements and bug fixes introduced by Oracle for MySQL 8.4.11 and included in Percona Server for MySQL are the following:

* Fixed an issue that could cause an InnoDB deadlock during `B-tree` page merges while concurrent searches were running. (Bug #39129182)

* Fixed an issue where stricter InnoDB row-size validation could reject or generate warnings for table definitions accepted by earlier MySQL LTS releases. (Bug #120323, Bug #39249507)

* Fixed an issue that could produce incorrect values when adding an `AUTO_INCREMENT` column to an existing InnoDB table. (Bug #115136, Bug #37105825)

* Fixed an issue that could return incorrect results when a scalar subquery and its outer query referenced the same Common Table Expression (CTE). (Bug #120403, Bug #39321676)

* Fixed an issue that could cause some `LEFT JOIN` queries with OR conditions to perform full table scans instead of index range scans. (Bug #113288, Bug #36061036)

* Fixed an issue that could prevent the server from starting on Oracle Linux 9 or Red Hat Enterprise Linux 9 when `innodb_redo_log_encrypt=ON` was configured. (Bug #39181231)

* Fixed an issue that caused memory leaks in the `statement_digest()` and `statement_digest_text()` functions. (Bug #104115, Bug #33073320)

Find the complete list of bug fixes and changes in the [MySQL 8.4.11 release notes :octicons-link-external-16:](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-11.html){:target="_blank"}.

Learn more in Percona Server for MySQL 8.4.11-11 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.11-11.html){:target="_blank"}.
