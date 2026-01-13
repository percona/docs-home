---
date: 2025-09-04
description: >
  Percona ClusterSync for MongoDB 0.7.0 has been released on January 14, 2026.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona ClusterSync for MongoDB
---

# Percona ClusterSync for MongoDB 0.7.0 has been released

<!-- more --> 

[Percona ClusterSync for MongoDB (PCSM)](https://docs.percona.com/percona-clustersync-for-mongodb/index.html){:target="_blank"} is a tool for replicating data from a source MongoDB cluster to a target MongoDB cluster. It enables you to migrate from MongoDB Atlas or MongoDB Enterprise Edition to Percona Server for MongoDB with near-zero downtime. 

This release marks the general availability of Percona ClusterSync for MongoDB for data migration across replica sets. The GA status means PCSM has passed the stability and reliability milestones required for enterprise use. You can confidently deploy it in production for data migration across replica sets with near-zero downtime.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-clustersync-for-mongodb/installation.html){:target="_blank"} 

This release also provides the following features and improvements:

* Data replication in sharded clusters. You can now replicate data between sharded MongoDB clusters or sync data from one sharded deployment to another. This makes it easier to migrate clusters with minimal downtime, set up disaster recovery across sharded environments, or keep data in sync for testing and development. 

   Learn more about sharding support in our [documentation](https://docs.percona.com/percona-clustersync-for-mongodb/sharding.md){:target="_blank"}


   This feature is in the tech preview stage. We don't recommend using it in production yet, but we encourage you to try it in testing or staging environments and share your feedback. Your input will help us improve and shape the future of Percona ClusterSync for MongoDB. 

* New deployment options. You can now run PCSM in Docker or install it from binary tarballs. These new deployment methods give you more flexibility to choose the approach that best fits your infrastructure, whether you're working in cloud-native setups, air‑gapped systems, or lightweight test environments.

   Refer to our [Quickstart guide](https://docs.percona.com/percona-clustersync-for-mongodb/installation.html){:target="_blank"} for detailed instructions on these new deployment options.

* Ensure data replication continuity for large data sets by fine-tuning the timeout for MongoDB client operations. Set the new value for the `PCSM_MONGODB_CLI_OPERATION_TIMEOUT` environment variable and ensure the replication continues smoothly without being interrupted by the default 5‑minute limit. 

   Learn more about this and other available environment variables in our [documentation](https://docs.percona.com/percona-clustersync-for-mongodb/install/parameters.html){:target="_blank"}.


Read more about this release in Percona ClusterSync for MongoDB 0.7.0 [release notes](https://docs.percona.com/percona-clustersync-for-mongodb/release-notes/0.7.0.html){:target="_blank"}