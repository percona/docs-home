---
date: 2025-09-01
description: >
  Percona Transparent Data Encryption (`pg_tde`) 2.0 has been released on September 01, 2025
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) 2.0 has been released

<!-- more -->

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that brings native data-at-rest encryption, now with production-ready WAL encryption.

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"}.

## WAL encryption is now Generally Available (GA)

The WAL (Write-Ahead Logging) encryption feature is now fully supported and production-ready. It adds secure logging to `pg_tde`, expanding encryption coverage by protecting both data files and WAL using the same key infrastructure.

## Major documentation update in pg_tde

Documentation has been expanded with a new WAL backup and restore guide, updated limitations, new command-line interface (CLI) utilities (`pg_tde_archive_decrypt`, `pg_tde_restore_encrypt`), and improved uninstall instructions. These updates simplify deploying and running `pg_tde` in production.

For details, [see the `pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/release-notes-v2.0.html){:target="_blank"}.

## Upgrade today

Upgrade today to secure your PostgreSQL with WAL encryption, explore improved docs, and [share your feedback on what you’d like to see next](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82).
