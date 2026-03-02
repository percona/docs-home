---
date: 2026-03-02
description: >
  Percona XtraDB Cluster 8.0.45-36 has been released on Monday, March 2, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.0.45-36 has been released

<!-- more -->

[Percona XtraDB Cluster 8.0.45-36](https://docs.percona.com/percona-xtradb-cluster/8.0/){:target="_blank"} has been released on Monday, March 2, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.0/quickstart-overview.html){:target="_blank"}.

Percona XtraDB Cluster 8.0.45-36 is based on Percona Server for MySQL and contains all improvements and bug fixes available in Percona Server for MySQL 8.0.45-36.

## MySQL 8.0.45

Improvements and bug fixes provided by Oracle for MySQL 8.0.45 and included in Percona Server for MySQL are the following:

* InnoDB redo logging error messages now include the current LSN and redo log capacity information. New warning and error codes were added, and the MONITOR output has been enhanced to include redo log capacity details. (Bug #37645185)

## Percona XtraDB Cluster 8.0.45-36

This release contains the following bug fixes:

* Fixed an issue where the `validate-config` tool incorrectly reported that `ssl-ca`, `ssl-cert`, and `ssl-key` must all be defined to use encrypted traffic.

* Fixed an issue where Percona audit log filter execution did not sync across Percona XtraDB Cluster nodes, although the audit log filter synced correctly on async or Group Replication replicas when executed on their source.

For a full list of the bug fixes, and to learn more, see the Percona XtraDB Cluster 8.0.45-36 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.0/release-notes/8.0.45-36.html){:target="_blank"}.
