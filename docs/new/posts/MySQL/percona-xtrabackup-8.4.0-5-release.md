---
date: 2025-12-17
description: >
  Percona XtraBackup 8.4.0-5 has been released on Wednesday, December 17, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-5 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-5](https://docs.percona.com/percona-xtrabackup/8.4/){:target="\_blank"} has been released on Wednesday, December 17, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="\_blank"}.

Percona has consolidated its build offerings. The Pro builds are no longer required. All features from the Percona XtraBackup 8.4.x Pro build series have been merged into the main open source Community release. The [Reduced backup lock time](https://docs.percona.com/percona-xtrabackup/8.4/reduction-in-locks.html){:target="\_blank"} feature, originally introduced in [Percona XtraBackup Pro 8.4.0-2](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-2.md){:target="\_blank"} for Pro builds, is now included in the Community release starting with Percona XtraBackup 8.4.0-5.

We recommend downloading Percona XtraBackup for the same platform as your MySQL-compatible server. For example, if your server runs on an ARM64 platform, download the Percona XtraBackup version for ARM64.

This release provides the following bug fixes:

* Fixed an issue where `xbcloud` could exit because `libcurl` attempted to use a `libev` event loop after it had already been shut down. `xbcloud` will throw a warning with libcurl `8.11.x` versions and may still exit due to [CVE-2025-0665](https://github.com/advisories/GHSA-cc57-hgv8-p56r){:target="\_blank"}. The issue is resolved in libcurl `8.12.0` and later.

* The `--move-back` option was not applied when restoring RocksDB files, causing the restore process to always perform a file copy instead of moving the files back to their original location.

Learn more in Percona XtraBackup 8.4.0-5 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-5.html){:target="\_blank"}.
