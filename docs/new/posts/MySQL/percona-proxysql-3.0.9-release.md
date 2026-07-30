---
date: 2026-07-29
description: >
  Percona Build of ProxySQL 3.0.9 has been released on Wednesday, July 29, 2026.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - ProxySQL
---

# Percona Build of ProxySQL 3.0.9 has been released

<!-- more -->

[ProxySQL](https://docs.percona.com/proxysql/){:target="_blank"} 3.0.9 has been released on Wednesday, July 29, 2026.

Try it out using the [Installation guide](https://docs.percona.com/proxysql/install-v3.html){:target="_blank"}.

This version updates the Percona Build of ProxySQL to version 3.0.9 and includes updates to the ProxySQL Admin tool and `percona-scheduler-admin`.

## Bug fixes

* Added support for Percona XtraDB Cluster  9.7 in `proxysql-admin` and `percona-scheduler-admin`.

* Added a configurable `AUTH_PLUGIN` setting and replaced the hard-coded `mysql_native_password` value used when creating admin tool users and establishing client connections.

Learn more in ProxySQL 3.0.9 [release notes](https://docs.percona.com/proxysql/3.0.9.html){:target="_blank"}.
