---
date: 2025-03-13
description: >
  Percona Distribution for MySQL 8.0.41 using Percona XtraDB Cluster has been released on Thursday, March 13, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.41 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.41 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Thursday, March 13, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

Percona XtraDB Cluster is based on Percona Server for MySQL and contains all improvements and bug fixes available in the Percona Server for MySQL 8.0.41-32 release notes.

### Percona XtraDB Cluster 8.0.41-32

Implements the [Clone plugin for State Snapshot Transfer (SST) Method](https://docs.percona.com/percona-xtradb-cluster/8.0/clone-sst.html){:target="_blank"}. The Clone SST is a modern and efficient method that leverages MySQL's native cloning capabilities to transfer data from a Donor node to a Joiner node. It is faster and more resource-efficient compared to traditional methods like xtrabackup or rsync.

### Percona Server for MySQL 8.0.41-32

* Extends the [Encryption user-defined functions](https://docs.percona.com/percona-server/8.0/encryption-functions.html){:target="_blank"} with the following:

     * Added support for `pkcs1`, `oaep`, or `no` padding for RSA encrypt and decrypt operations

     * Added support for `pkcs1` or `pkcs1_pss` padding for RSA sign and verify operations

     * Added the `encryption_udf.legacy_padding_scheme` system variable to manage legacy padding schemes

     * Added the character set awareness

* Improves the [Data masking](https://docs.percona.com/percona-server/8.0/data-masking-overview.html){:target="_blank"} performance by introducing an internal term cache. The new cache speeds up lookups for `gen_blocklist()` and `gen_dictionary()` functions by storing dictionary data in memory.

    Find more detailed information in the [Data masking overview](https://docs.percona.com/percona-server/8.0/data-masking-overview.html){:target="_blank"} and in the [Data masking component functions](https://docs.percona.com/percona-server/8.0/data-masking-function-list.html){:target="_blank"}.

### MySQL 8.0.41

Improvements and bug fixes provided by Oracle for MySQL 8.0.41 and included in Percona Server for MySQL are the following:

* Fixed an assertion in debug builds where certain IO buffer serializations caused system hangs. (Bug #37139618)

* Resolved a failure when dropping the primary key and adding a new `AUTO_INCREMENT` column as the primary key in descending order using the `INPLACE` algorithm resulted in failure. (Bug #36658450)

* Fixed incorrect results, including missing rows, in queries that used a descending primary key with the `index_merge` optimization. (Bug #106207, Bug #33767814)

* Addressed a replication channel issue where MySQL failed to stop the channel properly when large transactions were being processed, and `STOP REPLICA` was requested. This issue also prevented graceful server shutdown, requiring process termination or system restart. (Bug #115966, Bug #37008345)

Learn more in Percona Distribution for MySQL 8.0.41 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.41.html){:target="_blank"}.

