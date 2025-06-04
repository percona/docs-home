---
date: 2025-06-04
description: >
  Percona Operator for MongoDB 1.20.1 has been released on June 4, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.20.1 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.20.1 has been released on June 4, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

This release fixes the failing backup that was caused by the Operator sending multiple requests to PBM. The issue was fixed by bypassing the cache for the backup controller and enabling direct communication with the API server for sending backup requests.

Learn more in Percona Operator for MongoDB 1.20.1 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.20.1.html){:target="_blank"}.
