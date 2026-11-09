---
date: 2026-11-09
description: >
  Percona ClusterSync for MongoDB 1.1.0 has been released on November 9, 2026.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona ClusterSync for MongoDB
---

# Percona ClusterSync for MongoDB 1.1.0 has been released

<!-- more -->

[Percona ClusterSync for MongoDB (PCSM)](https://docs.percona.com/percona-clustersync-for-mongodb/){:target="_blank"} 1.1.0 has been released on November 9, 2026.

This release adds two controls for migrations:

- **Choose the write concern for target data writes.** The default remains `majority`. Lower values can reduce write stalls, but acknowledged data writes can roll back after a target primary failover.
- **Skip chunk pre-splitting during the initial clone.** Target collections retain the source shard key and MongoDB's initial chunk layout. Pre-splitting remains enabled by default.

PCSM 1.1.0 also improves clone failure reporting, pause handling, checkpoint recovery, and high availability.

Get started with the [Quickstart guide](https://docs.percona.com/percona-clustersync-for-mongodb/installation.html){:target="_blank"}.

See the [1.1.0 release notes](https://docs.percona.com/percona-clustersync-for-mongodb/release-notes/1.1.0.html){:target="_blank"} for upgrade guidance, configuration details, and recovery considerations.
