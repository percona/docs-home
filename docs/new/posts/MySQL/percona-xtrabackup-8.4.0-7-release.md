---
date: 2026-09-17
description: >
  Percona XtraBackup 8.4.0-7 has been released on Thursday, September 17, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-7 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-7](https://docs.percona.com/percona-xtrabackup/8.4/){:target="_blank"} has been released on Thursday, September 17, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="_blank"}.

## Release highlights

Percona XtraBackup 8.4.0-7 release includes new features, improvements and bug fixes.

* Improves parallel processing performance by processing files in largest-first order instead of discovery order. With `--parallel`, large tables and partitions start processing earlier, reducing the time spent waiting for large files after other parallel tasks complete. The improvement applies to `--backup`, `--prepare --incremental-dir`, `--copy-back`, `--move-back`, and `--decompress`.

* Improves incremental backups with page tracking by skipping unchanged page ranges between blocks of changed pages. This reduces unnecessary I/O, especially for large tablespaces, and keeps the amount of data read closer to the amount of changed data.

* Improves incremental backups with page tracking by reading nearby changed pages together instead of reading each page separately. This improves backup performance when changed pages are scattered. Backup contents and size remain unchanged. Set [`--page-tracking-merge-gap=0`](https://docs.percona.com/percona-xtrabackup/8.4/xtrabackup-option-reference.html#-page-tracking-merge-gap) to read each changed page separately.

We recommend that you download the Percona XtraBackup for the same platform as the MySQL-compatible server. For example, if your server is on an ARM64 platform, you should download and use the Percona XtraBackup for ARM64 for that operating system.

Learn more in Percona XtraBackup 8.4.0-7 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-7.html){:target="_blank"}.
