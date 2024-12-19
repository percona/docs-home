---
date: 2024-12-18
description: >
  Percona XtraBackup 8.4.0-2 has been released on Wednesday, December 18, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-2 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-2](https://docs.percona.com/percona-xtrabackup/8.4/){:target="_blank"} has been released on Wednesday, December 18, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="_blank"}.

Percona XtraBackup 8.4.0-2 merges the MySQL 8.4 code base and introduces Percona XtraBackup 8.4.0-2 Pro build, in addition to the regular community builds.

Percona XtraBackup 8.4.0-2 Pro build includes the [capabilities](https://docs.percona.com/percona-xtrabackup/8.4/pxb-pro.html#capabilities){:target="_blank"} that are typically requested by large enterprises. These Pro builds are specifically created and tested by Percona, and the corresponding packages are supported only for Percona customers with a valid subscription. 

Percona XtraBackup 8.4.0-2 Pro build is available for the following platforms:

* Oracle Linux 9

* Ubuntu (22.04)

* Ubuntu (24.04)

* Debian (12)

Percona XtraBackup 8.4.0-2 Pro build includes the [`Reduced backup lock time`](https://docs.percona.com/percona-xtrabackup/8.4/reduction-in-locks.html){:target="_blank"} feature. With the addition of the [`--lock-ddl=REDUCED`](https://docs.percona.com/percona-xtrabackup/8.4/xtrabackup-option-reference.html#lock-ddl){:target="_blank"} option this feature minimizes the time the server remains locked by xtrabackup during both full and incremental backups. Now, you can execute `Data Definition Language` (DDL) operations while the backup is in progress.

Learn more in Percona XtraBackup 8.4.0-2 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-2.html){:target="_blank"}.

