---
date: 2024-01-23
description: >
  Percona Operator for PostgreSQL 2.3.1 has been released on Tuesday, January 23, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 2.3.1 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/2.0/){:target="_blank"} 2.3.1 has been released on Tuesday, January 23, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/2.0/quickstart.html){:target="_blank"}.

This release provides a number of bug fixes, including fixes for the following vulnerabilities in  PostgreSQL, pgBackRest, and pgBouncer images used by the Operator:

* OpenSSH could cause remote code execution by ssh-agent if a user establishes an SSH connection to a compromised or malicious SSH server and has agent forwarding enabled ([CVE-2023-38408](https://nvd.nist.gov/vuln/detail/CVE-2023-38408){:target="_blank"}). This vulnerability affects pgBackRest and PostgreSQL images.
* The c-ares library could cause a Denial of Service with 0-byte UDP payload ([CVE-2023-32067](https://nvd.nist.gov/vuln/detail/CVE-2023-32067){:target="_blank"}). This vulnerability affects pgBouncer image.

Learn more in Percona Operator for PostgreSQL 2.3.1 [release notes](https://docs.percona.com/percona-operator-for-postgresql/2.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN2.3.1.html){:target="_blank"}.


