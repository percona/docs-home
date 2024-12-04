---
date: 2024-11-05
description: >
  Percona Server for MongoDB 6.0.18-15 has been released on November 5, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 6.0.18-15 has been released
---
<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/6.0/index.html){:target="_blank"} 6.0.18-15 has been released on November 5, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/6.0/install/index.html){:target="_blank"}. 

This release is of interest to users who use data-at-rest encryption with the Vault key management server. Before putting a new master encryption key as the versioned secret to Vault, Percona Server for MongoDB now checks if the secret's version reached the defined maximum. This prevents the loss of the old secret and the master encryption key it stores on the Vault server.

Make sure Percona Server for MongoDB has read permissions for the secret’s metadata and the secrets engine configuration. For details, refer to the [documentation](https://docs.percona.com/percona-server-for-mongodb/6.0/vault.html#master-key-loss-prevention){:target="_blank"}. 

Learn more about this improvement and other changes in Percona Server for MongoDB 6.0.18-15 [release notes](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.18-15.html){:target="_blank"}.

<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>