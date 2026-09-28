---
date: 2026-09-28
description: >
  Percona Server for MySQL 9.7.2-2 has been released on Monday, September 28, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 9.7.2-2 has been released

<!-- more -->

[Percona Server for MySQL 9.7.2-2](https://docs.percona.com/percona-server/9.7/index.html){:target="_blank"} has been released on Monday, September 28, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/9.7/quickstart-overview.html){:target="_blank"}.

Percona Server for MySQL 9.7.2-2 includes enhancements and bug fixes from MySQL 9.7.2.

Percona Server for MySQL 9.7.3 will not be released. After a review of MySQL 9.7.3, a Critical Security Patch Update (CSPU) that Oracle can issue between quarterly Critical Patch Updates, Percona determined that the fixes do not affect Percona Server for MySQL.

## Percona Server for MySQL 9.7.2-2

Percona Server for MySQL 9.7.2-2 introduces the following new features and improvements:

* Adds OpenID Connect (OIDC) authentication. Users can authenticate through compatible external identity providers. The server validates JSON Web Tokens (JWTs) and audience claims, maps identity-provider groups to MySQL roles, and supports proxy users. The OIDC plugin also includes telemetry and memory instrumentation to improve monitoring and operational visibility. Find more information in [OpenID Connect authentication](https://docs.percona.com/percona-server/9.7/openid-connect-authentication.html){:target="_blank"} and in [Get started with OpenID Connect authentication](https://docs.percona.com/percona-server/9.7/quickstart-openid-connect.html){:target="_blank"}.

* Adds the `DISTANCE()` function, and the `VECTOR_DISTANCE()` alias, for calculating the distance between vector values. Supported metrics are `EUCLIDEAN`, `EUCLIDEAN_SQUARED`, `MANHATTAN`, `COSINE`, and `DOT`. Applications can use these functions to measure vector similarity and support search, recommendation, and other vector-based workloads.


Find the complete list of bug fixes and changes in the [MySQL 9.7.2 release notes :octicons-link-external-16:](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/news-9-7-2.html){:target="_blank"}.

Learn more in Percona Server for MySQL 9.7.2-2 [release notes](https://docs.percona.com/percona-server/9.7/release-notes/9.7.2-2.html){:target="_blank"}.
