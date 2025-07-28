---
date: 2025-07-28
description: >
  Percona Server for MongoDB 7.0.22-12 has been released on July 28, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.22-12 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/index.html){:target="_blank"} 7.0.22-12 has been released on July 28, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/7.0/install/index.html){:target="_blank"}. 

This release provides the following improvements:

* Boost performance during cluster restore and scaling with [file copy-based initial sync](https://docs.percona.com/percona-server-for-mongodb/7.0/fcbis.html){:target="_blank"}. When a new or a restored member joins a replica set, it can now receive data from other members via physical file copying from the source node. File copy-based initial sync method is faster than the logical one and it reduces your maintenance time on scaling your cluster. 

   This feature is available in [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/7.0/psmdb-pro.html){:target="_blank"} out of the box. [Become a Percona Customer](https://www.percona.com/about/contact) to enjoy all Pro features with little to no effort from your side. Alternatively, you can receive it by building Percona Server from the source code. 

* Percona Server for MongoDB 7.0.22-12 is no longer supported on Ubuntu 20.04 (Focal Fossa) as this operating system has reached end of life. If you're not ready to upgrade to a newer Ubuntu OS but still want to update Percona Server for MongoDB, [contact us](https://hubs.ly/Q03rRtDg0){:target="_blank"}! We're here to make your databases run better.

Learn more about this release in Percona Server for MongoDB 7.0.22-12 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.22-12.html){:target="_blank"}.

