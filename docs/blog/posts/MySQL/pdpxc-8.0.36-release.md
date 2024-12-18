---
date: 2024-04-03
description: >
  Percona Distribution for MySQL 8.0.36 using Percona XtraDB Cluster has been released on Wednesday, April 03, 2024.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Distribution for MySQL using Percona XtraDB Cluster
---

# Percona Distribution for MySQL 8.0.36 using Percona XtraDB Cluster has been released

<!-- more -->

[Percona Distribution for MySQL 8.0.36 using Percona XtraDB Cluster](https://docs.percona.com/percona-distribution-for-mysql/8.0/index.html){.md-button} has been released on Wednesday, April 03, 2024.

Try it out using the [Installation guide](https://docs.percona.com/percona-distribution-for-mysql/8.0/installing.html){.md-button}.

Improvements and bug fixes provided by Oracle for MySQL 8.0.36 and included in Percona XtraDB Cluster are the following:

* The hashing algorithm employed yielded poor performance when using a HASH field to check for uniqueness. (Bug #109548, Bug #34959356)

* All [statement instrument elements](https://dev.mysql.com/doc/refman//8.0/en/performance-schema-instrument-naming.html#performance-schema-statement-instrument-elements){.md-button} that begin with `statement/sp/%`, except `statement/sp/stmt`, are disabled by default.

Learn more in Percona Distribution for MySQL 8.0.36 using Percona XtraDB Cluster [release notes](https://docs.percona.com/percona-distribution-for-mysql/8.0/release-notes-pxc-v8.0.36.html){:target="_blank"}.

