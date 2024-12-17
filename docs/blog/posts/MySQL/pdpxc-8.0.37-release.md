---
date: 2024-09-18
description: >
  Percona Distribution for MySQL 8.0.37 using Percona XtraDB Cluster has been released on Wednesday, September 18, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.37 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.37 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html) has been released on Wednesday, September 18, 2024.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html).

This release enhances telemetry and provides a more comprehensive explanation of how the telemetry works, including new components, metrics files, and additional methods for disabling telemetry. Find more information in the [Telemetry on Percona XtraDB Cluster](https://docs.percona.com/percona-xtradb-cluster/8.0/telemetry.html) document.

Improvements and bug fixes provided by Oracle for MySQL 8.0.37 and included in Percona Server for MySQL are the following:

* The redo log might not record a change in column order when using instant DDL, potentially leading to an inaccurate log replay during the recovery process. (Bug #35183686)

* Enhanced management of buffers has been implemented in deleting tablespaces to prevent a possible assertion failure. (Bug #35676106, Bug #36343647)

* Resolved an assertion failure associated with full-text indexes. (Bug #35836581)

**Packaging notes**

Percona XtraDB Cluster 8.0.37-29 supports Ubuntu 24.04.

Learn more in Percona Distribution for MySQL 8.0.37 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.37.html){:target="_blank"}.

