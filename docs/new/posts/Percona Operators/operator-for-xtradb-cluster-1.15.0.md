---
date: 2024-08-20
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.15.0 has been released on Tuesday, August 20, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.15.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.15.0 has been released on Tuesday, August 20, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

New features and improvements introduced by these release include:

* [Automated volume resizing](https://docs.percona.com/percona-operator-for-mysql/pxc/scaling.html#scale-storage){:target="_blank"} feature that allows the Operator to trigger the PVC resize when needed has graduated to general availability.
* [haproxy-replica Service](https://docs.percona.com/percona-operator-for-mysql/pxc/expose.html#__tabbed_1_1){:target="_blank"} can be configured to cycle through the reader instances only, which can be useful to simplify the application logic by splitting read and write MySQL traffic on the Kubernetes level

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.15.0.html#deprecation-rename-and-removal){:target="_blank"} are the following ones:

* Starting from now, `allowUnsafeConfigurations` Custom Resource option is deprecated in favor of a number of options under the [unsafeFlags](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#unsafe-flags-section){:target="_blank"} subsection
* [Finalizers](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#perconaxtradbcluster-custom-resource-options){:target="_blank"} were renamed to contain fully qualified domain names
* The [pxc-operator Helm chart](https://github.com/percona/percona-helm-charts/blob/main/charts/pxc-operator/README.md){:target="_blank"} now has `createNamespace` option set to `false` by default, resulting in not creating any namespaces unless explicitly allowed to do so by the user

Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.15.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.15.0.html){:target="_blank"}.

