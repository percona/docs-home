---
date: 2026-09-08
description: >
  `pg_stat_monitor` 2.4 has been released on September 08, 2026.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# `pg_stat_monitor` 2.4 has been released

<!-- more -->

[pg_stat_monitor :octicons-link-external-16:](https://docs.percona.com/pg-stat-monitor/index.html){:target="_blank"} is the Query Performance Monitoring tool for PostgreSQL. Version 2.4 of `pg_stat_monitor` has been released on September 08, 2026.

Try it out using the [installation instructions :octicons-link-external-16:](https://docs.percona.com/pg-stat-monitor/install.html){:target="_blank"}.

This release is focused on the stability and reliability of `pg_stat_monitor`. Large parts of the internals were reworked to remove long-standing sources of crashes, memory leaks and incorrect statistics, and the test suite was extended with test cases backported from `pg_stat_statements` so that the behavior of both extensions can be compared directly.

The release also adds support for PostgreSQL 19 beta 3, drops PostgreSQL 13 support, removes the deprecated `pg_stat_monitor.pgsm_overflow_target` parameter and deprecates the `pg_stat_monitor.pgsm_track_application_names` parameter.

Learn more about this release in the [release notes :octicons-link-external-16:](https://docs.percona.com/pg-stat-monitor/release-notes/2.4.0.html){:target="_blank"}.
