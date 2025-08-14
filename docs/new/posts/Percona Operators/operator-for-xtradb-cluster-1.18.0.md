---
date: 2025-08-14
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.18.0 has been released on August 14, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.18.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.18.0 has been released on August 14, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

This release provides the following features and enhancements:

* PMM improvements:

    * With added PMM3 support, you can now monitor the health and performance of your Percona Distribution for PostgreSQL deployment and at the same time enjoy enhanced performance, new features, and improved security that PMM 3 provides. Note that PMM2 support remains in the Operator. The decision what PMM version to use is done based on the configured authentication method. Read more about PMM 3 configuration in the [documentation](https://docs.percona.com/percona-operator-for-mysql/pxc/monitoring.html){:target="_blank"}.

    * Improved monitoring for clusters in multi-region or multi-namespace deployments with the ability to define a custom name for a database cluster in PMM. This helps PMM to correctly recognize how a cluster is deployed (in different data centers vs deployed with the same name in different namespaces) and correctly display metrics.

* More resilient database restores without matching user Secrets. The Operator now automatically manages users in the restored database by changing user passwords to the ones from the local Secret, adding missing users and user grants. This enhancement makes managing databases on Kubernetes more robust and operator-friendly.

* Improved backup retention configuration gives you more control over how backups are managed in storage and retained in Kubernetes. Use this new configuration in your Custom Resource:

    ```yaml
    schedule:
      - name: "sat-night-backup"
        schedule: "0 0 * * 6"
        retention:
          count: 3
          type: count
          deleteFromStorage: true
        storageName: s3-us-west
    ``` 

    Note that the legacy `keep` option is now deprecated and mapped to the new `retention` block for compatibility. If you have both `backup.schedule.keep`  and `backup.schedule.retention`  defined, the `backup.schedule.retention` takes precedence.

* Identify the current Operator version associated with Custom Resources via labels. This helps you decide if you need to upgrade it or not.

* Cross-site replication is now available with Percona XtraDB Cluster 8.4.x, lifting one of the tech preview limitations and approaching its general availability.

* The `pxc.expose.loadBalancerIP`, `haproxy.exposePrimary.loadBalancerIP`, `haproxy.exposeReplicas.loadBalancerIP` and `proxysql.expose.loadBalancerIP` keys are deprecated. We recommend using cloud provider-specific annotations instead, as they offer more predictable and portable behavior for managing load balancer IP assignments.

* Percona XtraBackup and Logcollector images are now pulled from official Percona repositories. Pay attention to the new image repositories when you upgrade the Operator and the database. Check the [Percona certified images](https://docs.percona.com/percona-operator-for-mysql/pxc/images.html){:target="_blank"} for exact image names. 


Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.18.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.18.0.html){:target="_blank"}.

