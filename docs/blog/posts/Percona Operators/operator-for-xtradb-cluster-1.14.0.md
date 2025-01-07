---
date: 2024-03-04
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.14.0 has been released on Monday, March 4, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.14.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.14.0 has been released on Monday, March 4, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

New features and improvements introduced by these release include:

* [A quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"} was added to the Operator docs, providing a guided step by step through quick installing, connecting to the database, inserting data, making a backup, and integrating with Percona Monitoring and Management (PMM) to monitor the cluster
* [Automated volume resizing](https://docs.percona.com/percona-operator-for-mysql/pxc/scaling.html#scale-storage){:target="_blank"} allows the Operator to detect if the storage usage on the PVC reaches a certain threshold, and trigger the PVC resize

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.14.0.html#deprecation-rename-and-removal){:target="_blank"} are the following ones:

* Custom Resource options for service exposure of Percona XtraDB Cluster HAProxy Primary, HAProxy Replicas, and ProxySQL [were moved](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.14.0.html#deprecation-rename-and-removal){:target="_blank"} to dedicated pxc.expose, haproxy.exposePrimary, haproxy.exposeReplicas, and proxysql.expose subsections.
* The `initImage` Custom Resource option was moved to a dedicated subsection and is now available as [initContainer.image](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#initcontainerimage){:target="_blank"}
* The `clustercheck` system user deprecated in v1.12.0 was [completely removed](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.14.0.html#deprecation-rename-and-removal){:target="_blank"} in this release

Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.14.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.14.0.html){:target="_blank"}.

