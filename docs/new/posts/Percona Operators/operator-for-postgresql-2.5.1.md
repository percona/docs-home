---
date: 2025-03-03
description: >
  Percona Operator for PostgreSQL 2.5.1 has been released on Monday, March 03, 2025.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.5.1 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.5.1 has been released on Monday, March 03, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

This release fixes the [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/){:target="_blank"} vulnerability in the libpq PostgreSQL client library, which made images used by the Operator vulnerable to SQL injection within the PostgreSQL interactive terminal due to the lack of neutralizing quoting.

Learn more in Percona Operator for PostgreSQL 2.5.1 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.5.1.html){:target="_blank"}.
