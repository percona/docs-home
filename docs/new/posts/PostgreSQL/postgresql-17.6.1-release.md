---
date: 2025-09-10
description: >
  Percona Distribution for PostgreSQL 17.6.1 has been released on September 10, 2025.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.6.1 has been released

<!-- more -->

We're excited to announce the release of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.6.1!

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}.

This release of Percona Distribution for PostgreSQL 17.6.1 provides the following enhancements:

## SBOMs available for download

Percona now provides Software Bill of Materials (SBOMs) to support compliance and security audits. SBOM files are available for tarball builds.

See [Software Bill of Materials (SBOMs)](https://docs.percona.com/postgresql/17/tarball.html#software-bill-of-materials-sboms) for the full list.

## Tarball updates

The binary tarballs for x86_64 and ARM64 architectures have been updated in this release. The following libraries and components have new versions:

- LIBXSLT: 1.1.43
- LUA: 5.3.6
- LIBTIFF: 4.7.0
- EXPAT: 2.5.0
- PGPOOL: 4.6.2
- PGBACKREST: 2.56.0
- PATRONI: 4.0.6

See [Install Percona Distribution for PostgreSQL from binary tarballs](https://docs.percona.com/postgresql/17/tarball.html) for the download links.

## CVE fixes

This release includes important security fixes for the following CVEs: CVE-2012-0868, CVE-2017-7484, and CVE-2025-8715. For more details, see the [PostgreSQL 17.6](https://www.postgresql.org/docs/release/17.6/) release notes.

For details specific to Percona Distribution for PostgreSQL 17.6.1, see the [release notes](https://docs.percona.com/postgresql/17/release-notes/release-notes-v17.6.1.html){:target="_blank"}.
