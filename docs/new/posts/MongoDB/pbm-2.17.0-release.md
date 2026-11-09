---
date: 2026-10-14
description: >
  Percona Backup for MongoDB 2.17.0 has been released on October 14, 2026.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.17.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/latest/index.html){:target="_blank"} 2.17.0 has been released on October 14, 2026.

This release improves restore reliability and helps you resolve backup failures:

- **Restore index changes with physical PITR.** Physical point-in-time recovery now applies index creation, deletion, and modification operations from the oplog. Physical restores also disable the TTL monitor automatically for the duration of the restore.
- **Restore time series collections more reliably.** Fixes address index creation errors during PITR and validation errors during logical restores of collections backed up under high write throughput.
- **Find the cause of backup failures.** In sharded clusters, PBM reports the failing shard's error instead of a generic convergence timeout.
- **Delete unfinished backups.** Backups with stale heartbeats can now be deleted even when their metadata shows a `starting` or `running` state.

For time series collections with expiration, manually disable the TTL monitor before a logical restore, including PITR. Keep it disabled throughout the restore and restore its original setting afterward.

Get started with the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/latest/installation.html){:target="_blank"}.

Learn more in the [PBM 2.17.0 release notes](https://docs.percona.com/percona-backup-mongodb/latest/release-notes/2.17.0.html){:target="_blank"}.
