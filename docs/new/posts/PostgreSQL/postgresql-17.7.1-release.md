---
date: 2025-11-15
description: >
  Percona Distribution for PostgreSQL 17.7.1 has been released on November 15, 2025.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.7.1 has been released

<!-- more -->

We're excited to announce the release of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.7.1!

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}.

## `pg_tde` is now a standalone package

Starting with this release, `pg_tde` is no longer shipped with Percona Server for PostgreSQL. However, pg_tde is installed automatically as a hard dependency.

For more information on the availability by PostgreSQL version, please see the [Install pg_tde](https://docs.percona.com/pg-tde/install.html) topic.

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

See [Install Percona Distribution for PostgreSQL from binary tarballs](https://docs.percona.com/postgresql/17/tarball.html) for the download links.

For details specific to Percona Distribution for PostgreSQL 17.7.1, see the [release notes](https://docs.percona.com/postgresql/17/release-notes/release-notes-v17.7.1.html){:target="_blank"}.
