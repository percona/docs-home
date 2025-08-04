---
date: 2025-07-28
description: >
  File copy-based initial sync in Percona Server for MongoDB.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# File copy-based initial sync in Percona Server for MongoDB

<!-- more -->

Speed up replica set initialization and cluster scaling with the [file copy-based initial sync](https://docs.percona.com/percona-server-for-mongodb/7.0/fcbis.html){:target="_blank"} in Percona Server for MongoDB. 

This enterprise-grade sync method uses physical file copying to transfer data, reducing the sync time for large datasets and write-heavy workloads as compared to logical initial sync. 

This feature is available out of the box with [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/7.0/psmdb-pro.html){:target="_blank"} starting with version 7.0.22-12 and will also be included in the upcoming 8.0 release. You can also access it by building Percona Server for MongoDB from source. [Contact Percona](https://www.percona.com/about/contact){:target="_blank"} to unlock Pro features with minimal effort.