---
date: 2025-05-28
description: >
  Percona Distribution for PostgreSQL 17.5.1 has been released on May 28, 2025.
authors: [Andriciuc]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.5.1 has been released

<!-- more -->

[Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.5.1 has been released on May 28, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}

This release of Percona Distribution for PostgreSQL 17.5.1 completes the quarterly minor release cycle for PostgreSQL quarter 2. It provides the following enhancements:

* The `pg_tde` extension for Transparent Data Encryption is now the Release Candidate 2 (RC2). This version of `pg_tde` provides a bunch of improvements, among which is WAL encryption now supporting Vault, automatic WAL internal key generation at server startup, new visibility and verification functions for default principal keys, and more. Learn about these features in the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/rc2.html){:target="_blank"}.

* Improved security and user experience for Docker images. Docker images are now based on Universal Base Image (UBI) version 9, which includes the latest security fixes. Also, Docker image tags are improved so that you only have to specify the database version: Docker automatically identifies the architecture of your operating system and pulls the corresponding image.

* PostGIS is included in tarballs, enabling you to install and run PostgreSQL as a geospatial database on hosts without direct access to the Internet.

* Meta-packages for Percona Distribution for PostgreSQL are deprecated and will be removed in future releases.

Learn more in Percona Distribution for PostgreSQL 17.5.1 [release notes](https://docs.percona.com/postgresql/17/release-notes-v17.5.html){:target="_blank"}.
