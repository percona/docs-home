---
date: 2026-06-24
description: >
  Percona XtraBackup 8.4.0-6 has been released on Wednesday, June 24, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-6 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-6](https://docs.percona.com/percona-xtrabackup/8.4/){:target="_blank"} has been released on Wednesday, June 24, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="_blank"}.

## Release highlights

Percona XtraBackup 8.4.0-6 release includes new features, improvements and bug fixes.

* Percona XtraBackup introduces the [`--check-tables`](https://docs.percona.com/percona-xtrabackup/8.4/innodb-btree-check.html){:target="_blank"} option to validate the structural integrity of InnoDB B-tree indexes during the [`--prepare`](https://docs.percona.com/percona-xtrabackup/8.4/xtrabackup-option-reference.html#prepare){:target="_blank"} phase. Validation during `--prepare` helps detect corrupted indexes before restore or production deployment.

* Percona XtraBackup introduces [backup size reporting](https://docs.percona.com/percona-xtrabackup/8.4/backup-size-reporting.html){:target="_blank"} for successful backups. Percona XtraBackup now records backup size in `xtrabackup_info` and reports the same information in the XtraBackup error log. Backup size reporting helps estimate storage requirements, check that backups work correctly, and plan restores for compressed and streamed backups.

* Percona XtraBackup adds support for Azure Storage accounts with [Hierarchical Namespace (HNS)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace){:target="_blank"} enabled in `xbcloud delete`. Percona XtraBackup now correctly removes backups from Azure Data Lake Storage Gen2 environments where deletion previously failed due to unsupported HNS behavior.

* Percona XtraBackup improves `--copy-back` and `--move-back` handling for backups created from servers with non-default InnoDB configuration paths. Percona XtraBackup now automatically processes configuration values stored in `backup-my.cnf`, avoiding restore failures caused by custom `innodb_data_file_path` and related settings.

* Percona XtraBackup improves sparse file handling efficiency by removing redundant `fallocate(PUNCH_HOLE)` calls from `local_write_sparse`.

* Percona XtraBackup improves incremental backup speed for instances containing around one million tables, reducing the time required for incremental backups to complete.

## Packaging notes

* Percona XtraBackup 8.4 adds support for Ubuntu 26.04.

We recommend downloading Percona XtraBackup for the same platform as your MySQL-compatible server. For example, if your server runs on an ARM64 platform, download the Percona XtraBackup version for ARM64.

Learn more in Percona XtraBackup 8.4.0-6 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-6.html){:target="_blank"}.
