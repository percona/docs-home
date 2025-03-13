---
date: 2025-03-12
description: >
  Percona Operator for PostgreSQL 2.6.0 has been released on March 12, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.6.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.6.0 has been released on March 12, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* Backup improvements:

    * An improved backup logic now allows retrying a failed backup in the same backup Pod for a specified number of times before deleting this Pod and creating a new one. This is beneficial in case of short connectivity issues or timeouts.   

    * An ability to [overwrite](https://docs.percona.com/percona-operator-for-postgresql/2.0/backups-restore.html#use-custom-restore-command){:target="_blank"} the default restore command for `pgBackRest` allows to control and filter files restored to `pg_wal` directory without editing these files in the backup repository storage.  

    * A new [delete-backups](https://docs.percona.com/percona-operator-for-postgresql/2.0/operator.html#finalizers-delete-backups){:target="_blank"} finalizer allows automatic removal of all backups when deleting the cluster. This is an experimental feature and is not recommended for production use.

* PostgreSQL image used by the operator now includes the `pgvector` built-in extension, which allows using Percona Distribution for PostgreSQL as a vector database and is particularly useful with AI applications.  While it was already possible to [install `pgvector` as a custom extension](https://www.percona.com/blog/create-an-ai-expert-with-open-source-tools-and-pgvector/){:target="_blank"}, now you can just [turn it on](http://docs.percona.com/percona-operator-for-postgresql/2.0/operator.html#extensionsbuiltinpgvector){:target="_blank"} by setting an appropriate Custom Resource option without additional installation steps.

* Changes in supported PostgreSQL versions:

    * PostgreSQL 17 is now supported by the Operator in addition to versions 13 - 16. The appropriate images are now included in the [list of Percona-certified images](https://docs.percona.com/percona-operator-for-postgresql/2.0/images.html){:target="_blank"}. 

    * PostgreSQL 12 is no longer supported by the Operator 2.6.0 and newer versions.

* Known limitations: PostgreSQL 17.2 image and images for other database cluster components based on PostgreSQL 17 contain the known [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/){:target="_blank"} - a vulnerability in the `libpq` PostgreSQL client library, which makes images used by the Operator vulnerable to SQL injection within the PostgreSQL interactive terminal due to the lack of neutralizing quoting. Images for other PosgreSQL versions are already fixed, while images for PostgreSQL 17 will be available soon.

Learn more in Percona Operator for PostgreSQL 2.6.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.6.0.html){:target="_blank"}.


