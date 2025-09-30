---
date: 2025-10-
description: >
  Percona XtraDB Cluster 8.4.6-6 has been released on Thursday, October , 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.4.6-6 has been released

<!-- more -->

[Percona XtraDB Cluster 8.4.6-6](https://docs.percona.com/percona-xtradb-cluster/8.4/){:target="_blank"} has been released on Thursday, October , 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.4/quickstart-overview.html){:target="_blank"}.

This release is based on Percona Server for MySQL 8.4.6-6.

### Percona XtraDB Cluster 8.4.6-6

Improves State Snapshot Transfer (SST) by retrying Incremental State Transfer (IST) when initial SST attempts fail before any data changes, preventing unnecessary full data transfers.

### Percona Server for MySQL 8.4.6-6

Implements Link-Time Optimization (LTO) to generate more optimized release binaries, resulting in improved performance for specific workloads.

### MySQL 8.4.6

Bug fixes introduced by Oracle for MySQL 8.4.6 and included in Percona Server for MySQL are the following:

* Fixed an issue where rebuilding a primary key with duplicate entries could cause the server to stop unexpectedly. (Bug #37822992)

* Fixed an issue related to dropping columns that were part of an index. (Bug #37726881)

* Fixed an issue with indexing spatial datatype columns. (Bug #36682518)

* Fixed an issue where creating a secondary index on a `VARCHAR` column could exceed configured memory limits, with the amount allocated being directly related to the `value of innodb_ddl_buffer_size`, leading to errors such as ERROR 1136 (21S01): Column count doesn't match value count at row 1. (Bug #37233273)

Find the complete list of bug fixes and changes in the [MySQL 8.4.6 release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-6.html).

## Build & packaging notes

* The official packages were built with the `WITH_LTO=ON` flag to enable the Link-Time Optimization (LTO) feature.

* This release adds support for Red Hat Enterprise Linux 10.

Learn more in Percona XtraDB Cluster 8.4.6-6 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.4/release-notes/8.4.6-6.html){:target="_blank"}.

