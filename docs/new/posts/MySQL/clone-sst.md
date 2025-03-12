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

This feature is currently in [tech preview](https://docs.percona.com/percona-xtradb-cluster/8.0/glossary.html#tech-preview){:target="_blank"}. Before using this feature in production, we recommend that you test restoring production from physical backups in your environment. Implement an alternative backup method for redundancy.

Percona XtraDB Cluster 8.0.41-32 implements the Clone plugin for State Snapshot Transfer (SST) Method. The Clone SST is a modern and efficient method that leverages MySQL's native cloning capabilities to transfer data from a donor node to a Joiner node. It is faster and more resource-efficient compared to traditional methods like xtrabackup or rsync.

## Limitations

Clone limitations are described in [Clone plugin limitations](https://docs.percona.com/percona-server/8.0/clone-plugin-limitations.html){:target="_blank"}

## Key features

| Feature                 | Description                                                 |
|-------------------------|-------------------------------------------------------------|
| Efficient data transfer | The clone plugin transfers data at the file level, reducing overhead. |
| Consistency            | Ensures data consistency between the donor and Joiner nodes. |
| Minimal Downtime       | Reduces the time required for node synchronization.         |
| Native Integration     | Fully integrated into MySQL, eliminating the need for external tools. |

Learn more in the [SST Method using Clone plugin](https://docs.percona.com/percona-xtradb-cluster/8.0/clone-sst.html){:target="_blank"} document.
