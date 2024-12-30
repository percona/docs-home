---
date: 2024-08-08
description: >
  Percona Server for MongoDB 5.0.28-24 has been released on August 8, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 5.0.28-24 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/5.0/index.html){:target="_blank"} 5.0.28-24 has been released on August 8, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/5.0/install/index.html){:target="_blank"}. 

This release includes all fixes and enhancements of MongoDB 5.0.28 Community Edition. It also provides the following features:

* Enhanced [Telemetry](https://docs.percona.com/percona-server-for-mongodb/5.0/telemetry.html){:target="_blank"} for better product usage reporting. Learn what telemetry is, why it exists, how it works and how you can disable it.
* Reduce mean time to resolve (MTTR) compromised encryption key incidents in KMIP. Percona Server for MongoDB automatically checks the state of master encryption keys and enables your security engineers to quickly identify which nodes require out-of-schedule master key rotation. Learn more Learn more about key state polling from [the documentation](https://docs.percona.com/percona-server-for-mongodb/5.0//kmip.html#key-state-polling){:target="_blank"}
* Easier dependency management with thinner tarballs. Tarballs are now available for each supported operating system individually and no longer include built-in libraries. This change reduces the tarball download size and increases their security by simplifying updates for required dependencies. 


Learn more about this release in Percona Server for MongoDB 5.0.28-24 [release notes](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.28-24.html){:target="_blank"}.

