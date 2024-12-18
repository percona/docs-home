---
date: 2024-12-17
description: >
  Percona Server for MongoDB 8.0.4-1 has been released on December 17, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 8.0.4-1 has been released

<!-- more -->

A long awaited new major version of [Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/8.0/index.html){:target="_blank"} 8.0.4-1 has been released on December 17, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/8.0/install/index.html){:target="_blank"}.

This release provides a lot of major changes. We recommend testing it on staging environments before using it in production. When you are ready to upgrade, check the [upgrade instructions](https://docs.percona.com/percona-server-for-mongodb/8.0/install/upgrade-from-70.html){:target="_blank"}

The changes in this release are focused around the following areas:

* Enjoy better performance with the following improvements:

   * A new algorithm enhances time series speed by processing queries in "blocks" of data rather than individual values 
   * Insert operations for multi-document transactions are now batched as a single entry, increasing multi-document insert performance and replication efficiency.
   * A new "oplog buffer" for replication uses separate writer and applier threads that work with oplog entries asynchronously and thus increase replication throughput.

* Analyze query performance and manage the workload in your system using [query shapes](https://www.mongodb.com/docs/manual/core/query-shapes/#std-label-query-shapes){:target="_blank"}. A query shape is a set of specifications to group similar queries together. For a query shape, you add query settings instead of index filters. Query settings are persistent meaning that they remain after the cluster restart thus saving you from rerunning them in your application.

* Your developers can now insert, update or delete multiple collections in one request instead of running then on a single collection only. This improves their experience.

* Manage data distribution across shards better and in a transparent way with these sharding improvements:  

   * Move a single unsharded collection to any shard to optimize resources or distribute the data more evenly across the shards.
   * Reshard a large collection with the same shard key to reduce the sharding time. This also enables you to dynamically reallocate your resources based on the workload. 
   * Unshard a collection if it should reside on a single shard or the collection requires resource isolation
   * Reduce cluster deployment costs by storing both the configuration and the database data on the config server replica set. Such a deployment is recommended for small clusters and is especially useful for evaluating the cluster without having to pay extra costs.

* Receive more accuracy from a database profiler when you analyze performance by logging slow operations based on the time MongoDB actually spent processing that operation.

* Improve security and use Manual Queryable Encryption in accounting operations, healthcare, financial services, and other strictly regulated data operations where data safety is crucial with the ability to run range queries on encrypted fields, specifically for numeric data types and dates. 


In addition to features and improvements of MongoDB Community 8.0.0 through 8.0.4, you also benefit from a [better handling of master encryption keys on the Vault server](https://docs.percona.com/percona-server-for-mongodb/8.0/vault.html#master-key-loss-prevention){:target="_blank"}. Before putting a new master encryption key as the versioned secret to Vault, Percona Server for MongoDB now checks if the secret's version reached the defined maximum. This prevents the loss of the old secret and the master encryption key it stores on the Vault server.


Learn more about these improvements and other changes in Percona Server for MongoDB 8.0.4-1 [release notes](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.4-1.html){:target="_blank"}.

