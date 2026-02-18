---
date: 2026-02-29
description: >
  Percona Distribution for PostgreSQL 18.3.1 has been released on February 29, 2026.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 18.3.1 has been released

<!-- more -->

We're excited to announce the release of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/18/index.html){:target="_blank"} 18.3.1!

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/18/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/18/major-upgrade.html){:target="_blank"}.

This release of Percona Distribution for PostgreSQL 18.3.1 provides the following enhancements:

- **Parallel logical replication** for improved throughput during initial data synchronization
- **Faster in-place upgrades** via `pg_upgrade` performance improvements
- **Enhanced monitoring** with new statistics views for `pg_stat_io` and background writer activity
- **Security improvements**, including expanded SSL/TLS configuration options
- **Performance optimizations** for query execution and index management
- Added support for **asynchronous I/O** (AIO)

These features make PostgreSQL 18 a major step forward in scalability, observability, and operational efficiency. This release also includes `pg_stat_monitor` 2.3.2 for advanced query-level observability, `pg_tde` 2.1.2 for Transparent Data Encryption and more.

## `pg_tde` is now a standalone package

Starting with PostgreSQL 18, `pg_tde` is no longer shipped with the server package. If your cluster relies on `pg_tde`, you must install the package manually.

For more information on the availability by PostgreSQL version, please see the [Install pg_tde](https://docs.percona.com/pg-tde/install.html) topic.

See [Install Percona Distribution for PostgreSQL from binary tarballs](https://docs.percona.com/postgresql/18/tarball.html) for the download links.

For details specific to Percona Distribution for PostgreSQL 18.3.1, see the [release notes](https://docs.percona.com/postgresql/18/release-notes/release-notes-v18.3.1.html){:target="_blank"}.
