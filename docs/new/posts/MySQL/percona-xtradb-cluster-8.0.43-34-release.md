---
date: 2025-09-22
description: >
  Percona XtraDB Cluster 8.0.43-34 has been released on Monday, September 22, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.0.43-34 has been released

<!-- more -->

[Percona XtraDB Cluster 8.0.43-34](https://docs.percona.com/percona-xtradb-cluster/8.0/){:target="_blank"} has been released on Monday, September 22, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.0/quickstart-overview.html){:target="_blank"}.

Percona XtraDB Cluster 8.0.43-34 is based on Percona Server for MySQL and contains all improvements and bug fixes available in Percona Server for MySQL 8.0.43-34.

### Percona XtraDB Cluster 8.0.43-34

Improves State Snapshot Transfer (SST) by retrying Incremental State Transfer (IST) when initial SST attempts fail before any data changes, preventing unnecessary full data transfers.

### Percona Server for MySQL 8.0.43-34

Implements Link-Time Optimization (LTO) to generate more optimized release binaries, resulting in improved performance for specific workloads.

### MySQL 8.0.43

Improvements and bug fixes provided by Oracle for MySQL 8.0.43 and included in Percona Server for MySQL are the following:

* Fixed an issue where rebuilding a primary key with duplicate entries could cause the server to stop unexpectedly. (Bug #37822992)

* Fixed an issue related to dropping columns that were part of an index. (Bug #37726881)

* Fixed an issue with indexing spatial datatype columns. (Bug #36682518)

* Fixed an issue where creating a secondary index on a `VARCHAR` column could exceed configured memory limits, with the amount allocated being directly related to the `value of innodb_ddl_buffer_size`, leading to errors such as ERROR 1136 (21S01): Column count doesn't match value count at row 1. (Bug #37233273)

### Build & packaging notes

* The official packages were built with the `WITH_LTO=ON` flag to enable the Link-Time Optimization (LTO) feature.

Learn more in Percona XtraDB Cluster 8.0.43-34 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.0/release-notes/8.0.43-34.html){:target="_blank"}.