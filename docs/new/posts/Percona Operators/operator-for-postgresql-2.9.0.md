---
date: 2026-04-01
description: >
  Percona Operator for PostgreSQL 2.9.0 has been released on April 1, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.9.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.9.0 has been released on April 1, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* PostgreSQL 18 is now the default version — New clusters get the latest major version out of the box, providing you with newer features, performance, and security without extra version hunting.

* Major upgrades are generally available — In-place major upgrades are now production-ready. Move between majors (e.g. 16 → 17 or 18) with the Operator instead of hand-rolled `pg_upgrade` and scripts.

* [Boost backup and restore performance with PVC snapshots (tech preview)](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/backups-pvc-snapshots.html){:target="_blank"} — Storage-level snapshots can shrink backup/restore time and CPU/network load on large databases as compared to streaming data through `pgBackRest` alone. By combining PVC snapshots with `pgBackRest` WAL archiving, you ensure data consistency and can make point-in-time recovery of your PostgreSQL cluster. Enable this feature via the `BackupSnapshots` feature gate; try it out in testing or staging environments and share your feedback. 

* Improve replication with [standby WAL lag detection](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/standby.html#detect-replication-lag-for-standby-cluster){:target="_blank"} — Cap how far a standby may lag. When the lag exceeds your defined threshold, the Pods become unready, the standby status shows Initializing, so replication problems are visible before apps silently read stale data.

* Centralize user identity management with [LDAP authentication](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/LDAP.html){:target="_blank"} — Enable users to authenticate via corporate LDAP directory accounts for database login. Use simple bind or bind-and-search, both supported in the Operator, and avoid manual `pg_hba.conf` churn. This improvement is easier for users and far more scalable to manage.

* [Automated TLS management with cert-manager](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/tls-cert-manager.html){:target="_blank"} — Issue, renew, and rotate cluster TLS with configurable lifetimes via cert-manager. Stay aligned with your organization's PKI and security policy.

* Operator troubleshooting with pprof — Set `PPROF_BIND_ADDRESS` on the Operator to expose CPU/memory profiling when diagnosing high usage or leaks without restarting the controller. Use with port-forward; disable when done.

* Ensure correct connections to external services with configurable DNS suffix — For vcluster or environments with custom DNS configuration, set the DNS suffix so internal names resolve correctly. Thereby connections to external services such as PMM, pgBackRest, and other integrations work correctly.

* [Volumes on sidecars](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/sidecar.html){:target="_blank"} — Mount PVCs, ConfigMaps, or Secrets into sidecars on Postgres, pgBouncer, and pgBackRest repo Pods directly. This unlocks a wide range of use cases for sidecars - from log exporters to agent that need sensitive data in secrets - all without the need for complex API calls for information exchange.

* [Configurable Operator leader election](https://docs.percona.com/percona-operator-for-postgresql/2.9.0/env-var-operator.html){:target="_blank"} — Tune lease timing for the Operator ReplicaSet to reduce election misbehavior on high-latency or constrained clusters.

* Configurable wal_level — Choose the right amount of WAL data you need for your environment (replica vs logical) and cut unnecessary I/O and CPU usage when you do not use logical replication.

* Official PostGIS images — Manage your geospatial workloads on Kubernets with ease. The Operator now uses the official PostGIS Docker image, maintained and supported by Percona. This ensures smooth operation of PostGIS alongside PostgreSQL.

* Deprecation, rename and removal:

    * Deprecated support for PMM2 - With PMM2 entering the end-of-life stage, its support is now deprecated in the Operator. It remains operational for the next two releases, after which it will be removed. Plan your migration to PMM3 to enjoy all new features and security patches supplied with this latest major version.
    * PostgreSQL 13 is removed from the Operator as it has entered the end-of-life stage upstream. If you still run this version, please upgrade to one of the supported versions before you upgrade the Operator.
    * Operators in Red Hat Marketplace catalog are no longer maintained. Red Hat Marketplace was discontinued in April 2025, resulting in dropped maintenance for the Operators beyond OpenShift 4.22. Use the Certified Operator Catalog instead for future updates and support.
    * `pg_stat_monitor` is disabled by default to prevent potential memory issues in production clusters. Re-enable it in the Custom Resource explicitly to continue using it.

Learn more in Percona Operator for PostgreSQL 2.9.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.9.0.html){:target="_blank"}.


