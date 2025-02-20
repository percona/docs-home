---
date: 2025-02-20
description: >
  Percona Operator for MongoDB 1.19.1 has been released on Thursday, February 20, 2025.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.19.1 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.19.1 has been released on Thursday, February 20, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

This release [fixes a bug](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.19.1.html#bugs-fixed){:target=”_blank”} by disabling MongoDB balancer during restores to follow requirements of Percona Backup for MongoDB 2.8.0.

[Known limitations](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.19.1.html#known-limitations){:target="_blank"} are the following ones:

* Operator versions 1.19.0 and 1.19.1 have a recommended MongoDB version set to 7.0 because point-in-time recovery may fail on MongoDB 8.0 if sharding is enabled and the Operator version is 1.19.x. Therefore, upgrading to Operator 1.19.0/1.19.1 is not recommended for sharded MongoDB 8.0 clusters.

Learn more in Percona Operator for MongoDB 1.19.1 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.19.1.html){:target="_blank"}.
