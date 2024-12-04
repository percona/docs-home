---
date: 2024-10-03
description: >
  Percona Distribution for PostgreSQL 17.0.1 has been released on Thursday, October 3, 2024.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.0.1 has been released

<!-- more -->

[Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.0.1 has been released on October 3, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}

This is the next major version of PostgreSQL, and instead of the native PostgreSQL server it is now based on Percona Server for PostgreSQL which is a binary drop-in replacement for PostgreSQL. [Read more about Percona Server for PostgreSQL](https://docs.percona.com/postgresql/17/postgresql-server.html){:target="_blank"}

In addition, this release includes the following improvements:

* Incremental base backup with the new `pg_combinebackup` tool. This feature is especially beneficial for organizations with large data sets where a full backup is a time-consuming and resource-intensive operation.
* Improved performance via the new internal data structure of the VACUUM process, new stream I/O interface can enhance performance during sequential scans and when running the ANALYZE command and the support for parallel index builds for BRIN indexes, which can significantly speed up index creation
* Developers can now transform JSON objects into a standard database table and convert JSON values to different data types directly within SQL statements. This adds flexibility when working with multiple data formats.
* Gain more control for managing PostgreSQL databases in high availability environments with the ability to continue logical replication from a new primary node after the failover.
* Convert a physical replica into a logical one using the new pg_createsubscriber command-line tool
* Users with the new pg_maintain role can perform maintenance operations such as ANALYZE, VACUUM, REINDEX, CLUSTER, REFRESH MATERIALIZED VIEW, and LOCK TABLE on all relations.
* New options for the EXPLAIN command provide more insights about query plans and execution

Learn more in Percona Distribution for PostgreSQL 17.0.1 [release notes](https://docs.percona.com/postgresql/17/release-notes-v17.0.html){:target="_blank"}.

<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>