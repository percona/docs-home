---
date: 2025-11-27
description: >
  Percona Distribution for PostgreSQL 18.1.1 has been released on November 27, 2025.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 18.1.1 has been released

<!-- more -->

We're excited to announce the release of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/18/index.html){:target="_blank"} 18.1.1!

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/18/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/18/major-upgrade.html){:target="_blank"}.

This release of Percona Distribution for PostgreSQL 18.1.1 provides the following enhancements:

- **Parallel logical replication** for improved throughput during initial data synchronization
- **Faster in-place upgrades** via `pg_upgrade` performance improvements
- **Enhanced monitoring** with new statistics views for `pg_stat_io` and background writer activity
- **Security improvements**, including expanded SSL/TLS configuration options
- **Performance optimizations** for query execution and index management
- Added support for **asynchronous I/O** (AIO)

These features make PostgreSQL 18 a major step forward in scalability, observability, and operational efficiency. This release also includes `pg_stat_monitor` 2.3.1 for advanced query-level observability, `pg_tde` 2.1 for Transparent Data Encryption and more.

## ### `pg_tde` is now a standalone package

Starting with PostgreSQL 18, `pg_tde` is no longer shipped with the server package. If your cluster relies on `pg_tde`, you must install the package manually.

For more information on installing `pg_tde`, see [Install pg_tde :octicons-link-external-16:](https://docs.percona.com/pg-tde/install.html).

## Tarball updates

The binary tarballs for x86_64 and ARM64 architectures have been updated in this release. The following libraries and components have new versions:

- pgbouncer: 1.25.0
- pgpool2: 4.6.3
- etcd: 3.5.24
- PostGIS: 3.5.4
- set_user: 4.2.0
- pg_repack: 1.5.3
- pg_stat_monitor: 2.3.1
- pgBackRest: 2.57.0
- Patroni: 4.1.0
- HAProxy: 2.8.16
- pgvector: 0.8.1
- libxml2: 2.12.10
- pg_tde: 2.1.0

See [Install Percona Distribution for PostgreSQL from binary tarballs](https://docs.percona.com/postgresql/18/tarball.html) for the download links.

For details specific to Percona Distribution for PostgreSQL 18.1.1, see the [release notes](https://docs.percona.com/postgresql/18/release-notes/release-notes-v18.1.1.html){:target="_blank"}.
