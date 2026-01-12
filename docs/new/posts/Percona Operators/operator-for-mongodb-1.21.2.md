---
date: 2026-01-12
description: >
  Percona Operator for MongoDB 1.21.2 has been released on January 12, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.21.2 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.21.2 has been released on January 12, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

This release is the security update to address the security vulnerability [CVE-2025-14847: CWE-130](https://radar.offseq.com/threat/cve-2025-14847-cwe-130-improper-handling-of-length-dd0a4a45){:target="_blank"} in Percona Server for MongoDB about the use of `zlib` compression library. Attackers with network access to `mongod` or `mongos` can extract fragments of uninitialized server memory without authentication if `zlib` compression is enabled, and access sensitive data. 

Percona Operator for MongoDB 1.21.2 includes the most recent versions of Percona Server for MongoDB with the fix. We recommend [updating to Percona Operator for MongoDB 1.21.2](https://docs.percona.com/percona-operator-for-mongodb/update-operator.html){:target="_blank"} as soon as possible to ensure your deployments remain secure. 

If an immediate update is not possible, you can disable `zlib` compression in Percona Server for MongoDB configuration or startup parameters. 

Learn more about the security issue and remediation steps in Percona Blog: [Urgent Security Update: Patching “Mongobleed” (CVE-2025-14847) in Percona Server for MongoDB](https://www.percona.com/blog/urgent-security-update-patching-mongobleed-cve-2025-14847-in-percona-server-for-mongodb/){:target="_blank"}.

Learn more about this release in Percona Operator for MongoDB 1.21.2 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.21.2.html){:target="_blank"}.
