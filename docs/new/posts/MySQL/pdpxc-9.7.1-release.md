---
date: 2026-09-10
description: >
  Percona Distribution for MySQL 9.7.1 using Percona XtraDB Cluster has been released on September 10, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 9.7.1 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 9.7.1 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/9.7/index.html){:target="_blank"} has been released on September 10, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/9.7/installing.html){:target="_blank"}.

* Percona XtraDB Cluster uses Profile-Guided Optimization (PGO) builds to improve runtime performance. PGO uses profiling data from representative workloads to guide compiler optimizations, which can improve throughput and reduce latency. Percona XtraDB Cluster packages are built with PGO enabled.

    See [Profile-Guided Optimization (PGO) and non-PGO builds](https://docs.percona.com/percona-server/9.7/pgo.html){:target="_blank"} for more information about PGO benefits and considerations.

* In Percona XtraDB Cluster 9.7, packaging was reorganized to align more closely with upstream MySQL, consistent with the equivalent change in Percona Server for MySQL 9.7. Several packages were split into separate components, which may affect upgrades and dependency resolution compared with earlier Percona XtraDB Cluster releases.

    The APT packages (Debian and Ubuntu) are:

    * percona-xtradb-cluster-client-core
    * percona-xtradb-cluster-client-plugins
    * percona-xtradb-cluster-client
    * percona-xtradb-cluster-common
    * percona-xtradb-cluster-server-core
    * percona-xtradb-cluster-server
    * percona-xtradb-cluster-garbd
    * percona-telemetry-agent

    The YUM packages (RHEL, CentOS, Oracle Linux) are:

    * percona-xtradb-cluster-client
    * percona-xtradb-cluster-client-plugins
    * percona-xtradb-cluster-server
    * percona-xtradb-cluster-shared
    * percona-xtradb-cluster-garbd
    * percona-xtradb-cluster-icu-data-files
    * percona-telemetry-agent

## Known issues

* This release does not include the Percona Toolkit component. We will add it once a Percona Toolkit version compatible with MySQL {{vers}} becomes available.
    
* In 9.7.x environments, the ProxySQL binlog reader can fail to initialize because it uses legacy commands, such as SHOW MASTER STATUS. Some internal counters also use outdated terminology. To address most terminology issues, enable the [terminology_use_previous](https://dev.mysql.com/doc/refman/9.7/en/replication-options-replica.html#sysvar_terminology_use_previous){:target="_blank"} system variable on the database server. This workaround addresses only terminology compatibility and may not fix all failures.

## Supplied components

Review each component’s release notes for What’s new, improvements, or bug fixes. The following is a list of the components supplied with the Percona Server for MySQL-based variation of the Percona Distribution for MySQL.

| Component               | Version   | Description                                |
| ----------------------- | --------- | -------------------------------------------|
| Percona XtraBackup      | [9.7.1-rc1](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.1-rc1.html){:target="_blank"}| An open-source hot backup utility for MySQL-based servers that doesn’t lock your database during the backup.|
| HAProxy                 | [3.4.4](https://git.haproxy.org/?p=haproxy-3.4.git;a=commit;h=7f03ae65c28605152c7a1a9ba7d9d0bcfb50f8b0){:target="_blank"} | A high-availability and load-balancing solution for Percona XtraDB Cluster. This is a default proxy.|
| ProxySQL                | [3.0.9](https://docs.percona.com/proxysql/3.0.9.html){:target="_blank"}| A high performance, high-availability, protocol-aware proxy for MySQL.          |
| replication_manager.sh   | [1.0](https://docs.percona.com/percona-distribution-for-mysql/9.7/replication-manager-for-pxc.html){:target="_blank"}  | A tool to manage multi-source replication between multiple Percona XtraDB Cluster clusters. |

Learn more in Percona Distribution for MySQL 9.7.1-1 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/9.7/release-notes-pxc-9.7.1-1.html){:target="_blank"}.
