---
date: 2025-09-25
description: >
  Percona Backup for MongoDB 2.11.0 has been released on September 25, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.11.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.11.0 has been released on September 25, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Ensure successful upload of any size backup. PBM now splits backup files that exceed the object size limit for backup storage into pieces and uploads them to the storage. When reading data from the storage, PBM merges these pieces into a single file. You can redefine the default size limit using PBM configuration and ensure your backups are uploaded regardless of the size. Learn more about how to do it in the [documentation](https://docs.percona.com/percona-backup-mongodb/features/split-merge-backup.html){:target="_blank"} .

* Percona Backup for MongoDB drops support of MongoDB 6.0. Existing functionality in Percona Backup for MongoDB remains compatible with MongoDB 6.0 and Percona Server for MongoDB 6.0; however, further enhancements and bug fixes are no longer tested against this version.

* Known limitation for using GCS with HMAc keys. When you run backups to GCS via HMAC keys, incomplete backups may be incorrectly marked as successful if network interruptions occur during the backup process. This results in corrupted or partially uploaded archives being stored and treated as valid backups, which can later fail during restore operations. This issue is addressed in [PBM-1605](https://perconadev.atlassian.net/browse/PBM-1605). Until the issue is resolved, we recommend using a native GCS connection type with JSON keys rather than HMAC keys to ensure backup integrity.

