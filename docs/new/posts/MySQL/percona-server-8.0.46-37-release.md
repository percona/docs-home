---
date: 2026-06-10
description: >
  Percona Server for MySQL 8.0.46-37 has been released on Wednesday, June 10, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.46-37 has been released

<!-- more -->

[Percona Server for MySQL 8.0.46-37](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Wednesday, June 10, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

Percona Server for MySQL 8.0.46-37 is the final release of the Percona Server for MySQL 8.0 series. MySQL 8.0 has reached its End of Life (EOL).

Percona offers tailored support before, during, and after your move to MySQL 8.4, and can keep your existing MySQL 8.0 deployment secure and performant post-EOL through [MySQL 8.0 Post-EOL Support from Percona](https://www.percona.com/mysql-8-0-eol-support/){:target="_blank"}.

Percona Server for MySQL 8.0.46-37 includes all the features and bug fixes available in MySQL 8.0.46 Community Edition, as well as enterprise-grade features developed by Percona.

The following lists some improvements and bug fixes:

* The audit log buffer is now flushed on server shutdown when the `ASYNCHRONOUS` logging strategy is in use, preventing the loss of buffered events.

* A prepared `INSERT` statement failed to write rows across partitions.

* MyRocks could overflow a buffer when `rocksdb_merge_buf_size` was set above 4 GB.

Learn more in Percona Server for MySQL 8.0.46-37 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.46-37.html){:target="_blank"}.
