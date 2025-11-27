---
date: 2025-11-27
description: >
  Percona Server for MySQL 5.7.44-56 has been released on Thursday, November 27, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 5.7.44-56 has been released

<!-- more -->


[Percona Server for MySQL 5.7.44-56](https://docs.percona.com/percona-server/5.7/){:target="_blank"} has been released on Thursday, November 27, 2025.

Try it out using the [Installation guide](https://docs.percona.com/percona-server/5.7/installation.html){:target="_blank"}.

This release is part of [Percona’s MySQL 5.7 Post-End-of-Life (EOL) support](https://www.percona.com/post-mysql-5-7-eol-support){:target="_blank"} program. This program provides critical updates and ensures the stability for businesses relying on MySQL 5.7 beyond its official EOL. Paying customers can access the full release, including pre-compiled binaries, through our private repository. Community members will be able to build the release from publicly available source code, which will be released on a quarterly basis.

This release includes bug fixes ported from the 8.0 version.

* A fix was implemented to prevent memory access errors when parsing optimizer hints near buffer boundaries. The server now automatically checks buffer boundaries before accessing the next character.

Learn more in Percona Server for MySQL 5.7.44-56 [release notes](https://docs.percona.com/percona-server/5.7/release-notes/5.7.44-56.html){:target="_blank"}.