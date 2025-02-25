---
date: 2025-02-26
description: >
  Percona Server for MySQL 8.0.41-32 has been released on Wednesday, February 26, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.41-31 has been released

<!-- more -->

[Percona Server for MySQL 8.0.41-31](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Wednesday, February 26, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

### Percona Server for MySQL 8.0.41-32

* Extends the [Encryption user-defined functions](https://docs.percona.com/percona-server/8.0/encryption-functions.html){:target="_blank"} with the following:

     * Added support for `pkcs1`, `oaep`, or `no` padding for RSA encrypt and decrypt operations

     * Added support for `pkcs1` or `pkcs1_pss` padding for RSA sign and verify operations

     * Added the `encryption_udf.legacy_padding_scheme` system variable to manage legacy padding schemes

     * Added the character set awareness

* Improves the [Data masking](https://docs.percona.com/percona-server/8.0/data-masking-overview.html){:target="_blank"} performance by introducing an internal term cache. The new cache speeds up lookups for `gen_blocklist()` and `gen_dictionary()` functions by storing dictionary data in memory.

    Find more detailed information in the [Data masking overview](https://docs.percona.com/percona-server/8.0/data-masking-overview.html){:target="_blank"} and in the [Data masking component functions](https://docs.percona.com/percona-server/8.0/data-masking-function-list.html){:target="_blank"}.

### MySQL 8.0.41

Improvements and bug fixes provided by Oracle for MySQL 8.0.41 and included in Percona Server for MySQL are the following:

* Fixed an assertion in debug builds where certain IO buffer serializations caused system hangs. (Bug #37139618)

* Resolved a failure when dropping the primary key and adding a new `AUTO_INCREMENT` column as the primary key in descending order using the `INPLACE` algorithm resulted in failure. (Bug #36658450)

* Fixed incorrect results, including missing rows, in queries that used a descending primary key with the `index_merge` optimization. (Bug #106207, Bug #33767814)

* Addressed a replication channel issue where MySQL failed to stop the channel properly when large transactions were being processed, and `STOP REPLICA` was requested. This issue also prevented graceful server shutdown, requiring process termination or system restart. (Bug #115966, Bug #37008345)

Learn more in Percona Server for MySQL 8.0.41-31 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.41-31.html){:target="_blank"}.
