---
date: 2026-09-04
description: >
  Percona Operator for PostgreSQL 3.1.0 has been released on September 4, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---


# Percona Operator for PostgreSQL 3.1.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/3.0/){:target="_blank"} 3.1.0 has been released on September 4, 2026.

This version establishes Percona Operator for PostgreSQL as a **hard fork of the [Crunchy PGO project :octicons-link-external-16:](https://github.com/CrunchyData/postgres-operator){:target="_blank"}**, making it fully independent and empowering the Percona team and community to drive and rapidly deliver features and improvements tailored to user needs.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/quickstart.html){:target="_blank"}.

Here is a [what's new](https://docs.percona.com/new/2026/07/23/percona-operator-for-mongodb-1230-has-been-released/) style draft for Operator 3.1.0 (September 4, 2026). You can paste it as-is.

New features and improvements introduced by this release include:

* **Encrypt data at rest with `pg_tde`.** Tables, indexes, temporary files and WAL stay unreadable without the keys, even if storage is compromised. Enable `pg_tde` in the Custom Resource and configure HashiCorp Vault as the key provider. The Operator installs and configures encryption for you. Encrypted tables, backups, and restores work as usual once the Operator can reach the key. Available with PostgreSQL 17 and 18. See our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/encryption.html){:target="_blank"} to learn more.

* **Keep logs after Pod restarts and configure log rotation.** PostgreSQL and `pgBackRest` logs now persist pods restart so that you have the trail you need for an incident. The Operator uses Fluent Bit to collect logs and stream them either as JSON lines or forward them to your custom destination such as S3 or OpenTelemetry. See our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/persistent-logging.html){:target="_blank"} to learn more. Also, [tune log rotation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/logrotate.html){:target="_blank"} in the Custom Resource so you keep enough history for troubleshooting or compliance without filling the disk. 

* **Offload reads with declarative logical replicas.** Point reporting or other heavy queries at a read-only replica in the same cluster instead of the primary. Declare the replica in the Custom Resource. The Operator creates the volume, copies the data, converts the physical replica to a logical one and exposes a dedicated Service. Patroni does not promote the logical replica so the endpoint stays stable. Requires PostgreSQL 17 or later. See our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/logical-replication.html){:target="_blank"} to learn more.

* **Pause pgBouncer without dropping clients.** Set `proxy.pgBouncer.paused` for a short window to restart PostgreSQL, run a switchover or drain backends. Active queries finish while new requests wait until you resume. The pause survives Pod restarts.

* **Grow backup storage before it fills.** Automatic storage scaling now covers pgBackRest repository volumes, not only data volumes. The Operator watches usage and expands the PVC up to the limit you set, so a full `pgBackRest` repository volume no longer stops backups. See our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/scaling.html#automated-scaling-with-auto-growable-disks){:target="_blank"} to learn more.

* **Mount extra files into PostgreSQL instances.** Share full-text search dictionaries or other assets outside the data directory. Configure the volume once under `instances.extraVolumes` and every instance in the set sees the same mount. Use a ConfigMap, Secret, PersistentVolumeClaim, emptyDir, or
another volume source that Kubernetes supports. See our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/extra-volumes.html){:target="_blank"} to learn more.

* **Fit PostgreSQL into your platform PKI.** If you sync certificates from AWS Secrets Manager or External Secrets, a briefly missing Secret no longer makes the Operator generate a new CA and restart Pods. Set `certManagementPolicy: userProvidedOnly` so applications keep using the certificates already loaded. Learn more about TLS management policy in our [documentation](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/tls-cert-management-policy.html){:target="_blank"}. For client mTLS, add your corporate CA to pgBouncer with `additionalTrustedCAs` while the Operator still rotates cluster certificates. Check the [setup guide](https://docs.percona.com/percona-operator-for-postgresql/3.1.0/tls-pgbouncer-trusted-cas.html){:target="_blank"} for the steps.

* **Support of UBI 8, 9 and 10 as the base image for PostgreSQL** UBI 9 remains the default. Stay on UBI 8 for older extensions or Enterprise Linux 8, or move to UBI 10 to align with RHEL 10 and a longer support window. Treat a UBI change as an OS upgrade: collation and indexes can break until you reindex.

* **Run the Operator with community or your own PostgreSQL images.** Point `spec.image`, pgBouncer, and pgBackRest at community tags or your private registry. The Operator manages the cluster the same way. Percona-only features such as `pg_tde` are not available on community images. 

* **Evaluate PostgreSQL 19 (tech preview).** Deploy Community PostgreSQL 19 now to test the next major version and plan your upgrade before GA.

* **RKE2 and full ARM64 support.** Official RKE2 testing adds a new supported Kubernetes distribution. Full ARM64 images let you run natively on ARM-based cloud and edge clusters.

Learn more in Percona Operator for PostgreSQL 3.1.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/3.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN3.1.0.html){:target="_blank"}.


