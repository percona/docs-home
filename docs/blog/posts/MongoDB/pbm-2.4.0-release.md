---
date: 2024-03-05
description: >
  Percona Backup for MongoDB 2.4.0 has been released on March 5, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.4.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.4.0 has been released on March 5, 2024. 

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Improved cleanup of outdated data. [Delete backups of a specific type](https://docs.percona.com/percona-backup-mongodb/usage/delete-backup.html#__tabbed_2_3){:target="_blank"} that you no longer need while keeping other backup types. In addition, verify what exactly will be deleted by using the `--dry-run` flag.

* Ensure [point-in-time recovery](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html) from large size backups. This is achieved by oplog slicing running in parallel with backup snapshots which in turn prevents gaps in oplog ranges.

* Enjoy using Percona Backup for MongoDB on ARM-based workstations not only as Docker image but also as packages for the following operating systems:

   * Ubuntu 20.04 (Focal Fossa)   
   * Ubuntu 22.04 (Jammy Jellyfish)
   * Red Hat Enterprise Linux 8 and compatible derivatives
   * Red Hat Enterprise Linux 9 and compatible derivatives


Learn more about other changes in Percona Backup for MongoDB 2.4.0 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.4.0.html){:target="_blank"}.

