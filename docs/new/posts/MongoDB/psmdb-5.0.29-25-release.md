---
date: 2024-08-08
description: >
  Percona Server for MongoDB 5.0.29-25 has been released on August 8, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 5.0.29-25 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/5.0/index.html){:target="_blank"} 5.0.29-25 has been released on August 8, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/5.0/install/index.html){:target="_blank"}. 

This release is the last in Percona Server for MongoDB 5.0.x series as this version has reached end of life. Read more about the implications and why you should upgrade to the active major version in [Percona blog](https://www.percona.com/blog/mongodb-4-4-eol-with-5-0-not-far-behind/){:target="_blank"}.

This release is of interest to users who use data-at-rest encryption with the Vault key management server. Before putting a new master encryption key as the versioned secret to Vault, Percona Server for MongoDB now checks if the secret's version reached the defined maximum. This prevents the loss of the old secret and the master encryption key it stores on the Vault server.

Make sure Percona Server for MongoDB has read permissions for the secret’s metadata and the secrets engine configuration. For details, refer to the [documentation](https://docs.percona.com/percona-server-for-mongodb/5.0/vault.html#master-key-loss-prevention){:target="_blank"}. 

Packaging changes:

* Dropped support for Debian 10 and Red Hat Enterprise 7 and derivatives as these operating systems reached End-Of-Life.

Learn more about this release in Percona Server for MongoDB 5.0.29-25 [release notes](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.29-25.html){:target="_blank"}.

