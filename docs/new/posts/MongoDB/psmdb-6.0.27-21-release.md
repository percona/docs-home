---
date: 2026-01-12
description: >
  Percona Server for MongoDB 6.0.27-21 has been released on January 12, 2026.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 6.0.27-21 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/6.0/index.html){:target="_blank"} 6.0.27-21 has been released on January 12, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/6.0/install/index.html){:target="_blank"}. 

This release is the security update to address the security vulnerability [CVE-2025-14847: CWE-130](https://radar.offseq.com/threat/cve-2025-14847-cwe-130-improper-handling-of-length-dd0a4a45){:target="_blank"} in how MongoDB uses `zlib` compression library. Attackers with network access to `mongod` or `mongos` can extract fragments of uninitialized server memory without authentication if zlib compression is enabled, and access sensitive data. 

We recommend [updating to Percona Server for MongoDB 6.0.27-21](https://docs.percona.com/percona-server-for-mongodb/6.0/install/minor-upgrade.html){:target="_blank"} as soon as possible to ensure your deployments remain secure. 

If an immediate update is not possible, you can disable `zlib` compression in configuration or startup parameters. 

Learn more about the security issue and remediation steps in Percona Blog: [Urgent Security Update: Patching “Mongobleed” (CVE-2025-14847) in Percona Server for MongoDB](https://www.percona.com/blog/urgent-security-update-patching-mongobleed-cve-2025-14847-in-percona-server-for-mongodb/){:target="_blank"}.

Learn more about this release in Percona Server for MongoDB 6.0.27-21 [release notes](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.27-21.html){:target="_blank"}.

