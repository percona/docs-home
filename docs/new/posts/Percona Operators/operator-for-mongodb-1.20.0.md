---
date: 2025-05-08
description: >
  Percona Operator for MongoDB 1.20.0 has been released on May 8, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.20.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.20.0 has been released on May 8, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Make point-in-time recovery from any storage](https://docs.percona.com/percona-operator-for-mongodb/multi-storage.html){:target="_blank"} - The Operator now natively supports multiple backup storages, enabling you to make a point-in-time recovery from any backup stored on any storage - PBM and the Operator maintain the data consistency for you.

* Improve RTO with the [added support of incremental physical backups](https://docs.percona.com/percona-operator-for-mongodb/backups.html){:target="_blank"} (tech preview) - You can now back up only the changes happened since the previous backup. Increments are smaller in size than the whole backup, speeding up the backup completion time and reducing your storage and data transfer costs. Using incremental backups and point-in-time recovery improves your recovery time objective (RTO). This feature is in the tech preview state. 

* Improved monitoring for clusters in multi-region or multi-namespace deployments in PMM - Assign a custom name to your clusters and enable PMM Server to correctly parse and display their monitoring metrics for you. For example, PMM Server now recognizes clusters in different data centers as one deployment but treats clusters deployed with the same name but in different namespaces separately. 

Learn more in Percona Operator for MongoDB 1.20.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.20.0.html){:target="_blank"}.
