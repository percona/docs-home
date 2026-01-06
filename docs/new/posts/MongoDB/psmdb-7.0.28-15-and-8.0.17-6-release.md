---
date: 2026-01-08
description: >
  Percona Server for MongoDB 7.0.28-15 and 8.0.17-6 have been released on January 8, 2026.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.28-15 and 8.0.17-6 have been released with a fix for CVE-2025-14847: CWE-130

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/8.0/index.html){:target="_blank"} 7.0.28-15 and 8.0.17-6 have been released on January 8, 2026.

These releases provide the fix for the security vulnerability [CVE-2025-14847: CWE-130](https://radar.offseq.com/threat/cve-2025-14847-cwe-130-improper-handling-of-length-dd0a4a45){:target="_blank"}, which affects how MongoDB uses `zlib` compression library. Attackers with network access to `mongod` or `mongos` can extract fragments of uninitialized server memory without authentication if zlib compression is enabled, and access sensitive data. 

We recommend updating to Percona Server for MongoDB 7.0.28-15 or 8.0.17-6 as soon as possible to ensure your deployments remain secure. Find the [update instructions for Percona Server for MongoDB 7.0](https://docs.percona.com/percona-server-for-mongodb/7.0/install/minor-upgrade.html){:target="_blank"} and [Percona Server for MongoDB 8.0](https://docs.percona.com/percona-server-for-mongodb/8.0/install/minor-upgrade.html){:target="_blank"}. 

If an immediate update is not possible, you can disable zlib compression in configuration or startup parameters. 

Learn more about these releases in the release notes of Percona Server for MongoDB [7.0.28-15](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.28-15.html){:target="_blank"} and [8.0.17-6](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.17-6.html){:target="_blank"}.

