---
date: 2024-09-23
description: >
  Percona Server for MongoDB 7.0.14-8 has been released on Monday, September 23, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.14-8 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/index.html){:target="_blank"} 7.0.14-8 has been released on Monday, September 23, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/7.0/install/index.html){:target="_blank"}.

This release introduces the following improvements:

* Automatic check of the state of master encryption keys on the KMIP server. If a master encryption key for a node transitions to the state other than Active, the node reports an error and shuts down. This method allows security engineers to quickly identify which nodes require out-of-schedule master key rotation. As a result, the mean time to resolve (MTTR) compromised encryption key incidents in KMIP reduces. 
* We provide tarballs for each supported operating system individually and they no longer include built-in libraries. This change  reduces the tarball download size and increases their security by simplifying updates for required dependencies.
* Packaging changes:

    * Added support for Ubuntu 24.04 (Noble Numbat)
    * Dropped support for Red Hat Enterprise 7 and derivatives as these operating systems reached End-Of-Life


Learn more about these improvements and other changes in Percona Server for MongoDB 7.0.14-8 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.14-8.html){:target="_blank"}.

