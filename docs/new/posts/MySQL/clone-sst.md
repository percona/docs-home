---
date: 2025-03-13
description: >
  SST Method using Clone plugin 
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona XtraDB Cluster
---

# Percona XtraDB Cluster feature - SST Method using Clone plugin

<!-- more -->

[Percona XtraDB Cluster 8.0.41-32](https://docs.percona.com/percona-xtradb-cluster/8.0/){:target="_blank"} has been released on Thursday, March 13, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-xtradb-cluster/8.0/quickstart-overview.html){:target="_blank"}.
 
Percona XtraDB Cluster 8.0.41-32 implements the State Snapshot Transfer (SST) Method for Clone plugin. This is a modern and efficient method that leverages MySQL's native cloning capabilities to transfer data from a Donor node to a Joiner node. It is faster and more resource-efficient compared to traditional methods like xtrabackup or rsync. 

The SST method for Clone plugin is currently in [tech preview](https://docs.percona.com/percona-xtradb-cluster/8.0/glossary.html#tech-preview){:target="_blank"}.

## Limitations

Clone plugin limitations are described in [Clone plugin limitations](https://docs.percona.com/percona-server/8.0/clone-plugin-limitations.html){:target="_blank"}.

## Key features

| Feature                 | Description                                                 |
|-------------------------|-------------------------------------------------------------|
| Efficient data transfer | The clone plugin transfers data at the file level, reducing overhead. |
| Consistency            | Ensures data consistency between the Donor and Joiner nodes. |
| Minimal Downtime       | Reduces the time required for node synchronization.         |
| Native Integration     | Fully integrated into MySQL, eliminating the need for external tools. |

Learn more in the [SST Method using Clone plugin](https://docs.percona.com/percona-xtradb-cluster/8.0/clone-sst.html){:target="_blank"} document.
