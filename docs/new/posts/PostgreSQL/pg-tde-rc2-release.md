---
date: 2025-05-29
description: >
  Percona Transparent Data Encryption (`pg_tde`) Release Candidate 2 (RC2) has been released on May 29, 2025
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) Release Candidate 2 (RC2) has been released

<!-- more -->

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that provides data encryption at rest.

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"} and [leave your feedback](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82){:target="_blank"}.

This release of `pg_tde` extension features the following:

 **Restricted key provider configuration to superusers**. The database owners can no longer configure key providers directly. Instead, they must refer to the superuser who manages the provider setup. This security improvement clearly separates the responsibilities between users and administrators.

* **WAL encryption supports Vault**.

    `pg_tde` now supports using the Vault keyring for secure storage and management of WAL encryption keys.

* **Automatic WAL internal key generation at server startup**.

    On each server start, a new internal key is generated for encrypting subsequent WAL records (assuming WAL encryption is enabled). The existing WAL records and their keys remain unchanged. This ensures continuity and secure key management without affecting historical data.

* **Proper removal of relation-level encryption keys on table drop**

    Previously, encrypted relation keys persisted even after dropping the associated tables, potentially leaving orphaned entries in the map file. This is now corrected, when an encrypted table is dropped, its corresponding key is also removed from the key map.

* **Fixed external tablespace data loss with encrypted partitions**

    An issue was fixed where data could be lost when the encrypted partitioned tables were moved to external tablespaces.  

* **New visibility and verification functions for default principal keys**

    Added additional functions to help you verify and inspect the state of default principal keys more easily.

* **Fixed SQL failures caused by inconsistent key provider switching**. An issue was resolved where SQL queries could fail after switching key providers while the server was running. This occurred because principal keys became inaccessible when spread across multiple keyring backends, triggering the single-provider-at-a-time design constraint. `pg_tde` now enforces consistency during provider changes to prevent a corrupted key state and query errors.

* **Upgrade considerations**. `pg_tde` Release Candidate 2 is not backward compatible with `pg_tde` Beta2 due to significant changes in code. This means you cannot directly upgrade from one version to another. You must [uninstall](https://docs.percona.com/pg-tde/uninstall.html) `pg_tde` Beta2 first and then [install](https://docs.percona.com/pg-tde/install.html) and configure the new Release Candidate version.

To learn more, refer to the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/rc2.html){:target="_blank"}
