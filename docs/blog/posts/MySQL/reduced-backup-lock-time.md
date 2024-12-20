---
date: 2024-12-18
description: >
  Reduced backup lock time
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona XtraBackup
---

# Percona XtraBackup Pro feature - Reduced backup lock time 

<!-- more -->

Percona XtraBackup Pro includes the [capabilities](https://docs.percona.com/percona-xtrabackup/8.4/pxb-pro.html#capabilities){:target="_blank"} that are typically requested by large enterprises. Percona XtraBackup Pro contains packages created and tested by Percona. These packages are supported only for Percona Customers with a subscription.

[Become a Percona Customer](https://www.percona.com/about/contact){:target="_blank"}

!!! important

    The `--lock-ddl=REDUCED` option is a [tech preview](https://docs.percona.com/percona-xtrabackup/8.4/glossary.html#tech-preview){:target="_blank"}. Before using this option in production, we recommend that you test restoring production from physical backups in your environment, and also use the alternative backup method for redundancy.

[Percona XtraBackup 8.4.0-2](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-2.html){:target="_blank"} adds the [`--lock-ddl=REDUCED`](https://docs.percona.com/percona-xtrabackup/8.4/xtrabackup-option-reference.html#lock-ddl){:target="_blank"} option to reduce the time the server remains locked by `xtrabackup` during full and incremental backups. Now, you can execute `Data Definition Language` (DDL) operations while the backup is in progress.

### Benefits

The `--lock-ddl=REDUCED` option features are as follows:

* Acquire and release the backup lock quickly: The backup process minimizes the time it holds the backup lock, allowing for concurrent DDL operations.

    ??? note "Comparing the backup duration with --lock-ddl=REDUCED"

        While we strive to provide accurate performance benchmarks, real-world results may vary depending on your hardware and software configurations.

        The following tables illustrate the approximate time differences between `--lock-ddl=ON` and `--lock-ddl=REDUCED` for local and cloud backups (Amazon S3). The `Improvement (X times)` column shows how many times less the server is locked by xtrabackup using  `--lock-ddl=REDUCED` compared to `--lock-ddl=ON`.

        === "Local backup"

	          | Data size in gigabytes | Backup duration with --lock-ddl=ON in seconds| Backup duration with --lock-ddl=REDUCED in seconds| Improvement (X times)  |
            |-----------------------------|---------------|--------------------|--------------------------|
            | 50 GB                       | 460.2 sec         | 2.169 sec             | 212.17                   |
            | 100 GB                      | 901.8 sec        | 1.305 sec             | 691.03                   |
            | 200 GB                      | 1820.4 sec       | 1.347 sec             | 1351.45                  |
            | 400 GB                      | 3580.2 sec       | 1.24 sec             | 2887.26                  |
            | 500 GB                      | 5436 sec         | 1.264 sec             | 4300.63                  |

        === "Cloud (Amazon s3) backup"

            | Data size in gigabytes | Backup duration with --lock-ddl=ON in seconds | Backup duration with --lock-ddl=REDUCED in seconds | Improvement (X times) |
            |----------------------------|---------------|--------------------|--------------------------|
            | 50 GB                      | 469.8 sec         | 3.859 sec             | 121.74                   |
            | 100 GB                     | 927.6 sec         | 4.072 sec             | 227.80                   |
            | 200 GB                     | 1851.6 sec        | 4.408 sec             | 420.05                   |
            | 400 GB                     | 3888 sec         | 3.948 sec             | 984.80                   |
            | 500 GB                     | 4896 sec         | 4.065 sec             | 1204.43                  |
        
        Using `--lock-ddl=REDUCED` leads to a dramatic reduction in backup time compared to `--lock-ddl=ON`, especially with larger data sizes.

* Track changes with redo logs: Redo logs record all file-level changes, ensuring data consistency during the backup process.
* Handle DDL operations: The backup process generates metadata files to account for any DDL operations that occur while the backup is in progress.
* Ensure consistency: The `--prepare` step processes generated metadata files and uses redo and undo logs to create a consistent database state.

### Limitations

* Certain DDL operations consume significant resources, and xtrabackup simultaneously requires I/O to copy and read files. This requirement can increase resource demand from DDL operations during the backup process.

* The master key rotation with the `ALTER INSTANCE ROTATE INNODB MASTER KEY` is prohibited while backup is in progress.

* Backups may be larger because new `DDL` operations are executed concurrently on the server, and the files generated by the server are included in the backup. Additionally, certain `DDL` operations, such as `ADD INDEX` or encryption changes to existing data files, will cause the data files to be recopied, increasing the backup size.

* The number of open file handles in your operating system should be configured to match the number of files in the server data directory.

* Taking a backup using [page tracking](https://docs.percona.com/percona-xtrabackup/8.4/page-tracking.html){:target="_blank"} is not supported with `--lock-ddl=REDUCED` option.

Learn more in the [Reduced backup lock time](https://docs.percona.com/percona-xtrabackup/8.4/reduction-in-locks.html){:target="_blank"} document.
