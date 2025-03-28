---
date: 2024-12-26
description: >
  Percona Transparent Data Encryption (`pg_tde`) Beta2 has been released on December 26, 2024
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) Beta2 has been released

<!-- more -->

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that provides data encryption at rest. 

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"} and [leave your feedback](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82){:target="_blank"}.

This release of `pg_tde` extension features the following:

* Increased security of your data via the index encryption for encrypted tables and global WAL encryption.  

* More options where to store and manage principal encryption keys with the added support for KMIP-compatible servers. 

These features come with the Beta version of the `tde_heap` access method available for Percona Server for PostgreSQL.

To learn more, refer to the [pg_tde release notes](https://docs.percona.com/pg-tde/release-notes/beta2.html){:target="_blank"}