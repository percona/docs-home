---
date: 15-11-2025
description: >
  Percona Distribution for PostgreSQL 18.1.1 has been released on 15 November, 2025.
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

These features make PostgreSQL 18 a major step forward in scalability, observability, and operational efficiency.

## Tarball updates

The binary tarballs for x86_64 and ARM64 architectures have been updated in this release. The following libraries and components have new versions:

- LIBXSLT: 1.1.43
- LUA: 5.3.6
- LIBTIFF: 4.7.0
- EXPAT: 2.5.0
- PGPOOL: 4.6.2
- PGBACKREST: 2.56.0
- PATRONI: 4.0.6

See [Install Percona Distribution for PostgreSQL from binary tarballs](https://docs.percona.com/postgresql/18/tarball.html) for the download links.

For details specific to Percona Distribution for PostgreSQL 18.1.1, see the [release notes](https://docs.percona.com/postgresql/18/release-notes/release-notes-v18.1.1.html){:target="_blank"}.
