---
date: 2026-03-18
description: >
  pg_upgrade is not supported with encrypted tables (pg_tde) in Percona Distribution for PostgreSQL
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - pg_tde
---

# Important: pg_upgrade is not supported with encrypted tables (pg_tde)

<!-- more -->

Percona has identified a limitation affecting the use of `pg_upgrade` with encrypted tables (`pg_tde`).

## Summary

`pg_upgrade` is not supported for clusters that contain encrypted tables.

Using `pg_upgrade` in this scenario corrupts encryption metadata in the target cluster.

## Impact

When upgrading a cluster with encrypted tables:

- Key files in the `pg_tde/` directory may be created but remain empty
- Provider metadata may be missing or incomplete

This may render encrypted data inaccessible after the upgrade.

## Who is affected

You are affected if:

- You are using `pg_tde`, or
- Your cluster contains encrypted tables

## Recommended action

Do not use `pg_upgrade` for clusters with encrypted tables.
