---
date: 2024-12-02
description: >
  Percona Distribution for MySQL 8.0.39 using Percona XtraDB Cluster has been released on Thursday, December 12, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.39 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.39 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){:target="_blank"} has been released on Thursday, December 12, 2024.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){:target="_blank"}.

The release also installs Percona Telemetry. Find more information in the [Telemetry on Percona XtraDB Cluster](https://docs.percona.com/percona-xtradb-cluster/8.0/telemetry.html){:target="_blank"} document.

Improvements and bug fixes provided by Oracle for  MySQL 8.0.38 and MySQL 8.0.39 and included in Percona XtraDB Cluster are the following:

* The server could not restart successfully after creating a large number of tables (8001 or more). This issue, Bug #36808732, is a regression of Bug #33398681.

* Enhanced performance of tablespace file scanning during startup. (Bug #110402, Bug #35200385)

* InnoDB file system operations now consistently perform an fsync on the parent directory when carrying out directory-altering tasks. (Bug #36174938)

* Worker jobs now include details about the relay log file that initiated the transaction, rather than relying on the default specified by `relay_log`.

Learn more in Percona Distribution for MySQL 8.0.39 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.39.html){:target="_blank"}.

