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
---
<!-- more -->

Percona Server for MongoDB 7.0.14-8 has been released on Monday, September 23, 2024.

This release introduces the following improvements:

* Automatic check of the state of master encryption keys on the KMIP server. If a master encryption key for a node transitions to the state other than Active, the node reports an error and shuts down. This method allows security engineers to quickly identify which nodes require out-of-schedule master key rotation. As a result, the mean time to resolve (MTTR) compromised encryption key incidents in KMIP reduces. 
* We provide tarballs for each supported operating system individually and they no longer include built-in libraries. This change  reduces the tarball download size and increases their security by simplifying updates for required dependencies.


Learn more about these improvements and other changes in Percona Server for MongoDB 7.0.14-8 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.14-8.html){:target="_blank"}.

<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>