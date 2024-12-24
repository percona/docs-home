---
date: 2024-09-10
description: >
  `pg_stat_monitor` 2.1.0 has been released on September 10, 2024.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
  - TDE
---

# `pg_stat_monitor` 2.1.0 has been released 

[pg_stat_monitor](https://docs.percona.com/pg-stat-monitor/index.html){:target="_blank"} is the Query Performance Monitoring tool for PostgreSQL. The version 2.1.0 of `pg_stat_monitor` has been released on September 10, 2024.

Try it out using the [installation instructions](https://docs.percona.com/pg-stat-monitor/install.html){:target="_blank"}

<!-- more -->

This release provides the following enhancements:

* Optimized query execution performance with the ability to [disable the application name tracking for a query](https://docs.percona.com/pg-stat-monitor/configuration.html#pg_stat_monitorpgsm_track_application_names){:target="_blank"}.  
* Compatibility with PostgreSQL 17.
* Improved display of queries with different parent queries in the statistics table. 
* The support of PostgreSQL 11 is deprecated. Existing functionality in `pg_stat_monitor` remains compatible with PostgreSQL 11; however, further enhancements and bug fixes are no longer tested against this version.

Learn more about this release in the [release notes](https://docs.percona.com/pg-stat-monitor/release-notes/2.1.0.html){:target="_blank"}. 
