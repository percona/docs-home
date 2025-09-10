---
date: 2025-09-11
description: >
  Percona Server for MongoDB 7.0.24-13 has been released on September 11, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.24-13 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/index.html){:target="_blank"} 7.0.24-13 has been released on September 11, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/7.0/install/index.html){:target="_blank"}. 

This release provides the following improvements:

* Enhance security with token-based authentication using OpenID Connect (OIDC). Now your users no longer have to share their credentials with Percona Server for MongoDB or MongoDB clients when they authenticate in your infrastructure. Instead, you configure a Single Sign-On using an external identity provider and have users authenticate via tokens. This way you centralize user management and eliminate the need to store credentials in your database, reducing the risk of credential theft. Learn more about this new authentication method in our [documentation](https://docs.percona.com/percona-server-for-mongodb/7.0/oidc.html){:target="_blank"}.

   This feature is available in [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/7.0/psmdb-pro.html){:target="_blank"} out of the box. You can also receive it by building Percona Server from the source code.

* No vendor lock-in with OpenBao support for data-at-rest encryption. Percona Server for MongoDB is integrated with OpenBao, the open-source fork of Vault. This enables you to offer the same level of security — without the constraints of vendor lock-in. For guidance on configuring OpenBao, check our [documentation](https://docs.percona.com/percona-server-for-mongodb/7.0/openbao.html){:target="_blank"}.

Learn more about this release in Percona Server for MongoDB 7.0.24-13 [release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.24-13.html){:target="_blank"}.

