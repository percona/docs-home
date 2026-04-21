---
date: 2026-04-21
description: >
  Percona Distribution for PostgreSQL ETCD security patch is now available on April 21, 2026.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# ETCD security update available for Percona Distribution for PostgreSQL

<!-- more -->

We have updated the etcd packages to version 3.5.29 across all released versions in the Q1 minor update of Percona Distribution for PostgreSQL to address recently disclosed security vulnerabilities.

## What changed

etcd is upgraded to version 3.5.29 and and is available in the following Percona PostgreSQL repositories:

- ppg-14
- ppg-15
- ppg-16
- ppg-17
- ppg-18

The packages are now available in [repo.percona.com/ppg-X](https://repo.percona.com/ppg-X), where X is the repository version number.

## Addressed vulnerabilities

This update fixes the following issues in etcd:

- CVE-2026-33413 – Authorization bypass in multiple APIs
- CVE-2026-33343 – RBAC bypass via nested transactions

## What you should do

Update etcd packages from the Percona repository. Recommendation:

- Update immediately if your deployment is exposed.
- Otherwise, update during your next maintenance window.

## Update scope

This update applies to **repository packages** only. etcd tarball updates will be included in upcoming releases.

For full technical details, see the upstream [etcd announcement](https://etcd.io/blog/2026/mar20-patch-release/){:target="_blank"}.
