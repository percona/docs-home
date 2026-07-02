---
date: 2026-07-
description: >
  Percona XtraDB Cluster 8.4.10-10 has been released on July , 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.4.10-10 has been released

<!-- more -->

[Percona XtraDB Cluster 8.4.10-10](https://docs.percona.com/percona-xtradb-cluster/8.4/){:target="_blank"} has been released on July , 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.4/quickstart-overview.html){:target="_blank"}.

This release is based on Percona Server for MySQL 8.4.10-10.

## Percona Server for MySQL 8.4.10-10

Percona Server for MySQL 8.4.10-10 introduces the following new features and improvements:

* Integrates the new Key Management Interoperability Protocol (KMIP) library into the key management component.

* Adds JSONL (JSON Lines) output format for Audit Log Filter.

* Increases the verbosity of the data dictionary upgrade process, making it easier to diagnose issues that occur during upgrade.

* Logs SQL statements for the Audit Log Filter `table_access` class and the `read` and `insert` subclasses.

* Flushes the audit log buffer on server shutdown when the `ASYNCHRONOUS` logging strategy is in use, preventing the loss of buffered events.

* Reduces memory pressure in the Audit Log Filter component caused by VFS buffering.

* Aligns the `audit_log_filter.format=NEW` output between the 8.0 plugin and the 8.4 component.

* Optimizes performance for `mem_root_deque`.

This release addresses the list of security vulnerabilities.

## MySQL 8.4.10

Improvements and bug fixes provided by Oracle for MySQL 8.4.10 and included in Percona Server for MySQL are the following:

* Connection attribute parsing could read a length-encoded size field before verifying that the complete field was present in the packet, leading to an out-of-bounds read. A size check is now performed before reading the field. (Bug #39116965)

* A regression in row size estimation for `ROW_FORMAT=COMPRESSED` tables could cause `CREATE TABLE` to fail with `Row size too large` for tables that were accepted in earlier releases. (Bug #39129182, Bug #120323)

Learn more in Percona XtraDB Cluster 8.4.10-10 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.4/release-notes/8.4.10-10.html){:target="_blank"}.

## Builds and packaging

* Percona Server for MySQL releases include a mixture of PGO and non-PGO builds. Where Profile-Guided Optimization (PGO) is enabled, the compiler uses runtime profiling data from representative workloads to guide optimization, which can improve throughput and reduce latency compared with non-PGO builds.

* See [Profile-Guided Optimization (PGO) and non-PGO builds](https://docs.percona.com/percona-server/8.4/pgo.html) for benefits, considerations, and which build you receive for your platform.
