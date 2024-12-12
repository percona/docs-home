---
date: 2024-12-12
description: >
  Percona Distribution for PostgreSQL 16.6, 15.10, 14.15, 13.18 and 12.22 have been released.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 16.6, 15.10, 14.15, 13.18 and 12.22 have been released

<!-- more -->

The next minor versions of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/16/index.html){:target="_blank"} 16.6, 15.10, 14.15, 13.18 and 12.22 have been released throughout December 2024.

Try out Percona Distribution for PostgreSQL using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. 

These releases are part of the quarter 4 release cycle and feature the following improvements:

* A fix for [CVE-2024-10978](https://www.postgresql.org/support/security/CVE-2024-10978/) and for certain PostgreSQL extensions that break because they depend on the modified Application Binary Interface (ABI). These regressions were introduced in PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21. For this reason, the releases of Percona Distribution for PostgreSQL for the above mentioned versions were skipped. 

* [`pgvector` :octicons-link-external-16:](https://github.com/pgvector/pgvector) is now part of Percona Distribution for PostgreSQL. It is an open-source extension that enables you to use PostgreSQL as a vector database. It is available as a package, a Docker image and is included in tarballs. 

* Percona Distribution for PostgreSQL now statically links `llvmjit.so` library for Red Hat Enterprise Linux 8 and 9 and compatible derivatives. This resolves the conflict between the LLVM version required by Percona Distribution for PostgreSQL and the one supplied with the operating system. This also enables you to use the LLVM modules supplied with the operating system for other software you require.

Percona Distribution for PostgreSQL 12.22 is the last release of 12.x series as this major version has reached end-of-life. Learn more about its implications and what options you have to upgrade in the blog post [PostgreSQL 12 End of Life: Upgrade Now with Percona](https://www.percona.com/blog/postgresql-12-end-of-life-upgrade-now-with-percona/){:target="_blank"} by Kai Wagner.

Learn more in Percona Distribution for PostgreSQL release notes for [16.6](https://docs.percona.com/postgresql/16/release-notes-v16.6.html){:target="_blank"}, [15.10](https://docs.percona.com/postgresql/15/release-notes-v15.10.html){:target="_blank"}, [14.15](https://docs.percona.com/postgresql/14/release-notes-v14.15.html){:target="_blank"}, [13.18](https://docs.percona.com/postgresql/13/release-notes-v13.18.html){:target="_blank"} and [12.22](https://docs.percona.com/postgresql/12/release-notes-v12.22.html){:target="_blank"}.

