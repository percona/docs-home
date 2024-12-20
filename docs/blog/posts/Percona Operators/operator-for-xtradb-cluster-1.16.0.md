---
date: 2024-12-19
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.16.0 has been released on Thursday, December 19, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.16.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) 1.16.0 has been released on Thursday, December 19, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html).

New features and improvements introduced by these release include:

* [Declarative user management (technical preview)](https://docs.percona.com/percona-operator-for-mysql/pxc/users.html#unprivileged-users) make it possible to create custom MySQL users in the Custom Resource
* [Percona XtraDB Cluster 8.4 support (technical preview)](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.16.0.html#percona-xtradb-cluster-84-support-technical-preview) based on Percona Server for MySQL 8.4 is now available within the Operator in addition to 8.0 and 5.7 versions. 

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.16.0.html#deprecation-rename-and-removal) are the following ones:

Operator versions older than 1.14.1 become incompatible with new HAProxy, ProxySQL and PXC Docker images due to the absence of the peer-list tool in them. If you are still using the older Operator version, make sure to update the Operator before switching to the latest database and proxy images. You can see the [list of Percona certified images](https://docs.percona.com/percona-operator-for-mysql/pxc/images.html) for the current release, and check image versions certified for previous releases in the [documentation archive](https://docs.percona.com/legacy-documentation/).

Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.15.1 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.15.1.html){:target="_blank"}.

