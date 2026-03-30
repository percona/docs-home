---
date: 2026-30-26
description: >
  Percona Server for MongoDB 7.0.31-17 has been released on March 30, 2026.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.31-17 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/index.html){:target="_blank"} 7.0.31-17 has been released on March 30, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/7.0/install/index.html){:target="_blank"}. 

This release provides the following improvements:

- **Enhanced LDAP authentication caching**

  To provide better parity with MongoDB Enterprise and improve performance in high-scale environments, we have introduced two new configuration parameters for LDAP user caching. These options allow administrators to fine-tune how and when cached user information is refreshed, reducing unnecessary overhead on LDAP servers while ensuring security data remains current.

  **New parameters**

  **ldapUserCacheRefreshInterval:** The ldapUserCacheRefreshInterval parameter sets the frequency (in seconds) at which the server proactively refreshes cached user information from the LDAP server. This allows the system to update permissions and group memberships in the background before the cache entry expires. For more detailed information, refer to MongoDB server parameters.

  **ldapShouldRefreshUserCacheEntries:** The ldapShouldRefreshUserCacheEntries parameter is a toggle that determines the cache renewal strategy. For more detailed information, refer to MongoDB server parameters.

  - If set to true: The server will use the ldapUserCacheRefreshInterval to proactively update entries.

  - If set to false: The server will wait for the ldapUserCacheInvalidationInterval (already supported in PSMDB) to pass before clearing and refetching the entry on the next login attempt.


- Implement LDAP user cache refresh options

  To provide better parity with MongoDB Enterprise and improve performance in high-scale environments, we have introduced two new configuration parameters for LDAP user caching. These options allow administrators to fine-tune how and when cached user information is refreshed, reducing unnecessary overhead on LDAP servers while ensuring security data remains current.



Learn more about this release in Percona Server for MongoDB 7.0.26-14 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.31-17.html){:target="_blank"}.

