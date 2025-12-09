---
date: 2025-12-10
description: >
  Percona XtraDB Cluster 8.0.44-35 has been released on Wednesday, December 10, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.0.44-35 has been released

<!-- more -->

[Percona XtraDB Cluster 8.0.44-35](https://docs.percona.com/percona-xtradb-cluster/8.0/){:target="_blank"} has been released on Wednesday, December 10, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.0/quickstart-overview.html){:target="_blank"}.

Percona XtraDB Cluster 8.0.44-35 is based on Percona Server for MySQL and contains all improvements and bug fixes available in Percona Server for MySQL 8.0.44-35.

## Percona XtraDB Cluster 8.0.44-35

Announcement – Discontinuation of the Percona PRO Program

Percona has consolidated its build offerings. The Pro builds are no longer required, and all features have been merged into the main open source Community release.

## MySQL 8.0.44

Improvements and bug fixes provided by Oracle for MySQL 8.0.44 and included in Percona Server for MySQL are the following:

* Fixed an issue that caused excessive memory chunk usage for very large buffer pools, which could lead to allocation failures. The allocation process now includes validation to ensure sufficient and stable memory allocation. (Bug #37994397)

* Fixed an issue where assertion failures could occur due to data size and bounds mismatches during DDL file operations. (Bug #37882398)

## Packaging and build notes

* Percona XtraDB Cluster 8.0 does not support Debian 13 or Red Hat Enterprise Linux 10.

* Percona XtraDB Cluster 8.0 has ended support for Ubuntu 20.04.

Learn more in Percona XtraDB Cluster 8.0.44-35 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.0/release-notes/8.0.44-35.html){:target="_blank"}.
