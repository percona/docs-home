---
date: 2024-11-27
description: >
  Percona Server for MongoDB 7.0.15-9 has been released on November 27, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.15-9 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/index.html){:target="_blank"} 7.0.15-9 has been released on November 27, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/7.0/install/index.html){:target="_blank"}.

This release includes a fix for a security vulnerability [CVE-2024-10921](https://nvd.nist.gov/vuln/detail/CVE-2024-10921){:target="_blank"}. This vulnerability allowed an authorized user to trigger server crashes or receive the contents of the buffer over-reads of the server memory by sending specially crafted requests that constructed malformed BSON in MongoDB. 

Users running any minor version of Percona Server for MongoDB 7.0.x before 7.0.15 should [upgrade](https://docs.percona.com/percona-distribution-for-mongodb/7.0/minor-upgrade.html){:target="_blank"} to this latest version as soon as possible. 

This release is also of interest to users who use data-at-rest encryption with the Vault key management server. Before putting a new master encryption key as the versioned secret to Vault, Percona Server for MongoDB now checks if the secret's version reached the defined maximum. This prevents the loss of the old secret and the master encryption key it stores on the Vault server.

Make sure Percona Server for MongoDB has read permissions for the secret’s metadata and the secrets engine configuration. For details, refer to the [documentation](https://docs.percona.com/percona-server-for-mongodb/7.0/vault.html#master-key-loss-prevention){:target="_blank"}.



Learn more about these improvements and other changes in Percona Server for MongoDB 7.0.15-9 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.15-9.html){:target="_blank"}.

