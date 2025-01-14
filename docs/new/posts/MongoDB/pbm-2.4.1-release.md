---
date: 2024-03-25
description: >
  Percona Backup for MongoDB 2.4.1 has been released on March 25, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.4.1 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.4.1 has been released on March 25, 2024. 

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release fixes the issue with failing incremental backups by introducing the new approach of handling the metadatada document. This document no longer contains the list of backup files which is now stored separately on the storage and is read by PBM on demand. 

Learn more about other changes in Percona Backup for MongoDB 2.4.1 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.4.1.html){:target="_blank"}.

