---
date: 2025-11-25
description: >
  Percona Transparent Data Encryption (`pg_tde`) 2.1 has been released on November 25, 2025
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) 2.1 has been released

<!-- more -->

[`pg_tde` :octicons-link-external-16:](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that brings native data-at-rest encryption, now with production-ready WAL encryption.

Try it out using the [installation guidelines :octicons-link-external-16:](https://docs.percona.com/pg-tde/install.html){:target="_blank"}.

## Added support for PostgreSQL 18.1

`pg_tde` is fully supported with the Postgres 18.1 version.

## Added support for AIO

Added support for **asynchronous I/O (AIO)** which is now the default I/O mechanism.

## Added support for Vault and OpenBao namespaces

Implemented support for the "namespace" feature in Vault Enterprise and OpenBao, available both on the CLI and on the HTTP interface using the `X-Vault-Namespace` header.

!!! note

    For details, see the pg_tde 2.1 [release notes :octicons-link-external-16:](https://docs.percona.com/pg-tde/release-notes/release-notes-v2.1.html).

## Upgrade today

Upgrade today to secure your PostgreSQL with WAL encryption, explore improved docs, and [share your feedback on what you’d like to see next :octicons-link-external-16:](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82).
