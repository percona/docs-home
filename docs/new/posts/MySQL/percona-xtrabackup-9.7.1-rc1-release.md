---
date: 2026-07-15
description: >
  Percona XtraBackup 9.7.1-rc1 has been released on Wednesday, July 15, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 9.7.1-rc1 has been released

<!-- more -->

[Percona XtraBackup 9.7.1-rc1](https://docs.percona.com/percona-xtrabackup/9.7/){:target="_blank"} has been released on Wednesday, July 15, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/9.7/quickstart-overview.html){:target="_blank"}.

## Release highlights

Percona XtraBackup 9.7.1-rc1 is based on the MySQL 9.7 Long-Term Supported (LTS) release. Percona XtraBackup 9.7.1-rc1 is a Release Candidate. Interfaces and behavior are subject to change before the General Availability (GA) release.

Percona XtraBackup 9.7.1-rc1 supports backing up Percona Server for MySQL 9.7.x and MySQL 9.7.x.

Use the [Percona XtraBackup 8.4 series] to take backups of [Percona Server for MySQL 8.4.x] and MySQL 8.4.x series.

Percona XtraBackup 9.7.1-rc1 release includes new features, improvements and bug fixes.

* Percona XtraBackup introduces the [`--check-tables`](https://docs.percona.com/percona-xtrabackup/9.7/innodb-btree-check.html){:target="_blank"} option to validate the structural integrity of InnoDB B-tree indexes during the [`--prepare`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#prepare){:target="_blank"} phase. Validation during `--prepare` helps detect corrupted indexes before restore or production deployment.

* Percona XtraBackup introduces [backup size reporting](https://docs.percona.com/percona-xtrabackup/9.7/backup-size-reporting.html){:target="_blank"} for successful backups. Percona XtraBackup now records backup size in `xtrabackup_info` and reports the same information in the XtraBackup error log. Backup size reporting helps estimate storage requirements, check that backups work correctly, and plan restores for compressed and streamed backups.

* Percona XtraBackup improves sparse file handling efficiency by removing redundant `fallocate(PUNCH_HOLE)` calls from `local_write_sparse`.

## Packaging notes

* Percona XtraBackup 9.7 adds support for Ubuntu 26.04.

We recommend downloading Percona XtraBackup for the same platform as your MySQL-compatible server. For example, if your server runs on an ARM64 platform, download the Percona XtraBackup version for ARM64.

Learn more in Percona XtraBackup 9.7.1-rc1 [release notes](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.1-rc1.html){:target="_blank"}.
