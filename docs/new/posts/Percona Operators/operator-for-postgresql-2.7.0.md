---
date: 2025-07-18
description: >
  Percona Operator for PostgreSQL 2.7.0 has been released on July 18, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.7.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.7.0 has been released on July 18, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* PMM improvements:

   * With added PMM3 support, you can now monitor the health and performance of your Percona Distribution for PostgreSQL deployment and at the same time enjoy enhanced performance, new features, and improved security that PMM 3 provides. Note that PMM2 support remains in the Operator. The decision what PMM version to use is done based on the configured authentication method. Read more about PMM 3 configuration in the [documentation](https://docs.percona.com/percona-operator-for-postgresql/2.0/monitoring.html){:target="_blank"}.
   * Improved monitoring for clusters in multi-region or multi-namespace deployments with the ability to define a custom name for a database cluster in PMM. This helps PMM to correctly recognize how a cluster is deployed (in different data centers vs deployed with the same name in different namespaces) and correctly display metrics.

* You can explicitly grant access to a `public` schema for a non-superuser setting the `grantPublicSchemaAccess` option to `true`. This grants the user permission to create tables and update in the `public` schema of every database they own. If multiple users are granted access to the `public` schema in the same database, each user can only access the tables they have created themselves. Read more about creating and managing users in the [documentation](https://docs.percona.com/percona-operator-for-postgresql/2.0/users.html){:target="_blank"}.

* Improved troubleshooting with the ability to override Patroni configuration for the whole cluster and/or for individual Pods. You can also redefine what method the Operator will use to create replica instances in your PostgreSQL cluster. Note that you must manually reload Patroni configuration on every database instance to apply the changes. Find exact steps and additional information in the [documentation](https://docs.percona.com/percona-operator-for-postgresql/2.0/manage-manually.html){:target="_blank"}.

* Identify the current Operator version associated with Custom Resources via labels. This helps you decide if you need to upgrade it or not.

Learn more in Percona Operator for PostgreSQL 2.7.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.7.0.html){:target="_blank"}.


