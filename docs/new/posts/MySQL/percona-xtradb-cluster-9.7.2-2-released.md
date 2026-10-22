---
date: 2026-10-23
description: >
  Percona XtraDB Cluster 9.7.2-2 has been released on October 23, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster 9.7.2-2 has been released

<!-- more -->

[Percona XtraDB Cluster 9.7.2-2](https://docs.percona.com/percona-xtradb-cluster/9.7/){:target="_blank"} has been released on October 23, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/9.7/quickstart-overview.html){:target="_blank"}.

!!! note "A note on MySQL 9.7.3"

```
After a thorough review of the updates included in MySQL 9.7.3, Percona has decided not to release a corresponding Percona Server for MySQL 9.7.3. MySQL 9.7.3 is a Critical Security Patch Update (CSPU) — a targeted security release that Oracle can issue between quarterly Critical Patch Updates (CPUs) when needed. The fixes included in this CSPU do not affect Percona Server for MySQL.
```

This release is based on Percona Server for MySQL 9.7.2-2.

## Percona Server for MySQL 9.7.2-2

Percona Server for MySQL 9.7.2-2 introduces the following new features and improvements:

* Adds OpenID Connect (OIDC) authentication. Users can authenticate through compatible external identity providers. The server validates JSON Web Tokens (JWTs) and audience claims, maps identity-provider groups to MySQL roles, and supports proxy users. The OIDC plugin also includes telemetry and memory instrumentation to improve monitoring and operational visibility. Find more information in [OpenID Connect authentication](https://docs.percona.com/percona-server/9.7/openid-connect-authentication.html){:target="_blank"} and in [Get started with OpenID Connect authentication](https://docs.percona.com/percona-server/9.7/quickstart-openid-connect.html){:target="_blank"}.
* Adds the `DISTANCE()` function, and the `VECTOR_DISTANCE()` alias, for calculating the distance between vector values. Supported metrics are `EUCLIDEAN`, `EUCLIDEAN_SQUARED`, `MANHATTAN`, `COSINE`, and `DOT`. Applications can use these functions to measure vector similarity and support search, recommendation, and other vector-based workloads. See [`DISTANCE()`](https://docs.percona.com/percona-server/9.7/distance-function.html){:target="_blank"}.

## Improvements

* [PXC-5106](https://perconadev.atlassian.net/browse/PXC-5106){:target="_blank"}: Sets `sql_require_primary_key=1` when using `pxc_strict_mode=ENFORCING` or `MASTER`.
* [PXC-5208](https://perconadev.atlassian.net/browse/PXC-5208){:target="_blank"}: Adds the `repl.force_sst_after_inconsistency` option. When enabled, a node voted out of the cluster because of a data inconsistency removes `grastate.dat`, so the next start uses a full State Snapshot Transfer (SST) instead of Incremental State Transfer (IST).

## Bug fixes

* [PXC-5252](https://perconadev.atlassian.net/browse/PXC-5252){:target="_blank"}: Fixed an issue where clone State Snapshot Transfer (SST) failed when the `validate_password` component was enabled with a strict policy, because the generated password for `mysql.pxc.sst.user` did not meet the configured requirements.
* [PXC-5291](https://perconadev.atlassian.net/browse/PXC-5291){:target="_blank"}: Fixed an issue where a user with only the `SET_ANY_DEFINER` privilege could create a trigger when `log_bin_trust_function_creators=0`.

Find the complete list of bug fixes and changes in the [MySQL 9.7.2 release notes](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/news-9-7-2.html){:target="_blank"}.

Learn more in Percona XtraDB Cluster 9.7.2-2 [release notes](https://docs.percona.com/percona-xtradb-cluster/9.7/release-notes/9.7.2-2.html){:target="_blank"}.
