---
date: 2024-10-09
description: >
  Percona Backup for MongoDB 2.7.0 has been released on October 10, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.7.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.7.0 has been released on October 10, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release primarily focuses on bug fixing and code stability. Find the list of fixes in Percona Backup for MongoDB 2.7.0 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html){:target="_blank"}.

Yet it also offers the ability to increase the security of your cloud infrastructure. Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. However, if you run Percona Operator for MongoDB, there's the limitation: a restore does not work with this feature without the modification of default serviceAccount. We plan to cover this case in future releases of the Operator.

