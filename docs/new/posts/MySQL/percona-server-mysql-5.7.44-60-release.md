---
date: 2026-09-29
description: >
  Percona Server for MySQL 5.7.44-60 has been released on Tuesday, September 29, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 5.7.44-60 has been released

<!-- more -->

[Percona Server for MySQL 5.7.44-60](https://docs.percona.com/percona-server/5.7/){:target="_blank"} has been released on Tuesday, September 29, 2026.

Try it out using the [Installation guide](https://docs.percona.com/percona-server/5.7/installation.html){:target="_blank"}.

This release is part of [Percona's MySQL 5.7 Post-End-of-Life (EOL) support](https://www.percona.com/post-mysql-5-7-eol-support){:target="_blank"} program. This program provides critical updates and ensures the stability for businesses relying on MySQL 5.7 beyond its official EOL. Customers can access the full release, including pre-compiled binaries, through our private repository. Community members will be able to build the release from publicly available source code, which will be released on a quarterly basis.

This release includes bug fixes ported from the 8.0 version.

- Group Replication decode now checks variable-length payload items against the available message buffer and rejects malformed messages.
- Externally received XCom client messages are no longer handled as local Group Replication input. Unsupported `client_msg` cargo is rejected.
- Malformed replication event metadata is validated earlier and rejected before later processing.

Learn more in Percona Server for MySQL 5.7.44-60 [release notes](https://docs.percona.com/percona-server/5.7/release-notes/5.7.44-60.html){:target="_blank"}.