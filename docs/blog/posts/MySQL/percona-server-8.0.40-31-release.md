---
date: 2024-12-30
description: >
  Percona Server for MySQL 8.0.40-31 has been released on Monday, December 30, 2024.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.40-31 has been released

<!-- more -->

[Percona Server for MySQL 8.0.40-31](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Monday, December 30, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

Percona Server for MySQL 8.0.40-31 includes all the features and bug fixes available in the MySQL 8.0.40 Community Edition in addition to enterprise-grade features developed by Percona. 

* The Audit plugin caused a memory leak. This occurred when threads remained connected to the database for extended periods.

* After an upgrade, the telemetry daemon ran continuously. The telemetry daemon was manually stopped and the service was disabled. Adding `percona_telemetry_disable=1` to the configuration file and restarting MySQL led to the server becoming unresponsive and required a forced termination.

Learn more in Percona Server for MySQL 8.0.40-31 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.40-31.html){:target="_blank"}.
