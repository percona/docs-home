---
date: 2024-10-01
description: >
  Percona Everest 1.2.0 now includes Breaking API changes
authors: [rasika-chivate]
categories:
  - Percona Everest
tags:
  - Percona Everest
---

# Breaking API changes in Percona Everest

<!-- more -->

Give [Percona Everest](https://docs.percona.com/everest/index.html){:target="_blank"} a go by following our [Quickstart guide](https://docs.percona.com/everest/quickstart-guide/quick-install.html){:target="_blank"}.

The breaking API changes as part of Percona Everest 1.2.0 include: 

- Previously, the resources `monitoring-instances` and `backup-storages` had a global scope. Percona Everest used a `.spec.allowedNamespaces` field to control access to these global resources. This field defined the namespaces where the resources could be accessed, thus providing some degree of access control.
- With the upgrade to Percona Everest version 1.2.0, the transition from global scope to the designated namespaces for these resources is an important change in the way access control is managed. This improves security as the resources are only accessible within their designated namespaces. The database clusters can only use monitoring-instances and backup-storages located within the same namespace as the cluster.
- When upgrading to 1.2.0 using the CLI command everestctl upgrade, all your existing backup-storages and monitoring-instances will be automatically migrated to the namespaces specified in their `.spec.allowedNamespaces` fields.



<!-- more -->

Explore more in Percona Everest 1.2.0 [release notes](https://docs.percona.com/everest/release-notes/Percona-Everest-1.2.0-%282024-10-01%29.html#__tabbed_1_1){:target="_blank"}.
