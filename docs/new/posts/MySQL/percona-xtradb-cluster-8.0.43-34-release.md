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

Improves State Snapshot Transfer (SST) failure diagnostics. `garbd` now uses distinct exit codes to differentiate between donor exit, SST script failure, and garbd-initiated termination, making SST issues easier to identify and debug.

### Percona Server for MySQL 8.0.43-34

* By implementing Link-Time Optimization (LTO), new release binaries are more optimized, leading to improved performance for specific workloads.

* The default SST timeout is often too short, which can cause the process to abort before completion.

* Creating a foreign key without sufficient privileges causes an inconsistency where the originating node fails with a `1216` error, while other nodes fail with a `1452` error during replication.

### MySQL 8.0.43

Improvements and bug fixes provided by Oracle for MySQL 8.0.43 and included in Percona Server for MySQL are the following:

* Improves the `audit_log_filter_set_user()` UDF to accept account names with wildcard characters (`'%'` and `'_'`) in the host part. For example, you can use `‘usr1@%'`, `‘usr2%192.168.0.%’`, or `'usr3@%.mycorp.com'`.

* The `audit_log_filter_set_user()` UDF now accepts wildcards in the host part of account names, allowing for more flexible user filtering.

* The KMPI library has been updated with a new C++ level to enhance its error-handling capabilities.

* A fix was implemented to restore the optimizer's correct handling of constant tables, resolving a bug that could lead to suboptimal range scan performance.

Learn more in Percona XtraDB Cluster 8.0.43-34 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.0/release-notes/8.0.43-34.html){:target="_blank"}.