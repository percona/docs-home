---
date: 2024-09-02
description: >
  Percona Backup for MongoDB 2.6.0 has been released on September 2, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.6.0 has been released
---
<!-- more -->

Percona Backup for MongoDB 2.6.0 has been released on September 2, 2024.

This release provides the following features and improvements:

* [Support for multiple storages for backups and restores](https://docs.percona.com/percona-backup-mongodb/features/multi-storage.html){:target="_blank"} enables you to define additional remote backup storages and instruct PBM to which storage to save a backup. This ability helps you save on data transfer costs when using cloud storage, as well as enables you to follow closely with the requirements of your organization’s backup policy.

* [Adjust node priority for point-in-time recovery oplog slicing](https://docs.percona.com/percona-backup-mongodb/features/point-in-time-recovery.html#adjust-node-priority-for-oplog-slices){:target="_blank"} and have more control over the process. For example, prioritize geographically closest nodes for oplog slicing and reduce the network latency. 

* [Snapshot-based physical backups](https://docs.percona.com/percona-backup-mongodb/features/snapshots.html){:target="_blank"} are generally available enabling you to use this functionality on production and enjoy all the benefits of faster restores from snapshots with almost immediate access to data.

* Dropped support of MongoDB 4.4. Existing functionality remains compatible with Percona Server for MongoDB 4.4. Further enhancements and bug fixes are no longer tested against this version. 

* Packaging changes:
  
    * Added support for Ubuntu 24.04 (Noble Numbat).
    * We no longer provide packages for Ubuntu 18.04 (Bionic Beaver), Debian 10 and Red Hat Enterprise 7 and derivatives as these operating systems reached End-Of-Life

Learn more about other changes in Percona Backup for MongoDB 2.6.0 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.6.0.html){:target="_blank"}.

<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>