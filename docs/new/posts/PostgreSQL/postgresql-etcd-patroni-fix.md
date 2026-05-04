---
date: 2026-04-24
description: >
  Percona Distribution for PostgreSQL Patroni 4.1.2 update is now available on April 24, 2026.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Patroni 4.1.2 update for Percona Distribution for PostgreSQL

<!-- more -->

We have updated Patroni to version 4.1.2 across all supported versions of Percona Distribution for PostgreSQL.

We have also updated how extensions are enabled in the PostgreSQL Docker images.

## Why this update matters

This update ensures compatibility with the recently updated [etcd version (3.5.29)](postgresql-etcd-sec-fix.md).

Additionally, Patroni 4.1.2 includes:

- Compatibility fixes for etcd 3.5.29
- Stability improvements
- Bug fixes for Kubernetes environments

## What changed

- Patroni has been upgraded to version 4.1.2 in all supported repositories:

  - ppg-14
  - ppg-15
  - ppg-16
  - ppg-17
  - ppg-18

## Docker image configuration changes

- The `ENABLE_TDE` flag is no longer supported  
- `shared_preload_libraries` is empty by default  

### How to enable extensions

To enable extensions, specify them explicitly using PostgreSQL configuration parameters. For example:

```bash
-c shared_preload_libraries=pg_tde,pg_stat_monitor
```

### Updated image tags

The following tags are available in `percona/percona-distribution-postgresql` and `percona/percona-distribution-postgresql-with-postgis`:

| Major version | Full tag |
|---|---|
| 14 | 14.22 |
| 15 | 15.17 |
| 16 | 16.13 |
| 17 | 17.9 |
| 18 | 18.3 |

Major version tags (`14`, `15`, `16`, `17`, `18`) also point to the updated images.

## What you should do

Update your packages from the Percona repositories:

- Update along with etcd to ensure compatibility
- Validate cluster behavior after upgrade
