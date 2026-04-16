---
date: 2026-04-17
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 1.1.0 has been released on April 17, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL 1.1.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/ps/index.html){:target="_blank"} 1.1.0 has been released on April 17, 2026.

This release focuses on significant improvements to backup functionality. It introduces incremental backups, backup compression, and the long awaited point in time recovery, enabling more efficient and flexible data protection workflows.

New features and improvements introduced by this release include:

* [Point-in-time recovery](https://docs.percona.com/percona-operator-for-mysql/ps/backups-pitr.html){:target="_blank"} (tech preview) - This release introduces point-in-time recovery, giving you precise control over how far back you restore your MySQL cluster. Instead of recovering only to the moment a backup was taken, you can now roll the database forward to a specific transaction or timestamp. This is invaluable when you need to undo a bad migration, recover right before someone dropped the wrong table, or meet tighter RPO requirements with minimal data loss. 

* [Incremental backups](https://docs.percona.com/percona-operator-for-mysql/ps/backups-incremental.html){:target="_blank"} (tech preview) give you a faster, more efficient, and more cost effective way to protect your data. Instead of creating a full backup every time, the Operator now captures only the changes since the previous backup, significantly reducing backup size, storage usage, and data transfer overhead. Incremental backups also lower the load on your cluster, helping you maintain performance even during frequent backup operations

* [Compressed backups](https://docs.percona.com/percona-operator-for-mysql/ps/backups-compressed.html){:target="_blank"} empower you to make faster, lighter, and more cost efficient backups. Compressed backups work for full and incremental backups, and you can use it for both on demand and scheduled backup workflows. They are smaller in size, which means they stream to object storage quicker and consume less storage space as compared to uncompressed ones. In practice, this reduces both storage and data transfer costs.

* Improve external HAProxy checks with a configurable file descriptor limit. When HAProxy performs external MySQL health checks, it tries to close every file descriptor (FD) up to the system limit before executing the check script. If the FD limit is huge this can lead to long delays and outages. This release sets the safe FD limit to the HAProxy entrypoint which you can also override via an environmental variable. This improvement ensures external checks are fast, stable, and predictable.  


* Deprecation, rename and removal

    * Operators in Red Hat Marketplace catalog are no longer maintained. Red Hat Marketplace was discontinued in April 2025, resulting in dropped maintenance for the Operators beyond OpenShift 4.22. Use the Certified Operator Catalog instead for future updates and support.

Learn more in Percona Operator for MySQL based on Percona Server for MySQL 1.1.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN1.1.0.html){:target="_blank"}.
