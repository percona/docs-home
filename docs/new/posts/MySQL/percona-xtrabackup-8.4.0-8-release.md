---
date: 2026-11-23
description: >
  Percona XtraBackup 8.4.0-8 has been released on Monday, November 23, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 8.4.0-8 has been released

<!-- more -->

[Percona XtraBackup 8.4.0-8](https://docs.percona.com/percona-xtrabackup/8.4/){:target="_blank"} has been released on Monday, November 23, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/8.4/quickstart-overview.html){:target="_blank"}.

## Release highlights

Percona XtraBackup 8.4.0-8 release includes new features, improvements, deprecations, and bug fixes.

* Adds the `--history-host`, `--history-port`, `--history-socket`, `--history-user`, `--history-password`, and `--history-ssl-*` options to [store backup history on a different server](https://docs.percona.com/percona-xtrabackup/8.4/store-backup-history.html){:target="_blank"}. Before, Percona XtraBackup always wrote the history record to the server you back up, and the write failed when that server ran with `super_read_only` enabled, for example, a replica or a secondary member of a single-primary Group Replication cluster.

* Renames the following options. The new names describe the phase or the action of each option more clearly:

    * `--apply-log-only` is renamed to `--apply-redo-only`.
    * `--incremental-basedir` is renamed to `--backup-incremental-base`.
    * `--incremental-dir` is renamed to `--prepare-incremental-from-dir`.

    Percona XtraBackup still accepts the old names but prints a deprecation warning at startup. If you pass an old name and its new name in the same command, Percona XtraBackup reports an error and does not start. A future Long-Term Support (LTS) release will remove the old names.

* Deprecates the `--create-ib-logfile`, `--innodb`, `--log`, `--no-version-check`, and `--rebuild-threads` options, which have no effect, and the `--rsync` option. Use `--lock-ddl=REDUCED` instead of `--rsync`. Percona XtraBackup still accepts the options but prints a deprecation warning at startup. A future release will remove the options.

We recommend that you download the Percona XtraBackup for the same platform as the MySQL-compatible server. For example, if your server is on an ARM64 platform, you should download and use the Percona XtraBackup for ARM64 for that operating system.

Learn more in Percona XtraBackup 8.4.0-8 [release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-8.html){:target="_blank"}.
