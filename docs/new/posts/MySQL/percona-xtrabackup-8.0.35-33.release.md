---
date: 2025-05-19
description: >
  Percona XtraBackup 8.0.35-33 has been released on Monday, May 19, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.0.35-33 has been released

<!-- more -->

[Percona XtraBackup 8.0.35-33](https://docs.percona.com/percona-xtrabackup/8.0/){:target="_blank"} has been released on Monday, May 19, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.0/quickstart-overview.html){:target="_blank"}.

Starting with Percona XtraBackup 8.0.34, you can take backups of different versions of Percona Server for MySQL. [See list of Supported versions](https://docs.percona.com/percona-xtrabackup/8.0/supported-versions.html){:target="_blank"}.

This release has the following improvements:

Percona XtraBackup now processes incremental backups more efficiently with direct .delta file application during `--prepare` operations. Speed up preparation further with the `--parallel=X` option for multi-threaded processing.

`xbcloud put` now supports ObjectLock-enabled AWS S3 buckets, providing WORM (write-once-read-many) protection for your backup data. Special thanks to community contributor volver for this feature.

This release also contains a number of bug fixes:

* Fixed crashes caused by Key Management Interoperability Protocol (KMIP) component keyring usage

* Corrected invalid URL for the Boost tarball

[Learn more in Percona XtraBackup 8.0.35-33 release notes](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-33.0.html){:target="_blank"}.