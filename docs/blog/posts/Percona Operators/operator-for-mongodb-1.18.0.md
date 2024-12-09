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

Percona Operator for MongoDB 1.18.0 has been released on Thursday, November 14, 2024.

New features and improvements introduced by these release include:

* Enhancements of the declarative user management make it possible to create custom MongoDB roles on various databases just like users via the Custom Resource
* Partial restores allow selectively restoring only with the desired subset of data (a specific database or a collection) from a backup which is useful to reduce time on restore operations when fixing corrupted data fragment
* Splitting the replica set of the database cluster over multiple Kubernetes clusters is now possible, useful to get a fault-tolerant system in which all replicas are in different data centers

Learn more in Percona Operator for MongoDB 1.18.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.18.0.html){:target="_blank"}.


