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

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that provides data encryption at rest.

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"} and [leave your feedback](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82){:target="_blank"}.

* **WAL encryption is now Generally Available (GA)**

The WAL (Write-Ahead Logging) encryption feature is now fully supported and production-ready, it adds secure logging to `pg_tde`, expanding Percona's PostgreSQL encryption coverage by enabling secure, transparent encryption of write-ahead logs using the same key infrastructure as data encryption.

To learn more, refer to the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/release-notes-v2.0.html){:target="_blank"}
