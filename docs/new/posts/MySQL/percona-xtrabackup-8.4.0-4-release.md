---
date: 2025-08-21
description: >
  Percona XtraBackup 8.4.0-4 has been released on Thursday, August 21, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-4 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-4](https://docs.percona.com/percona-xtrabackup/8.4/){:target="\_blank"} has been released on Thursday, August 21, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="\_blank"}.

This release provides the following bug fixes:

- Fixed an issue where encrypted tablespace keys were not saved when using transition keys with `--lock-ddl=reduced`, preventing prepare failures.

- Improved the decompression speed for compressed backups using lz4 or zstd with the `--compress` option, reducing processing time.

We recommend downloading Percona XtraBackup for the same platform as your MySQL-compatible server. For example, if your server runs on an ARM64 platform, download the Percona XtraBackup version for ARM64.

Learn more in Percona XtraBackup 8.4.0-4 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-4.html){:target="\_blank"}.
