---
date: 2026-06-04
description: >
  Percona XtraBackup 8.0.35-36 has been released on Thursday, June 04, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.0.35-36 has been released

<!-- more -->

[Percona XtraBackup 8.0.35-36](https://docs.percona.com/percona-xtrabackup/8.0/){:target="_blank"} has been released on Thursday, June 04, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.0/quickstart-overview.html){:target="_blank"}.

Starting with Percona XtraBackup 8.0.34, you can take backups of different versions of Percona Server for MySQL. [See list of Supported versions](https://docs.percona.com/percona-xtrabackup/8.0/supported-versions.html){:target="_blank"}.

We recommend that you download the Percona XtraBackup for the same architecture as the MySQL-compatible server. For example, if your server is on an ARM64 platform, you should download and use the Percona XtraBackup for ARM64 for that operating system.

!!! important

    Percona XtraBackup 8.0.35-36 is the final release of the Percona XtraBackup 8.0 series.

    We recommend that you either upgrade to MySQL 8.4 or stay on 8.0; we'll support you.

Percona XtraBackup 8.0.35-36 release contains the following improvements:

* Percona XtraBackup adds support for Azure Storage accounts with [Hierarchical Namespace (HNS)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace) enabled in `xbcloud delete`. Percona XtraBackup now correctly removes backups from Azure Data Lake Storage Gen2 environments where deletion previously failed due to unsupported HNS behavior.

* Percona XtraBackup improves sparse file handling efficiency by removing redundant `fallocate(PUNCH_HOLE)` calls from `local_write_sparse`.

[Learn more in Percona XtraBackup 8.0.35-36 release notes](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-36.0.html){:target="_blank"}.
