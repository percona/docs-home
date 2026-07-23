---
date: 2026-07-23
description: >
  Percona XtraDB Cluster 8.0.46-37 has been released on Thursday, July 23, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.0.46-37 has been released

<!-- more -->

[Percona XtraDB Cluster 8.0.46-37](https://docs.percona.com/percona-xtradb-cluster/8.0/){:target="_blank"} has been released on Thursday, July 23, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.0/quickstart-overview.html){:target="_blank"}.

Percona XtraDB Cluster 8.0.46-37 is the final release of the Percona XtraDB Cluster 8.0 series. MySQL 8.0 and Percona Server for MySQL 8.0 have reached their End of Life (EOL).

Percona offers tailored support before, during, and after your move to Percona XtraDB Cluster 8.4, and can keep your existing Percona XtraDB Cluster 8.0 deployment secure and performant post-EOL through [MySQL 8.0 Post-EOL Support from Percona](https://www.percona.com/mysql-8-0-eol-support/){:target="_blank"}.

Percona XtraDB Cluster 8.0.46-37 is based on Percona Server for MySQL and contains all improvements and bug fixes available in Percona Server for MySQL 8.0.46-37.

## MySQL 8.0.46

Improvements and bug fixes provided by Oracle for MySQL 8.0.46 and included in Percona Server for MySQL are documented in the [MySQL 8.0.46 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-46.html){:target="_blank"}.

## Security updates

This release addresses the following security vulnerabilities:

* [CVE-2026-48165](https://www.cve.org/CVERecord?id=CVE-2026-48165): Fixed a vulnerability in the handling of the `wsrep_sst_donor` and `wsrep_sst_receive_address` system variables that could allow a high-privileged user to execute arbitrary shell commands with the privileges of the `mariadbd` process during State Snapshot Transfer (SST). This fix was backported from MariaDB.

* [CVE-2026-49261](https://www.cve.org/CVERecord?id=CVE-2026-49261): Fixed a vulnerability that, when `wsrep_notify_cmd` was enabled, could allow a remote attacker to execute arbitrary shell commands by embedding commands in a joiner's node name. This fix was backported from MariaDB.

## Percona XtraDB Cluster 8.0.46-37

This release contains the following bug fixes:

* Fixed an issue where nodes could leave the cluster after an error in a stored procedure.

* Fixed an issue that caused `Inconsistency` errors on backup nodes when pending DDL conflicted with `FLUSH TABLES WITH READ LOCK` (FTWRL).

* Restored the `mysqlchk` script to the Percona XtraDB Cluster 8.0 package and binary tarball distributions.

* Added `wsrep` threads to `performance_schema.variables_by_thread`.

* Fixed an issue where inconsistency voting under high load could trigger an internal deadlock that permanently paused Flow Control.

* Fixed an issue that prevented nodes with Event Scheduler tasks and `read_only` enabled from joining the cluster after a successful State Snapshot Transfer (SST).

* Fixed an issue where `CREATE ROLE` statements were not replicated when the validate password plugin was enabled.

* Fixed an issue where `GRANT` privileges differed between in-place upgraded and newly installed Percona XtraDB Cluster instances.

* Fixed an issue where nodes could leave the cluster when `SET PASSWORD` included a single quote (for example, `SET PASSWORD="a'b"`).

* Fixed an issue where `SELECT ... FOR UPDATE SKIP LOCKED` could trigger a fatal InnoDB error and crash the node under concurrent transactional workloads.

* Fixed an issue where corrupted Galera `gcache` files during node restart with `gcache.recover=yes` could cause out-of-memory conditions or `std::bad_alloc` crashes.

* Fixed an issue where `WSREP` applier threads inherited `tx_read_only=true`, causing replication failures and node inconsistency.

* Fixed an issue where peer-supplied fields in `wsrep_notify_cmd` were not sanitized before shell substitution, which could allow a malicious joiner to execute arbitrary commands on the donor.

* Fixed an issue where `wsrep_sst_receive_address` values were not validated on the joiner side, which could allow shell injection during State Snapshot Transfer (SST).

For a full list of the bug fixes, and to learn more, see the Percona XtraDB Cluster 8.0.46-37 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.0/release-notes/8.0.46-37.html){:target="_blank"}.
