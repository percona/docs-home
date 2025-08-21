---
date: 2025-08-21
description: >
  Percona Server for MongoDB 8.0.12-4 has been released on August 21, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 8.0.12-4 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/8.0/index.html){:target="_blank"} 8.0.12-4 has been released on August 21, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/8.0/install/index.html){:target="_blank"}. 

This release provides the following improvements:

* Boost performance during cluster restore and scaling with [file copy-based initial sync](https://docs.percona.com/percona-server-for-mongodb/8.0/fcbis.html){:target="_blank"}. When a new or a restored member joins a replica set, it can now receive data from other members via physical file copying from the source node. File copy-based initial sync method is faster than the logical one and it reduces your maintenance time on scaling your cluster. 

   This feature is available in [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/8.0/psmdb-pro.html){:target="_blank"} out of the box. [Become a Percona Customer](https://www.percona.com/about/contact) to enjoy all Pro features with little to no effort from your side. Alternatively, you can receive it by building Percona Server from the source code. 

* Enhance security with token-based authentication using OpenID Connect (OIDC). Now you users no longer have to share their credentials with Percona Server for MongoDB or MongoDB clients when they authenticate in your infrastructure. Instead, you configure a Single Sign-On using an external identity provider and have users authenticate via tokens. This way you centralize user management and eliminate the need to store credentials in your database, reducing the risk of credential theft. Learn more about this new authentication method in our [documentation](https://docs.percona.com/percona-server-for-mongodb/8.0/oidc.html){:target="_blank"}.

   This feature is available in [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/8.0/psmdb-pro.html){:target="_blank"} out of the box. You can also receive it by building Percona Server from the source code.

* Percona Server for MongoDB 8.0.12-4 is no longer supported on Ubuntu 20.04 (Focal Fossa) as this operating system has reached end of life. If you're not ready to upgrade to a newer Ubuntu OS but still want to update Percona Server for MongoDB, [contact us](https://hubs.ly/Q03rRtDg0){:target="_blank"}! We're here to make your databases run better.


Learn more about this release in Percona Server for MongoDB 8.0.12-4 [release notes](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.12-4.html){:target="_blank"}.

