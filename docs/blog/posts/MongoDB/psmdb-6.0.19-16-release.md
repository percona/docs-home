---
date: 2024-11-28
description: >
  Percona Server for MongoDB 6.0.19-16 has been released on November 28, 2024.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 6.0.19-16 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/6.0/index.html){:target="_blank"} 6.0.19-16 has been released on November 28, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/6.0/install/index.html){:target="_blank"}. 

This release of includes a fix for a security vulnerability [CVE-2024-10921](https://nvd.nist.gov/vuln/detail/CVE-2024-10921){:target="_blank"}. This vulnerability allowed an authorized user to trigger server crashes or receive the contents of the buffer over-reads of the server memory by sending specially crafted requests that constructed malformed BSON in MongoDB. The issue is fixed and included in Percona Server for MongoDB 6.0.19-16. If you wish to [upgrade to the following major version](https://docs.percona.com/percona-server-for-mongodb/7.0/install/upgrade-from-60.html){:target="_blank"}, the fix is also included in Percona Server for MongoDB 7.0.15-9.    

Learn more about this release in Percona Server for MongoDB 6.0.19-16 [release notes](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.19-16.html){:target="_blank"}.

