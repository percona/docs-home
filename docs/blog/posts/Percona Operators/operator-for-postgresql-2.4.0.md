---
date: 2024-06-26
description: >
  Percona Operator for PostgreSQL 2.4.0 has been released on Wednesday, June 26, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.4.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.4.0 has been released on Wednesday, June 26, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Major versions upgrade (tech preview)](https://docs.percona.com/percona-operator-for-postgresql/2.0/update.html#major-version-upgrade){:target="_blank"} automates upgrades from one PostgreSQL major version to another
* [Supporting PostgreSQL tablespaces](https://docs.percona.com/percona-operator-for-postgresql/2.0/tablespaces.html){:target="_blank"} make it is possible to upgrade from one PostgreSQL major version to another with custom images for the database cluster components (PostgreSQL, pgBouncer, and pgBackRest)
* [Using cloud roles to authenticate on the object storage for backups](https://docs.percona.com/percona-operator-for-postgresql/2.0/backups-storage.html#__tabbed_3_1){:target="_blank"} is now possible, significantly improving security by eliminating the need to manage S3 access keys directly

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.4.0.html#deprecation-and-removal){:target="_blank"} are the following ones:

* The `plpythonu` extension was removed from the list of built-in PostgreSQL extensions; users who still need it can enable it for their databases via [custom extensions functionality](https://docs.percona.com/percona-operator-for-postgresql/2.0/custom-extensions.html){:target="_blank"}

Learn more in Percona Operator for PostgreSQL 2.4.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.4.0.html){:target="_blank"}.


