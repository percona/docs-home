---
date: 2025-01-21
description: >
  Percona Operator for MongoDB 1.19.0 has been released on Tuesday, January 21, 2025.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.19.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.19.0 has been released on Tuesday, January 21, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* The new [filesystem](https://docs.percona.com/percona-operator-for-mongodb/backups-storage.html#remote-file-server){:target="_blank"} backup storage type allows users to mount a remote file server directory via Network File System (NFS) protocol to a local directory, and make Percona Backup for MongoDB using this directory as a storage for backups
* A new improvement for the [declarative management of custom MongoDB users](https://docs.percona.com/percona-operator-for-mongodb/users.html#unprivileged-users){:target="_blank"} brings the possibility to use automatic generation of users passwords
* Percona Server for MongoDB 8.0 [is now supported](https://docs.percona.com/percona-operator-for-mongodb/images.html){:target="_blank"} by the Operator in addition to 6.0 and 7.0 versions.

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.19.0.html#deprecation-rename-and-removal){:target="_blank"} are the following ones:

* The `psmdbCluster` option from the `deploy/backup/backup.yaml` manifest used for [on-demand backups](https://docs.percona.com/percona-operator-for-mongodb/backups-ondemand.html){:target="_blank"}, which was deprecated since the Operator version 1.12.0 in favor of the `clusterName` option, has been removed and is no longer supported.
* Percona Server for MongoDB 5.0 has reached its end of life and in no longer supported by the Operator

Learn more in Percona Operator for MongoDB 1.19.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.19.0.html){:target="_blank"}.
