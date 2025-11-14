---
date: 2025-11-17
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 1.0.0 has been released on November 17, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# General Availability: Percona Operator for MySQL 1.0.0 with Group Replication

<!-- more -->

We're excited to announce the General Availability (GA) of [Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/ps/index.html){:target="_blank"} 1.0.0 with group replication. GA status means you can now safely deploy group replication clusters in production, backed by long‑term maintenance and enterprise‑grade reliability.

Asynchronous replication remains in tech preview. We don't recommend it for production yet, but encourage you to experiment in testing or staging environments and share feedback. Ax utomated pod management in Kubernetes can introduce higher failover lag compared to bare‑metal setups, we're actively working to improve the user experience in these scenarios.

This release primarily focuses on stability and bug fixing, ensuring the Operator is ready for production use. Additionally, it introduces these improvements:

* OpenShift certification in progress  
   
    Operator images are undergoing official certification. Once complete, you'll gain full support for the Operator Lifecycle Manager (OLM), enabling you to install, upgrade, and manage the Operator directly from the OpenShift console. This improvement aims to bring you closer to secure, scalable, and policy‑driven infrastructure.

* Streamlined backup and restore configuration management. 

    The Operator now always applies `xtrabackup`, `xbstream` and `xbcloud` settings defined defined in dedicated backup or restore objects over global Custom Resource settings. This gives you maximum flexibility to fine‑tune performance or customize specific backup/restore scenarios without impacting global configuration.

* Reliable cluster provisioning for large datasets and variable network conditions

    Default timeouts for read, write, and clone operations have been increased to 3600s, reducing premature failures caused by slow disk I/O during large data transfers or network delays. You can override these defaults with `BOOTSTRAP_CLONE_TIMEOUT`, `BOOTSTRAP_READ_TIMEOUT` and `BOOTSTRAP_WRITE_TIMEOUT` environment variables to meet your environment conditions.


* Deprecation, rename and removal

    * Example backup/restore configuration files are now located in `deploy/backup/` path. Update automation workflows accordingly.
   
    * Custom Resource options `spec.pmm.readinessProbes` and `spec.pmm.livenessProbes` have been renamed to `spec.pmm.readinessProbe` and `spec.pmm.livenessProbe`, respectively.


* Known limitation: multiple backup schedules for the same backup storage

    Retention policies apply only to the first schedule when multiple schedules target the same storage. Simultaneous backups to the same path may overwrite each other. See our [documentation](https://docs.percona.com/percona-operator-for-mysql/ps/backups-scheduled.html#managing-multiple-backup-schedules-in-the-same-storage){:target="_blank"} for best practices when managing multiple schedules.

Learn more in Percona Operator for MySQL based on Percona Server for MySQL 1.0.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN1.0.0.html){:target="_blank"}.
