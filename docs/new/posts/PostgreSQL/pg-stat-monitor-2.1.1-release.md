---
date: 2025-02-27
description: >
  `pg_stat_monitor` 2.1.1 has been released on February 27, 2025.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# `pg_stat_monitor` 2.1.1 has been released 

<!-- more -->

[pg_stat_monitor](https://docs.percona.com/pg-stat-monitor/index.html){:target="_blank"} is the Query Performance Monitoring tool for PostgreSQL. The version 2.1.1 of `pg_stat_monitor` has been released on February 27, 2025.

Try it out using the [installation instructions](https://docs.percona.com/pg-stat-monitor/install.html){:target="_blank"}

This release fixes the deadlock that occurs when the error handler tries to log the error while `pg_stat_monitor` still holds the LWLock. It was fixed by forcefully releasing the lock prior to logging an error.

Learn more about this release in the [release notes](https://docs.percona.com/pg-stat-monitor/release-notes/2.1.1.html){:target="_blank"}. 
