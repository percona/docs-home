---
date: 2025-08-21
description: >
  Centralized authentication with OpenID Connect (OIDC) in Percona Server for MongoDB.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Enhanced authentication with OpenID Connect (OIDC) in Percona Server for MongoDB

<!-- more -->

Improve security in your infrastructure utilizing OpenID Connect (OIDC) and OAuth 2.0 for token-based authentication and authorization of users and applications. These tokens are issued by an external identity provider (IdP). The IdP serves as a centralized storage of user credentials, which are not shared with either Percona Server for MongoDB or MongoDB clients.

With centralized user management on the IdP side, administrators can define granular access policies and roles, streamlining permissions for individuals and applications. Administrators can leverage advanced authentication techniques such as Single Sign-On (SSO) and Multi-Factor Authentication (MFA), improving both security and user experience. 

Learn more about authentication flow and configuration guidelines in our [documentation](https://docs.percona.com/percona-server-for-mongodb/8.0/oidc.html){:target="_blank"}.

This feature is available out of the box with [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/8.0/psmdb-pro.html){:target="_blank"} starting with version 8.0.12-4. You can also access it by building Percona Server for MongoDB from source. [Contact Percona](https://www.percona.com/about/contact){:target="_blank"} to unlock Pro features with minimal effort.