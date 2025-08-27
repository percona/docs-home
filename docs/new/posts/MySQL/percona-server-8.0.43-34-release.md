---
date: 2025-08-28
description: >
  Percona Server for MySQL 8.0.43-34 has been released on Thursday, August 28, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.43-34 has been released

<!-- more -->

[Percona Server for MySQL 8.0.43-34](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Thursday, August 28, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

### Percona Server for MySQL 8.0.43-34

Implements Link-Time Optimization (LTO) to generate more optimized release binaries, resulting in improved performance for specific workloads.

### MySQL 8.0.43

Bug fixes provided by Oracle for MySQL 8.0.43 and included in Percona Server for MySQL are the following:

* Fixed an issue where rebuilding a primary key with duplicate entries could cause the server to stop unexpectedly. (Bug #37822992)

* Fixed an issue related to dropping columns that were part of an index. (Bug #37726881)

* Fixed an issue with indexing spatial datatype columns. (Bug #36682518)

* Fixed an issue where creating a secondary index on a `VARCHAR` column could exceed configured memory limits, with the amount allocated being directly related to the `value of innodb_ddl_buffer_size`, leading to errors such as ERROR 1136 (21S01): Column count doesn't match value count at row 1. (Bug #37233273)

Learn more in Percona Server for MySQL 8.0.43-34 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.43-34.html){:target="_blank"}.
