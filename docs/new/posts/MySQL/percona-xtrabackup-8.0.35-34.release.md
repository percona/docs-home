---
date: 2025-08-11
description: >
  Percona XtraBackup 8.0.35-34 has been released on Monday, August 11, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.0.35-34 has been released

<!-- more -->

[Percona XtraBackup 8.0.35-34](https://docs.percona.com/percona-xtrabackup/8.0/){:target="\_blank"} has been released on Monday, August 11, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.0/quickstart-overview.html){:target="\_blank"}.

Starting with Percona XtraBackup 8.0.34, you can take backups of different versions of Percona Server for MySQL. [See list of Supported versions](https://docs.percona.com/percona-xtrabackup/8.0/supported-versions.html){:target="\_blank"}.

This release also contains a bug fix:

- When streaming a backup that has been compressed (using `lz4` or `zstd` with the `--compress` option), the decompression process, whether performed by `xbstream --decompress` or `xtrabackup --decompress`, requires a significant amount of time.

This release supports Red Hat Enterprise Linux 10.

[Learn more in Percona XtraBackup 8.0.35-34 release notes](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-34.0.html){:target="\_blank"}.
