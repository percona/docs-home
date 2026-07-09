---
date: 2026-07-09
description: >
  Percona Server for MySQL 5.7.44-59 has been released on Thursday, July 9, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 5.7.44-59 has been released

<!-- more -->


[Percona Server for MySQL 5.7.44-59](https://docs.percona.com/percona-server/5.7/){:target="_blank"} has been released on Thursday, July 9, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-server/5.7/installation.html){:target="_blank"}.

This release is part of [Percona's MySQL 5.7 Post-End-of-Life (EOL) support](https://www.percona.com/post-mysql-5-7-eol-support){:target="_blank"} program. This program provides critical updates and ensures the stability for businesses relying on MySQL 5.7 beyond its official EOL. Customers can access the full release, including pre-compiled binaries, through our private repository. Community members will be able to build the release from publicly available source code, which will be released on a quarterly basis.

This release includes bug fixes ported from the 8.0 version.

* During connection setup, connection attribute parsing could read a length-encoded size field before verifying that the complete field was present in the packet, leading to an out-of-bounds read. A size check is now performed before reading the field.

Learn more in Percona Server for MySQL 5.7.44-59 [release notes](https://docs.percona.com/percona-server/5.7/release-notes/5.7.44-59.html){:target="_blank"}.
