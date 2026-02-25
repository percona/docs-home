---
date: 2026-02-15
description: >
  Percona Transparent Data Encryption (`pg_tde`) 2.1.2 has been released on 15 February, 2026.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) 2.1.2 has been released

<!-- more -->

[`pg_tde` :octicons-link-external-16:](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that brings native data-at-rest encryption, now with production-ready WAL encryption.

Try it out using the [installation guidelines :octicons-link-external-16:](https://docs.percona.com/pg-tde/install.html){:target="_blank"}.

## Integrated Hashicorp Vault namespace

The namespace of Hashicorp vault is integrated with ``pg_tde`` through the  ``pg_tde_add_global_key_provider_vault_v2`` parameter.

## Upgrade today

Upgrade today to secure your PostgreSQL with WAL encryption, explore improved docs, and [share your feedback on what you’d like to see next :octicons-link-external-16:](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82).
