---
date: 2024-10-09
description: >
  Percona Backup for MongoDB 2.8.0 has been released on December 12, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.8.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.8.0 has been released on December 12, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* [Better organization of selective backups](https://docs.percona.com/percona-backup-mongodb/usage/start-backup.html#__tabbed_1_3){:target="_blank"} by defining multiple namespaces when making a backup. A single backup for multiple namespaces instead of backups per namespace also enables you to save on disk space.

* [Control communication between pbm-agents residing behind different network settings and remote backup storage](https://docs.percona.com/percona-backup-mongodb/details/storage-configuration.html#support-of-multiple-endpoints-to-the-same-S3-storage){:target="_blank"}. This ensures proper functioning of PBM. 

* Simplified troubleshooting with [restoring the same collection under a different name](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-collection-under-a-different-name){:target="_blank"}. The restored collection has the same data and indexes as the one you backed up. This makes it easier to compare the data in both collections and identify what caused the issue with the database. 

* [Reduce troubleshooting time with the diagnostics report](https://docs.percona.com/percona-backup-mongodb/troubleshoot/pbm-report.html){:target="_blank"}. Use the pbm diagnostic command to collect comprehensive information about a command execution and generate a report. Either dive deep yourself or file a bug report to our experts and attach the diagnostics archive to it. 

* Improved log rotation with a [custom path for log output](https://docs.percona.com/percona-backup-mongodb/manage/logpath.html){:target="_blank"}. Outputting log information to a file at a custom path enables you to introduce log rotation, manage the system log effectively and comply to security regulations for logging and auditing. 

* Additional flexibility for backups is achieved with replacing mongodump with PBM's own dump implementation. This lifts the mongodumps' limitations and opens space for further improvements. 

* Changes in supported MongoDB versions:

   * PBM now supports Percona Server for MongoDB 8.0 and MongoDB Community 8.0. 
   * PBM no longer supports Percona Server for MongoDB 5.0 and MongoDB Community 5.0 as it entered the end-of-life stage. Existing functionality remains compatible with version 5.0. However, we will no longer test new features and improvements against this version.

