---
date: 2024-11-14
description: >
  Percona Operator for MongoDB 1.18.0 has been released on Thursday, November 14, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.18.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.18.0 has been released on Thursday, November 14, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Enhancements of the declarative user management](https://docs.percona.com/percona-operator-for-mongodb/users.html#custom-mongodb-roles){:target="_blank"} make it possible to create custom MongoDB roles on various databases just like users via the Custom Resource
* [Partial restores](https://docs.percona.com/percona-operator-for-mongodb/backups-restore.html#selective-restore){:target="_blank"} allow selectively restoring only with the desired subset of data (a specific database or a collection) from a backup which is useful to reduce time on restore operations when fixing corrupted data fragment
* [Splitting the replica set of the database cluster](https://docs.percona.com/percona-operator-for-mongodb/replication-multi-dc.html){:target="_blank"} over multiple Kubernetes clusters is now possible, useful to get a fault-tolerant system in which all replicas are in different data centers

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.18.0.html#deprecation-rename-and-removal){:target="_blank"} are the following ones:

* [Automated storage scaling with Volume Expansion capability](https://docs.percona.com/percona-operator-for-mongodb/scaling.html#automated-scaling-with-volume-expansion-capability){:target="_blank"} is now disabled by default and has to be explicitly enabled with a [dedicated option](https://docs.percona.com/percona-operator-for-mongodb/operator.html#enablevolumeexpansion){:target="_blank"}
* A number of Service exposure Custom Resource options [were renamed](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.18.0.html#deprecation-rename-and-removal){:target="_blank"} to provide a unified experience with other Percona Operators

Learn more in Percona Operator for MongoDB 1.18.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.18.0.html){:target="_blank"}.
