---
date: 2026-10-04
description: >
  Percona XtraBackup 9.7.2-2 has been released on Wednesday, November 04, 2026.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup 9.7.2-2 has been released

<!-- more -->

[Percona XtraBackup 9.7.2-2](https://docs.percona.com/percona-xtrabackup/9.7/){:target="_blank"} has been released on Wednesday, November 04, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtrabackup/9.7/quickstart-overview.html){:target="_blank"}.

## Release Highlights
 
Percona XtraBackup 9.7.2-2 supports backing up Percona Server for MySQL 9.7.x and MySQL 9.7.x.
 
Use the Percona XtraBackup 8.4 series to take backups of Percona Server for MySQL 8.4.x and MySQL 8.4.x series.

We recommend that you download the Percona XtraBackup for the same platform as the MySQL-compatible server. For example, if your server is on an ARM64 platform, you should download and use the Percona XtraBackup for ARM64 for that operating system.
 
Percona XtraBackup 9.7.2-2 release includes new features, improvements, deprecations, and bug fixes.

### Renamed options

Percona XtraBackup 9.7.2-2 renames the following options. The new names describe the phase or the action of each option more clearly.

| Deprecated name | New name | Used with |
| --------------- | -------- | --------- |
| `--apply-log-only` | [`--apply-redo-only`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#apply-redo-only){:target="_blank"} | `--prepare` |
| `--incremental-basedir` | [`--backup-incremental-base`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#backup-incremental-base){:target="_blank"} | `--backup` |
| `--incremental-dir` | [`--prepare-incremental-from-dir`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#prepare-incremental-from-dir){:target="_blank"} | `--prepare` |

Percona XtraBackup still accepts the old names but prints a deprecation warning at startup. If you pass an old name and its new name in the same command, Percona XtraBackup reports an error and does not start. A future Long-Term Support (LTS) release will remove `--apply-log-only`, `--incremental-basedir` and `--incremental-dir`.

### Deprecated options

Percona XtraBackup 9.7.2-2 deprecates the following options.

| Option | Use instead |
| ------ | ----------- |
| `--create-ib-logfile` | No replacement. The option has no effect. |
| [`--innodb`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#innodb){:target="_blank"} | No replacement. The option has no effect. |
| [`--log`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#log){:target="_blank"} | No replacement. The option has no effect. |
| [`--no-version-check`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#no-version-check){:target="_blank"} | No replacement. The option has no effect. |
| `--rebuild-threads` | No replacement. The option has no effect. |
| [`--rsync`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#rsync){:target="_blank"} | [`--lock-ddl=REDUCED`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#lock-ddl){:target="_blank"} |

Percona XtraBackup still accepts the options but prints a deprecation warning at startup. A future release will remove the options.
 
## New features and improvements

Percona XtraBackup 9.7.2-2 adds the following features and improvements.
 
* Adds the `--history-host`, `--history-port`, `--history-socket`, `--history-user`, `--history-password`, and `--history-ssl-*` options to [store the backup history on a different server](https://docs.percona.com/percona-xtrabackup/9.7/store-backup-history.html#store-backup-history-on-a-different-server){:target="_blank"}. Before, Percona XtraBackup always wrote the history record to the server you back up. The write failed when that server ran with `super_read_only` enabled, for example, a replica or a secondary member of a single-primary Group Replication cluster. The `--incremental-history-name` and `--incremental-history-uuid` options also read the base LSN from the history server.
 
* Improves parallel processing performance. With `--parallel`, Percona XtraBackup now processes files in largest-first order instead of discovery order. Large tables and partitions start processing earlier, so you spend less time waiting for large files after other parallel tasks complete. The improvement applies to `--backup`, `--prepare --prepare-incremental-from-dir`, `--copy-back`, `--move-back`, and `--decompress`.

* Adds the [`--apply-redo-only`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#apply-redo-only){:target="_blank"} option as the new name for `--apply-log-only`. Both names work the same way. If you pass both options in the same command, Percona XtraBackup reports an error and does not start. For details, see [Prepare an incremental backup](https://docs.percona.com/percona-xtrabackup/9.7/prepare-incremental-backup.html){:target="_blank"}.

* Adds phase-specific names for the incremental backup options. Use [`--backup-incremental-base`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#backup-incremental-base){:target="_blank"} instead of `--incremental-basedir` with `--backup`. Use [`--prepare-incremental-from-dir`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#prepare-incremental-from-dir){:target="_blank"} instead of `--incremental-dir` with `--prepare`. The old and new names work the same way. If you pass an old name and its new name in the same command, Percona XtraBackup reports an error and does not start.

* Fixes an issue where incremental backups with page tracking read the unchanged pages between blocks of changed pages. On large tablespaces, the incremental backup could read nearly the whole file. Percona XtraBackup now skips the unchanged page ranges between blocks of changed pages. (Thank you to Reto Giezendanner for your contribution)

* Fixes an issue where incremental backups with page tracking were slow when a tablespace had scattered changed pages. Percona XtraBackup read each scattered changed page on its own, and thousands of small reads take much longer than a few large reads. Percona XtraBackup now reads nearby changed pages together when reading the unchanged pages between them costs less than another read. Percona XtraBackup measures your storage at the start of the backup, so you do not need to change the configuration. The backup contents and size stay the same. Use the new [`--page-tracking-merge-gap`](https://docs.percona.com/percona-xtrabackup/9.7/xtrabackup-option-reference.html#page-tracking-merge-gap){:target="_blank"} option to set a fixed gap, or set the option to `0` to turn off the behavior. For details, see [Read scattered changed pages](https://docs.percona.com/percona-xtrabackup/9.7/page-tracking.html#read-scattered-changed-pages){:target="_blank"}.

Learn more in Percona XtraBackup 9.7.2-2 [release notes](https://docs.percona.com/percona-xtrabackup/9.7/release-notes/9.7.2-2.html){:target="_blank"}.
