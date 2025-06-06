---
date: 2024-10-08
description: >
  Percona Operator for PostgreSQL 2.5.0 has been released on Tuesday, October 08, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.5.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.5.0 has been released on Tuesday, October 08, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Automated storage scaling](https://docs.percona.com/percona-operator-for-postgresql/2.0/scaling.html#scale-storage){:target="_blank"} allows the Operator to detect if the storage usage on the PVC reaches a certain threshold, and trigger the PVC resize
* [Major versions upgrade improvements](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.5.0.html#major-versions-upgrade-improvements){:target="_blank"} make it is possible to upgrade from one PostgreSQL major version to another with custom images for the database cluster components (PostgreSQL, pgBouncer, and pgBackRest)
* [Azure Kubernetes Service](https://docs.percona.com/percona-operator-for-postgresql/2.0/aks.html){:target="_blank"} is now officially supported platform, and also [Azure Blob Storage can now be used for backups](https://docs.percona.com/percona-operator-for-postgresql/2.0/backups-storage.html#__tabbed_1_3){:target="_blank"}

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.5.0.html#deprecation-change-rename-and-removal){:target="_blank"} are the following ones:

* With the Operator versions prior to 2.5.0, [autogenerated TLS certificates](https://docs.percona.com/percona-operator-for-postgresql/2.0/TLS.html#allow-the-operator-to-generate-certificates-automatically){:target="_blank"} for all database clusters were based on the same generated root CA. Starting from 2.5.0, the Operator creates root CA on a per-cluster basis.

Learn more in Percona Operator for PostgreSQL 2.5.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.5.0.html){:target="_blank"}.


