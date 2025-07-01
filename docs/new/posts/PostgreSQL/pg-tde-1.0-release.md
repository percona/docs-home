---
date: 2025-06-30
description: >
  Percona Transparent Data Encryption (`pg_tde`) 1.0 has been released on June 30, 2025
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) 1.0 (Generally Available) has been released

<!-- more -->

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that provides data encryption at rest.

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"} and [leave your feedback](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82){:target="_blank"}.

This release marks the GA version of `pg_tde`.

* **pg_tde 1.0 is now GA (Generally Available)**

    And stable for encrypting relational data in PostgreSQL using Transparent Data Encryption (TDE). This milestone brings production-level data protection to PostgreSQL workloads.

* **WAL encryption is still in Beta**

    The WAL encryption feature is currently still in beta and is not effective unless explicitly enabled. It is not yet production ready. Do not enable this feature in production environments.

* **Upgrade considerations**

    `pg_tde` 1.0 is **not** backward compatible with previous pg_tde versions, like Release Candidate 2, due to significant changes in code. This means you **cannot** directly upgrade from one version to another. You must do **a clean installation** of `pg_tde`.

To learn more, refer to the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/release-notes-v1.0.html){:target="_blank"}
