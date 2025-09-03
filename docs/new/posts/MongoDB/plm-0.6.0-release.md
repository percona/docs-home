---
date: 2025-09-04
description: >
  Percona Link for MongoDB 0.6.0 has been released on September 4, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Link for MongoDB
---

# Percona Link for MongoDB 0.6.0 has been released

<!-- more -->

[Percona Link for MongoDB](https://docs.percona.com/percona-link-for-mongodb/index.html){:target="_blank"} is a tool for replicating data from a source MongoDB cluster to a target MongoDB cluster. It enables you to migrate from MongoDB Atlas or MongoDB Enterprise Edition to Percona Server for MongoDB with zero downtime. 

The first public release of Percona Link for MongoDB 0.6.0 has been released on September 4, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-link-for-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Replication of both unique and non-unique indexes defined on the same fields. Percona Link for MongoDB now supports replication of both unique and non-unique indexes defined on the same fields, improving coverage and reliability. Failed or skipped index creations are automatically retried, ensuring more consistent finalization across environments.

* You can now leverage both CLI and the API to define what namespaces to include or exclude for replication. This enables you to optimize resource utilization and manage the load on your source and target clusters by replicating only the data you care about. Check the command usage in our [https://docs.percona.com/percona-link-for-mongodb/install/usage.html#start-the-filtered-replication)

Read more about this release in Percona Link for MongoDB 0.6.0 [release notes](https://docs.percona.com/percona-link-for-mongodb/release-notes/0.6.0.html){:target="_blank"}