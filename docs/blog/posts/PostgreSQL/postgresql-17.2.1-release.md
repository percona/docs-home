---
date: 2024-12-26
description: >
  Percona Distribution for PostgreSQL 17.2.1 has been released on December 26, 2024.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.2.1 has been released

<!-- more -->

[Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.2.1 has been released on December 26, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}

This release of Percona Distribution for PostgreSQL 17.2.1 completes the quarterly minor release cycle for PostgreSQL this year. It provides the following enhancements:

* A fix for [CVE-2024-10978](https://www.postgresql.org/support/security/CVE-2024-10978/) and for certain PostgreSQL extensions that break because they depend on the modified Application Binary Interface (ABI). These regressions were introduced in PostgreSQL 17.1. For this reason, the release of Percona Distribution for PostgreSQL 17.1 was skipped.

* The `pg_tde` extension is now a part of the Percona Server for PostgreSQL server package and a Docker image. Therefore, if you installed the extension before, from its individual package, uninstall it first to avoid conflicts during the upgrade. See the [Minor Upgrade of Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/minor-upgrade.html#preconditions){:target="_blank"} for details. 

* Use PostgreSQL as a vector database with [`pgvector` :octicons-link-external-16:](https://github.com/pgvector/pgvector){:target="_blank"} added to Percona Distribution for PostgreSQL. `pgvector` is an open-source extension that enriches PostgreSQL with vector similarity search. Interested but still not sure? [Talk to us](https://www.percona.com/contact-us/){:target="_blank"} to find the best solution for you.

* Forget about LLVM conflicts if you run Red Hat Enterprise Linux 8 and 9 or compatible derivatives. Use the software of your choice with the LLVM modules supplied with the operating system and Percona Distribution for PostgreSQL on the same host. Starting with this release, Percona Distribution for PostgreSQL statically links `llvmjit.so` library it requires. 

Learn more in Percona Distribution for PostgreSQL 17.2.1 [release notes](https://docs.percona.com/postgresql/17/release-notes-v17.2.html){:target="_blank"}.

