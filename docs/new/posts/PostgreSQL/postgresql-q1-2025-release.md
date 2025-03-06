---
date: 2025-03-06
description: >
  Percona Distribution for PostgreSQL 16.8, 15.12, 14.17 and 13.20 have been released.
authors: [nastena1606]
categories:
  - PostgreSQL
tags:
  - Percona Distribution for PostgreSQL
---

# Percona Distribution for PostgreSQL 16.8, 15.12, 14.17 and 13.20 have been released

<!-- more -->

The minor releases of [Percona Distribution for PostgreSQL](https://docs.percona.com/postgresql/16/index.html){:target="_blank"} 16.8, 15.12, 14.17 and 13.20 have been released end of February - March 2025.

Try out Percona Distribution for PostgreSQL using the [Quickstart guide](https://docs.percona.com/postgresql/16/installing.html){:target="_blank"}. 

These are out-of-cycle releases due to the regression related to string handling for non-null terminated strings. This regression affects versions 17.3, 16.7, 15.11, 14.16, and 13.19, therefore, they were skipped.

These releases provide the following enhancements:

* Improved security and user experience for Docker images. Docker images are now based on Universal Base Image (UBI) version 9, which includes the latest security fixes. Also, Docker image tags are improve so that you only have to specify the database version: Docker automatically identifies the architecture of your operating system and pulls the corresponding image. 

* PostGIS is included in tarballs, enabling you to install and run PostgreSQL as a geospatial database on hosts without a direct access to the Internet.

* Meta-packages for Percona Distribution for PostgreSQL are deprecated and will be removed in future releases.

Learn more in Percona Distribution for PostgreSQL release notes for [16.8](https://docs.percona.com/postgresql/16/release-notes-v16.8.html){:target="_blank"}, [15.12](https://docs.percona.com/postgresql/15/release-notes-v15.12.html){:target="_blank"}, [14.17](https://docs.percona.com/postgresql/14/release-notes-v14.17.html){:target="_blank"} and [13.20](https://docs.percona.com/postgresql/13/release-notes-v13.20.html){:target="_blank"}.

