---
date: 2026-01-13
description: >
  Percona XtraDB Cluster 8.4.7-7 has been released on Tuesday, January 13, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 8.4.7-7 has been released

<!-- more -->

[Percona XtraDB Cluster 8.4.7-7](https://docs.percona.com/percona-xtradb-cluster/8.4/){:target="_blank"} has been released on Tuesday, January 13, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.4/quickstart-overview.html){:target="_blank"}.

This release is based on Percona Server for MySQL 8.4.7-7.

### Percona XtraDB Cluster 8.4.7-7

Announcement – Discontinuation of the Percona PRO Program

Percona has consolidated its build offerings. The Pro builds are no longer required. All features from the Percona Server for MySQL 8.4.x Pro build series and Percona XtraBackup 8.4.x Pro build series have been merged into the main open source Community release.

Starting with Percona XtraDB Cluster 8.4.7-7, the [`xtrabackup` SST method](https://docs.percona.com/percona-xtradb-cluster/8.4/state-snapshot-transfer.html#xtrabackup-sst-method){:target="_blank"} uses the [Reduced backup lock time](https://docs.percona.com/percona-xtrabackup/8.4/reduction-in-locks.html){:target="_blank"} feature. This enhancement minimizes blocking on the **Donor node** during SST process while the backup is being prepared. The Percona XtraBackup reduced lock feature is enabled by default. To modify this behavior, set the desired `lock_ddl` value in the [xtrabackup] section of the `my.cnf` configuration file. For more information about the `--lock-ddl` option and its available values, refer to the [xtrabackup command-line options](https://docs.percona.com/percona-xtrabackup/8.4/xtrabackup-option-reference.html#lock-ddl){:target="_blank"} documentation.

### Percona Server for MySQL 8.4.7-7

* The audit log plugin has been reintroduced in Percona Server for MySQL 8.4. However, it is already marked as deprecated and is planned for removal in a future release. This deprecation is due to the availability of the [audit log filter component](https://docs.percona.com/percona-server/8.4/audit-log-filter-overview.html){:target="_blank"}, which is the recommended replacement. Users should migrate to this component, which provides equivalent functionality with enhanced flexibility, performance, and filtering capabilities, ensuring continued support for auditing and compliance requirements.

### MySQL 8.4.7

Improvements and bug fixes provided by Oracle for MySQL 8.4.7 and included in Percona Server for MySQL are the following:

* Fixed an issue that caused excessive memory chunk usage for very large buffer pools, which could lead to allocation failures. The allocation process now includes validation to ensure sufficient and stable memory allocation. (Bug #37994397)

* Fixed an issue where assertion failures could occur due to data size and bounds mismatches during DDL file operations. (Bug #37882398)

Find the complete list of bug fixes and changes in the [MySQL 8.4.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-7.html){:target="_blank"}.

## Build & packaging notes

* Percona XtraDB Cluster 8.4 adds support for Debian 13.

* Percona XtraDB Cluster 8.4 has ended support for Ubuntu 20.04.

Learn more in Percona XtraDB Cluster 8.4.7-7 [release notes](https://docs.percona.com/percona-xtradb-cluster/8.4/release-notes/8.4.7-7.html){:target="_blank"}.

