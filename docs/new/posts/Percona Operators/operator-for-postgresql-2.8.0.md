---
date: 2025-11-13
description: >
  Percona Operator for PostgreSQL 2.8.0 has been released on November 13, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.8.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.8.0 has been released on November 13, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* Simplified [management of user passwords](https://docs.percona.com/percona-operator-for-postgresql/2.0/users.html#managing-user-passwords){:target="_blank"}. You no longer need to include full connection details in Secrets. Just provide the password, and the Operator automatically fills in the rest from your Custom Resource configuration. You also have the flexibility in naming the Secret: using the `<clusterName>-pguser-<userName>` format lets the Operator detect and use the Secret without requiring an explicit reference in the Custom Resource.

* Achieve more efficient memory use and improved performance with [huge pages support for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/huge-pages.html){:target="_blank"}. Huge pages help your workloads run faster and scale more reliably by reducing CPU overhead and optimizing memory. To benefit, make sure huge pages are enabled in your Kubernetes environment and configured for your PostgreSQL deployment.

* Expanded flexibility with custom S3 storage support. You can now configure the Operator to connect to your own S3‑compatible storage by enabling path‑style access or bypassing TLS verification. This unlocks you from using AWS S3 to store custom extensions and ensures the Operator can download and install them seamlessly for your PostgreSQL deployment.

* Streamlined Patroni version management in PostgreSQL clusters. The Operator standardizes on Patroni 4 as the only supported version and no longer honors Patroni version overrides via the `pgv2.percona.com/custom-patroni-version` annotation. Version detection happens automatically through `patronictl`, and results are recorded in cluster annotations and status. For backward compatibility, Custom Resources at 2.7.0 can still use Patroni 3 via the annotation, but once upgraded to 2.8.0, Patroni 4 is always applied.

* Official Docker image for PostgreSQL images. The Operator now uses the official Percona Docker images for Percona Distribution for PostgreSQL, with the image path `percona/percona-distribution-postgresql:<postgresql-version>`. 

  Because of this transition, the Operator is compatible with and supports only the following specific PostgreSQL versions:

  * Percona Distribution for PostgreSQL 17.5.2, 17.6.2
  * Percona Distribution for PostgreSQL 16.10
  * Percona Distribution for PostgreSQL 15.14
  * Percona Distribution for PostgreSQL 14.19
  * Percona Distribution for PostgreSQL 13.22

Learn more in Percona Operator for PostgreSQL 2.8.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.8.0.html){:target="_blank"}.


