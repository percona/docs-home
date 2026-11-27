---
date: 2026-11-30
description: >
  Percona Server for MySQL 8.4.13-13 has been released on Monday, November 30, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.13-13 has been released

<!-- more -->

[Percona Server for MySQL 8.4.13-13](https://docs.percona.com/percona-server/8.4/index.html){:target="_blank"} has been released on Monday, November 30, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html){:target="_blank"}.

## Percona Server for MySQL 8.4.13-13

Percona Server for MySQL 8.4.13-13 introduces the following new features and improvements:

- Stale Adaptive Hash Index data: point lookups could return outdated rows after a table's tablespace was discarded and replaced with an older imported image. Stale entries are now treated as cache misses.

- Failed tablespace import cleanup: a failed `ALTER TABLE ... IMPORT TABLESPACE` could trigger an assertion during page eviction. Cleanup now preserves the index space ID so leftover entries can be purged.

- Page reorganization mismatches: size discrepancies that were previously ignored without redo logging are now treated as fatal errors, to prevent corruption or recovery failures.

- Self-referencing foreign keys: fixed problems when renaming columns bound by self-referencing foreign keys.

## New features and improvements

- **OIDC proxied users for long group names and IDs ([PS-11419](https://perconadev.atlassian.net/browse/PS-11419)):** The OpenID Connect authentication plugin now supports proxied users when group names or IDs are long. This release also adds an installation script for the plugin ([PS-11568](https://perconadev.atlassian.net/browse/PS-11568)).

- **Regular expressions in Audit Log Component filters ([PS-11118](https://perconadev.atlassian.net/browse/PS-11118)):** Audit log filters can now match with regular expressions, so you can write fewer, broader rules.

## Bug fixes

- **Missing privilege checks on audit log UDFs ([PS-11926](https://perconadev.atlassian.net/browse/PS-11926)):** Four audit log user-defined functions were missing `AUDIT_ADMIN` privilege checks. They are now enforced.

## MySQL 8.4.13 fixes included

- Point lookups could return outdated rows through the Adaptive Hash Index after a tablespace was discarded and replaced with an older imported image. Stale entries are now treated as cache misses.

- A failed `ALTER TABLE ... IMPORT TABLESPACE` could trigger an assertion during page eviction.

- Page reorganization size mismatches are now treated as fatal errors to prevent corruption or recovery failures.

- Renaming columns bound by self-referencing foreign keys is fixed.

Find the complete list of bug fixes and changes in the [MySQL 8.4.13 release notes :octicons-link-external-16:](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-13.html){:target="_blank"}.

Learn more in Percona Server for MySQL 8.4.13-13 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.13-13.html){:target="_blank"}.
