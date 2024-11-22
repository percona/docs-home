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
---
<!-- more -->

Percona Backup for MongoDB 2.7.0 has been released on October 10, 2024.

This release primarily focuses on bug fixing and code stability. Find the list of fixes in Percona Backup for MongoDB 2.7.0 [release notes](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html){:target="_blank"}.

Yet it also offers the ability to increase the security of your cloud infrastructure. Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. However, if you run Percona Operator for MongoDB, there's the limitation: a restore does not work with this feature without the modification of default serviceAccount. We plan to cover this case in future releases of the Operator.



<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>