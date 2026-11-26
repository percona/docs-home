---
date: 2026-11-26
description: >
  Percona XtraBackup 9.7.2-3 has been released on Thursday, November 26, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 9.7.2-3 has been released

<!-- more -->

[Percona XtraBackup 9.7.2-3](https://docs.percona.com/percona-xtrabackup/9.7/){:target="_blank"} has been released on Thursday, November 26, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/9.7/quickstart-overview.html){:target="_blank"}.

## Release highlights

Percona XtraBackup 9.7.2-3 supports backing up Percona Server for MySQL 9.7.x and MySQL 9.7.x.

Use the Percona XtraBackup 8.4 series to take backups of Percona Server for MySQL 8.4.x and MySQL 8.4.x series.

Percona XtraBackup 9.7.2-3 adds support for the Hierarchical Navigable Small World (HNSW) vector indexes introduced in Percona Server for MySQL 9.7.4-4. If you use Percona XtraBackup 9.7.2-2 or earlier to back up a Percona Server for MySQL 9.7.4-4 server that has tables with vector indexes, the backup can be incomplete or fail. To back up tables with vector indexes, use Percona XtraBackup 9.7.2-3. For details, see [Vector index](https://docs.percona.com/percona-xtrabackup/9.7/server-backup-version-comparison.html#vector-index){:target="_blank"}.

We recommend that you download the Percona XtraBackup for the same platform as the MySQL-compatible server. For example, if your server is on an ARM64 platform, you should download and use the Percona XtraBackup for ARM64 for that operating system.


Learn more in Percona XtraBackup 9.7.2-3 [release notes](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.2-3.html){:target="_blank"}.
