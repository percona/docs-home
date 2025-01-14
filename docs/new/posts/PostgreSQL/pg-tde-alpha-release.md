---
date: 2024-03-28
description: >
  Percona Transparent Data Encryption Alpha1 has been released on March 28, 2024.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# Percona Transparent Data Encryption Alpha1 has been released.

[pg_tde](https://percona.github.io/pg_tde/main/index.html){:target="_blank"} is the open source extension for PostgreSQL developed by us to enable you to keep sensitive data safe and secure. `pg_tde` provides data encryption at rest. The encryption happens transparently in the background and doesn't affect database operations.

Try it out using the [installation instructions](https://percona.github.io/pg_tde/main/install.html){:target="_blank"}

<!-- more -->

The Alpha1 version of the extension introduces the following key features:

* You can now rotate principal keys used for data encryption. This reduces the risk of long-term exposure to potential attacks and helps you comply with security standards such as GDPR, HIPAA, and PCI DSS.

* You can now configure encryption differently for each database. For example, encrypt specific tables in some databases with different encryption keys while keeping others non-encrypted.

* Keyring improvements:

    * You can define separate keyring configuration for each database
    * You can change keyring configuration dynamically, without having to restart the server
    * The keyring configuration is now stored in a catalog separately for each database, instead of a configuration file
    * Avoid storing secrets in the unencrypted catalog by configuring keyring parameters to be read from external sources (file, http(s) request)

Learn more about `pg_tde` Alpha1 in the [release notes](https://percona.github.io/pg_tde/main/release-notes/release-notes.html#alpha-1-2024-03-28){:target="_blank"}. 
