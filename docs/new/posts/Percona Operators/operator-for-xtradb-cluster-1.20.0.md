---
date: 2026-06-05
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.20.0 has been released on June 5, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.20.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.20.0 has been released on June 5, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

This release provides the following features and enhancements:

## Security and compliance

* [Automated TLS certificates rotation](https://docs.percona.com/percona-operator-for-mysql/pxc/tls-update.html){:target="_blank"}. You no longer need a manual, multi-step procedure to roll over TLS certificates. Provide updated CA, server, and key material in a Secret, and the Operator applies the change on the next reconciliation loop with minimal downtime and less risk of human error. 

## Performance and reliability

* [Automatic storage resizing based on your usage thresholds](https://docs.percona.com/percona-operator-for-mysql/pxc/scaling.html#automatic-storage-resizing){:target="_blank"}. The Operator now monitors disk usage on Percona XtraDB Cluster Pods and expands the storage automatically when the usage crosses your thresholds. As a result, you spend less time on capacity planning, save costs by expanding only when needed and avoid outages from full disks.

* Improved external HAProxy checks with a configurable file descriptor limit. When HAProxy performs external MySQL health checks, it tries to close every file descriptor (FD) up to the system limit before executing the check script. If the FD limit is huge, this can lead to long delays and outages. This release sets the safe FD limit to the HAProxy entrypoint which you can also override via an environment variable. This improvement ensures external checks are fast, stable, and predictable.

* Version-aware `jemalloc` path selection for optimized memory usage. When you choose `jemalloc` as the memory allocator, the Operator now selects the correct shared library path for your Percona XtraDB Cluster version, so clusters start reliably without manual path fixes for 8.0 vs 8.4. The default `jemalloc` path is changed to `/usr/lib64/libjemalloc.so.2` to align with the default Percona XtraDB Cluster 8.4 version for new cluster deployments. 

* Percona XtraDB Cluster 8.4 has NUMA disabled by default. MySQL 8.4 enables NUMA interleaving by default, but that often causes warnings or blocked requests in Kubernetes. The Operator now disables it by default for Percona XtraDB Cluster 8.4, giving you cleaner logs and more predictable behavior in typical cloud environments.

## Operational excellence

* Configurable leader election for the Operator Deployment. If the Operator struggles with leader election in high-latency or resource-constrained clusters, you can now tune lease duration, renewal deadlines, and retry behavior through environment variables instead of being stuck with fixed defaults. Refer to [Environment variables reference](https://docs.percona.com/percona-operator-for-mysql/pxc/env-vars-operator.html){:target="_blank"} for details.

## Deprecation, rename, removal

* Deprecated support for PMM2 - With PMM2 entering the end-of-life stage, its support is now deprecated in the Operator. It remains operational for the next two releases, after which it will be removed. [Plan your migration to PMM3](https://docs.percona.com/percona-monitoring-and-management/3/pmm-upgrade/migrating_from_pmm_2.html){:target="_blank"} to enjoy all new features and security patches supplied with this latest major version.

Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.20.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.20.0.html){:target="_blank"}.

