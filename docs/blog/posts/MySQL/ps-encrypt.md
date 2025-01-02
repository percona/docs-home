---
date: 2024-12-30
description: >
  Percona Server for MySQL 8.0.40-31 adds support for padding for RSA operations.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL feature - Support for RSA padding

<!-- more -->

[Percona Server for MySQL 8.0.40-31](https://docs.percona.com/percona-server/8.0/){:target="_blank"} adds support for the following padding for RSA operations:

* pkcs1, oaep, or no padding for RSA encrypt and decrypt operations

* pkcs1 or pkcs1_pss padding for RSA sign and verify operations

Find more information in [Encryption user-defined functions](https://docs.percona.com/percona-server/8.0/encryption-functions.html){:target="_blank"}.