---
date: 2024-12-23
description: >
  Percona Toolkit v3.7.0 has been released on Monday, December 23, 2024.
authors: [patrickbirch]
categories:
  - Percona Toolkit
tags:
  - Percona Toolkit
---

# Percona Toolkit v3.6.0 has been released

<!-- more -->

[Percona Toolkit v3.7.0](https://docs.percona.com/percona-toolkit/){:target="_blank"} has been released on Monday, December 23, 2024.

This version has the following new features:

* Supports MySQL 8.4

* Improved pt-secure-collect to use KDF to encrypt and decrypt user passwords. This change is incompatible with earlier versions. The pt-secure-collect tool v3.7.0 cannot decrypt data collected by earlier versions and earlier versions cannot decrypt data collect by v3.7.0.

* Updated pt-mysql-summary.

Learn more in the Percona Toolkit v3.7.0 [release notes](https://docs.percona.com/percona-toolkit/release_notes.html){:target="_blank"}.