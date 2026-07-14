---
date: 2026-07-21
description: >
  Percona Server for MySQL 8.0.46-38 has been released on Tuesday, July 21, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.46-38 has been released

<!-- more -->

[Percona Server for MySQL 8.0.46-38](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Tuesday, July 21, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

This release is part of Percona’s [MySQL 8.0 Post-EOL Support](https://www.percona.com/mysql-8-0-eol-support/){:target="_blank"} program. The program provides critical updates and ensures stability for businesses relying on MySQL 8.0 beyond the official EOL.

Paying customers can access the full release, including pre-compiled binaries, through the private repository. Community members can build the release from publicly available source code, which is released quarterly.

Upgrading to MySQL 8.4 is recommended, but support for MySQL 8.0 will continue.

Percona Server for MySQL 8.0.46-38 builds on MySQL 8.0.46 Community Edition, adding enterprise-grade features and security enhancements from Percona.

The following lists some improvements and bug fixes:

* During connection setup, connection attribute parsing could read a length-encoded size field before verifying that the complete field was present in the packet, leading to an out-of-bounds read. A size check is now performed before reading the field.

* An unauthenticated repeated X Protocol TLS upgrade causes an unplanned exit of the MySQL Router.

Learn more in Percona Server for MySQL 8.0.46-38 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.46-38.html){:target="_blank"}.
