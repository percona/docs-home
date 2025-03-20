---
date: 2025-03-27
description: >
  Percona Distribution for PostgreSQL 17.4.1 has been released on March 27, 2025.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 17.4.1 has been released

<!-- more -->

[Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/17/index.html){:target="_blank"} 17.4.1 has been released on March 27, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/postgresql/17/installing.html){:target="_blank"}. Check the [upgrade instructions](https://docs.percona.com/postgresql/17/major-upgrade.html){:target="_blank"}

This release of Percona Distribution for PostgreSQL 17.4.1 completes the quarterly minor release cycle for PostgreSQL quarter 1. It provides the following enhancements:

* The `pg_tde` extension for Transparent Data Encryption is now the Release Candidate. This version of `pg_tde` provides a bunch of improvements, among which is the redesigned WAL encryption, simplified configuration for single-tenant environments, the ability to change key provider configuration offline, and more. Learn about these features in the [`pg_tde` release notes](https://docs.percona.com/pg-tde/release-notes/rc.html){:target="_blank"}.

* Improved security and user experience for Docker images. Docker images are now based on Universal Base Image (UBI) version 9, which includes the latest security fixes. Also, Docker image tags are improved so that you only have to specify the database version: Docker automatically identifies the architecture of your operating system and pulls the corresponding image. 

* PostGIS is included in tarballs, enabling you to install and run PostgreSQL as a geospatial database on hosts without direct access to the Internet.

* Meta-packages for Percona Distribution for PostgreSQL are deprecated and will be removed in future releases.

Learn more in Percona Distribution for PostgreSQL 17.4.1 [release notes](https://docs.percona.com/postgresql/17/release-notes-v17.4.html){:target="_blank"}.

