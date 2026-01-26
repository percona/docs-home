---
date: 2026-01-26
description: >
  Percona XtraBackup 8.0.35-34 has been released on Monday, January 26, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.0.35-35 has been released

<!-- more -->

[Percona XtraBackup 8.0.35-35](https://docs.percona.com/percona-xtrabackup/8.0/){:target="_blank"} has been released on Monday, January 26, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.0/quickstart-overview.html){:target="_blank"}.

Starting with Percona XtraBackup 8.0.34, you can take backups of different versions of Percona Server for MySQL. [See list of Supported versions](https://docs.percona.com/percona-xtrabackup/8.0/supported-versions.html){:target="_blank"}.

Announcement – Discontinuation of the Percona PRO Program

Percona has consolidated its build offerings. The Pro builds are no longer required. All features from the Percona XtraBackup 8.0.x Pro build series have been merged into the main open source Community release. Percona XtraBackup 8.0.35-35 release build is available for Amazon Linux 2023 (AL2023). We support both AMD64 and ARM64 versions of Amazon Linux 2023.

We recommend downloading Percona XtraBackup for the same platform as your MySQL-compatible server. For example, if your server runs on an ARM64 platform, download the Percona XtraBackup version for ARM64.

This release contains the following improvements and bug fixes:

**Improvements**

* Improves restore reliability by preventing failures caused by invalid `innodb_undo_directory` in the `--copy-back` mode.

* Adds `--move-back` support for the RocksDB storage engine.

**Bug fixes**

* Fixed a performance degradation that occurred during incremental backups when the base backup contained 10,000 or more unchanged `.ibd` files.

* Fixed an issue where `xbcloud` could exit because `libcurl` attempted to use a `libev` event loop after it had already been shut down. While `xbcloud` threw a warning with `libcurl` versions `8.11.x` and potentially exited due to [CVE-2025-0665](https://github.com/advisories/GHSA-cc57-hgv8-p56r){:target="_blank"}, this behavior was resolved in libcurl 8.12.0 and later.

[Learn more in Percona XtraBackup 8.0.35-35 release notes](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-35.0.html){:target="_blank"}.
