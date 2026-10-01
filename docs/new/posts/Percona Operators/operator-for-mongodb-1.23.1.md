---
date: 2026-10-05
description: >
  Percona Operator for MongoDB 1.23.1 has been released on October 5, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.23.1 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.23.1 has been released on October 5, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/1.23.1/quickstart.html){:target="_blank"}.

This release focuses on day-to-day operations. New features and improvements include:

* **Keep query router logs after a restart**. [Persistent logging](https://docs.percona.com/percona-operator-for-mongodb/1.23.1/persistent-logging.html){:target="_blank"} now covers `mongos` Pods, so connection failures, slow queries, and routing decisions stay available after a rollout or restart when you configure storage for those logs.

* **Choose how often the Operator contacts HashiCorp Vault**. When system user passwords live in HashiCorp Vault, you set how often the Operator reads them and how often it signs in again.


Learn more in Percona Operator for MongoDB 1.23.1 [release notes](https://docs.percona.com/percona-operator-for-mongodb/1.23.1/RN/Kubernetes-Operator-for-PSMONGODB-RN1.23.1.html){:target="_blank"}.
