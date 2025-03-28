---
date: 2025-03-27
description: >
  Percona Transparent Data Encryption (`pg_tde`) Release Candidate has been released on March 27, 2025
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption (`pg_tde`) Release Candidate has been released

<!-- more -->

[`pg_tde`](https://docs.percona.com/pg-tde/index.html){:target="_blank"} is an open source extension for PostgreSQL that provides data encryption at rest. 

Try it out using the [installation guidelines](https://docs.percona.com/pg-tde/install.html){:target="_blank"} and [leave your feedback](https://forums.percona.com/c/postgresql/pg-tde-transparent-data-encryption-tde/82){:target="_blank"}.

This release of `pg_tde` extension features the following:

 **Improved performance with redesigned WAL encryption**. `pg_tde` now encrypts entire WAL files starting from the first WAL write after the server was started with the encryption turned on. The information about what is encrypted is stored in the internal key metadata. This change improves WAL encryption flow with native replication and increases performance for large scale databases. 

* **Default encryption key for single-tenancy**. If you are the owner of the entire database cluster and don't need specific keys per database, you now have a simplified way to configure encryption. Set a single default principal key and have `pg_tde` use it to encrypt all databases and tables. You can still define individual keys per database and these will take precedence over the default key. 

* **Ability to change key provider configuration**. You can now change the key provider configuration both for the current database and the entire PostgreSQL cluster using [functions](https://docs.percona.com/pg-tde/functions.html#key-provider-management){:target="_blank"}. 

* **Key management permissions**. Have a granular control over key management operations and delegate key management tasks to different roles using [functions](https://docs.percona.com/pg-tde/functions.html){:target="_blank"} for global and database key management. 

* **Additional information about principal keys and providers**. Understand the current key configuration and troubleshoot issues related to key management by [displaying additional information about principal keys and providers](https://docs.percona.com/pg-tde/functions.html){:target="_blank"}. 

* **`tde_heap_basic` access method is deprecated** due to limitations in encryption capabilities, performance impact and a potential security risk when used in production environments due to indexes remaining unencrypted. Use the `tde_heap` access method instead to enjoy full encryption capabilities. 

* **Upgrade considerations**. `pg_tde` Release Candidate is not backward compatible with `pg_tde` Beta2 due to significant changes in code. This means you cannot directly upgrade from one version to another. You must [uninstall](https://docs.percona.com/pg-tde/uninstall.html) `pg_tde` Beta2 first and then [install](https://docs.percona.com/pg-tde/install.html) and configure the new Release Candidate version.

To learn more, refer to the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/rc.html){:target="_blank"}