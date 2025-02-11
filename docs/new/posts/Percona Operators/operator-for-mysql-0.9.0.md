---
date: 2025-02-11
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 0.9.0 has been released on Tuesday, February 11, 2025.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona Server for MySQL 0.9.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/ps/index.html){:target="_blank"} 0.9.0 has been released on Tuesday, February 11, 2025.
Version 0.9.0 of the Percona Operator for MySQL is still **a tech preview release**, and it is **not recommended for production environments**. You can try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/ps/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Scheduled backups](https://docs.percona.com/percona-operator-for-mysql/ps/backups-scheduled.md){:target="_blank"} are now supported in addition to on-demand ones
* A new [percona.com/delete-mysql-pvc](https://docs.percona.com/percona-operator-for-mysql/ps/operator.html#metadata-name){:target="_blank"} Finalizer can be used to automatically delete Persistent Volume Claims for the database cluster Pods after the cluster deletion event (off by default)

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN0.9.0.html#deprecation-and-removal){:target="_blank"} are the following ones:

* The `psmdbCluster` option from the `deploy/backup/backup.yaml` manifest used for [on-demand backups](https://docs.percona.com/percona-operator-for-mongodb/backups-ondemand.html){:target="_blank"}, which was deprecated since the Operator version 1.12.0 in favor of the `clusterName` option, has been removed and is no longer supported.
* Both upgrade to the Operator version 0.9.0 and the appropriate database cluster upgrade can not be done in a usual way due to a number of internal changes, and [require additional manual operations](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN0.9.0.html#known-limitations).

Learn more in Percona Operator for MySQL based on Percona Server for MySQL 0.9.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN0.9.0.html){:target="_blank"}.
