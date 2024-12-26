---
date: 2024-05-16
description: >
  Percona Backup for MongoDB 2.5.0 has been released on May 16, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.5.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.5.0 has been released on May 16, 2024. 

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Enhanced authentication management for custom databases. If in your deployment each user has an individual database and authenticates against it, you can now restore those users when you restore these databases. This saves you extra effort of recreating users and roles. Read more about it in the [restore custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles){:target="_blank"} section. 

* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. You can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.

Learn more about other changes in Percona Backup for MongoDB 2.5.0 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html){:target="_blank"}.

