---
date: 2025-04-14
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.17.0 has been released on April 14, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.17.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.17.0 has been released on Thursday, April 14, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

This release provides the following features and enhancements:

* [Improved observability for HAProxy and ProxySQL](https://docs.percona.com/percona-operator-for-mysql/pxc/haproxy-conf.html){:target="_blank"} with the ability to connect to their statistics pages.
* [Improved cluster load management during backups](https://docs.percona.com/percona-operator-for-mysql/pxc/backups.html){:target="_blank"} by queuing simultaneous backups if you disabled their parallel execution. You can fine-tune the queue by setting the start time for all backups or for a specific on-demand one using the [`spec.backup.startingDeadlineSeconds`](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#backupstartingdeadlineseconds) Custom Resource option.

    Another improvement is in suspending backups when your cluster becomes unhealthy and resuming them when the cluster recovers. You can configure how long a backups remains suspended to offload your cluster even more. In this case, after the set time expires, the Operator marks a backup as failed. 

* Observability improvements:

    * Monitor PMM Client health and status using Kubernetes probes added to a PMM Client container. Use the [`spec.pmm.readinessProbes.*`](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#pmmreadinessprobesinitialdelayseconds){:target="_blank"} and [`spec.pmm.livenessProbes.*`](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html#pmmlivenessprobesinitialdelayseconds){:target="_blank"} Custom Resource options to fine-tune Readiness and Liveness probes.

    * Get insights into the binlog performance by connecting to the `<pitr-pod-service>:8080/metrics` endpoint. Learn more about the available metrics in the [documentation](https://docs.percona.com/percona-operator-for-mysql/pxc/backups-pitr.html#binary-logs-statistics){:target="_blank"}.

* The `spec.haproxy.exposePrimary.enabled` field is deprecated. If enabled via the `spec.haproxy.enabled`, the HAProxy primary service is already exposed. 


Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.17.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.17.0.html){:target="_blank"}.

