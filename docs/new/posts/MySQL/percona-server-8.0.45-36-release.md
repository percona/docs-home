---
date: 2026-02-17
description: >
  Percona Server for MySQL 8.0.45-36 has been released on Tuesday, February 17, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.45-36 has been released

<!-- more -->

[Percona Server for MySQL 8.0.45-36](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Tuesday, February 17, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

Percona Server for MySQL 8.0.45-36 includes all the features and bug fixes available in MySQL 8.0.45 Community Edition, as well as enterprise-grade features developed by Percona.

Percona has consolidated its build offerings. The Pro builds are no longer required, and all features have been merged into the main open source Community release.

The following lists some of the bug fixes:

* The Audit Log Filter could crash when `audit_log_filter.file` pointed to a non-existent directory.

* MySQL 8.0.40 and later could be about two or three times slower than 8.0.39 in a particular index scan scenario.

* Expanded Fast Index Creation could fail with partitioned tables.

* A table definition mismatch between MyRocks and the data dictionary after a crash could cause a crash or assertion failures.

* The Audit Log Filter could crash when the definition passed to `audit_log_filter_set_filter()` contained invalid data replacement fields.

Learn more in Percona Server for MySQL 8.0.45-36 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.45-36.html){:target="_blank"}.
