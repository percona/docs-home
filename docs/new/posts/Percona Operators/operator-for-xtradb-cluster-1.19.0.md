---
date: 2026-01-13
description: >
  Percona Operator for MySQL based on Percona XtraDB Cluster 1.19.0 has been released on January 13, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona XtraDB Cluster 1.19.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona XtraDB Cluster](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html){:target="_blank"} 1.19.0 has been released on January 13, 2026.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/pxc/quickstart.html){:target="_blank"}.

This release provides the following features and enhancements:

## Security and compliance

* Percona XtraDB Cluster 8.4 is generally available and is the default version for cluster deployments. Data-at-rest encryption is also supported for Percona XtraDB Cluster 8.4 via the `keyring_vault` *component*. The rich feature set of the latest major version of Percona XtraDB Cluster 8.4 helps ensure that your sensitive data is secured. In doing so, you can meet compliance requirements and protect critical information without added operational complexity. Learn how to [configure data at rest encryption for Percona XtraDB Cluster 8.4](https://docs.percona.com/percona-operator-for-mysql/pxc/encryption-setup.md){:target="_blank"}.

* Custom CA certificates for TLS verification during backups and restores to S3 storage are now supported. This enhancement allows you to use your own trusted Certificate Authority (CA) certificates for secure TLS connections, ensuring that your backup and restore operations meet specific security policies and compliance requirements. Learn how to [configure custom CA certificates for TLS verification](https://docs.percona.com/percona-operator-for-mysql/pxc/backups-storage.html#configure-tls-verification-with-custom-certificates-for-s3-storage){:target="_blank"}.

* Configurable lifetimes for certificates issued by the cert-manager. You can now set custom lifetimes for certificates issued by the cert-manager when you create a new cluster. This allows you to align certificate expiration with your organization's security policies and operational practices. Note that the Operator enforces minimum duration to certificates:

   * For TLS certificates – 1 hour
   * For CA certificate – 730 hours.

   This flexibility helps ensure that your certificates remain valid and secure over time. Learn how to [configure certificate lifetimes as well as rules and limitations about certificate duration](https://docs.percona.com/percona-operator-for-mysql/pxc/tls-cert-manager.html#customize-certificate-duration-for-cert-manager){:target="_blank"}.

* Security context for ProxySQL sidecar containers. You can now define the security context for ProxySQL sidecar containers in the Operator, reducing the risk of unsecured sidecars bypassing Pod restrictions. This improvement lets you set user IDs, privileges, and filesystem access directly, ensuring compliance and strengthening Pod security. 

## Performance and reliability

* Improved load balancing with ProxySQL scheduler. The new ProxySQL scheduler gives you smarter query routing, automatically balancing reads across nodes while ensuring writes always go to the active writer. This means higher performance, better reliability, and healthier clusters through early detection of lag or node issues.

   This feature is currently in tech preview, so we recommend experimenting with it in test or staging environments before using it in production.

   The previous internal scheduler remains enabled by default to maintain backward compatibility. You can switch to the new one when you're ready to benefit from smarter query handling.

* Faster HAProxy failover. You can now control how quickly HAProxy detects and reacts to node failures. Instead of waiting the default 20 seconds while HAProxy performs the failover, you can tune health checks to cut that down to just a few seconds in a declarative way via the Custom Resource. 

   ```yaml
   haproxy:  
      healthCheck:
          interval: 10000
          rise: 1
          fall: 2
   ```

   That means your applications recover faster, and users don't get stuck with hanging sessions when a node goes down.

* Switch from HAProxy to ProxySQL at runtime. You can now switch from HAProxy to ProxySQL without redeploying your Percona XtraDB Cluster which was not the case previously. ProxySQL has now the `caching_sha2_password` as the default authentication plugin, which gives you the flexibility to start with HAProxy and migrate to ProxySQL later as your needs evolve.

    Each proxy brings its own resource requirements and advantages. We offer [additional guidance](https://docs.percona.com/percona-operator-for-mysql/pxc/load-balancing.html#what-load-balancer-to-use){:target="_blank"} on selecting the right proxy for your environment, plus [detailed recommendations](https://docs.percona.com/percona-operator-for-mysql/pxc/proxy-switching.html){:target="_blank"} on resource planning and best practices. Review these carefully to ensure your choice fits your operational and performance needs.

* ProxySQL 3 support. You can now deploy ProxySQL 3 with Percona Operator for MySQL, giving you greater flexibility and control over application connectivity in Kubernetes. Enjoy seamless password rotation, richer query and event logging, and improved debugging with detailed prepared statement values.

* Direct-access backups via Percona XtraBackup sidecar. Starting with Operator 1.19.0, you can back up your Percona XtraDB Cluster using the new XtraBackup sidecar container, delivering faster and more reliable backups without interrupting client requests. Unlike SST backups, this method doesn't change the database Pod's state to Donor enabling it to keep accepting client requests.

  Since the sidecar constantly runs in the database Pod, you have a constant access to logs and status, which simplifies troubleshooting.

  This feature is in the tech preview stage and currently supports only cloud storages. We encourage you to try it out in your testing or staging environments and leave your feedback.

  Learn more about this backup method and its setup in our [documentation](https://docs.percona.com/percona-operator-for-mysql/pxc/backups.html#xtrabackup-sidecar-method-tech-preview){:target="_blank"}

* Memory allocator configuration. You can now choose between different memory allocators for Percona XtraDB Cluster nodes, allowing you to optimize memory management based on your workload characteristics. The supported allocators include:

   * jemalloc 
   * tcmalloc
   * libc (default)

   To set the memory allocator, modify the Custom Resource:

   ```yaml
   spec:
      pxc:
        mysqlAllocator: jemalloc
   ``` 

   If you have previously set the allocator via the environment variable, the Operator respects this setting and uses that value.

   This enhancement lets you fine-tune memory management for your cluster while keeping compatibility with existing configurations.  

## Operational excellence


- Automatic cleanup of backup/restore jobs. You no longer need to manually clean up backup / restore Jobs and Pods to free up resources. Instead, you can assign a time-to-live (TTL) for backup and restore Jobs once the operation finishes via the Custom Resource:

  ```yaml
  backup:
    image: perconalab/percona-xtradb-cluster-operator:main-pxc8.4-backup
    ttlSecondsAfterFinished: 3600
  ```

   When the TTL expires, the Operator automatically deletes the Job and its associated Pod. This setting is global and applies to all on-demand and scheduled backups as well as all restores. 

   This improvement reduces manual maintenance overhead, gives you control over the processes lifetime for debugging or auditing purposes and helps keep your cluster healthy and efficient.

* Improved backup identification for point-in-time recovery readiness. The Operator now creates a `<backup-name>.pitr-not-ready` file in the backup storage if a backup contains binlog gaps. This file makes it easy to identify which backups are appropriate for point-in-time recovery both in the storage and when listing backup objects. Before starting a restore, the Operator checks for this marker file and blocks unsafe restores, protecting you from incomplete recovery attempts.

- External PVC mounting for shared data. You can now mount an external Persistent Volume Claim (PVC) to the Percona XtraDB Cluster, ProxySQL or HAProxy Pods in a clean, declarative way using the Custom Resource. This feature allows you to share data between the database Pods and other applications or tools running in your Kubernetes cluster such as reference files, shared configuration files or lookup tables. 

   To use this feature, specify the external PVC in the Custom Resource. This example shows how to attach external PVC to the XtraDB Cluster Pods:

   ```yaml
   pxc:
     extraPVCs:
       - name: extra-data-volume
         claimName: my-extra-storage
         mountPath: /var/lib/mysql-extra
         readOnly: false
   ```

   This improvement gives you a reliable way to separate internal database storage from external domain data, update shared datasets independently, and still benefit from the Operator's automation and resilience.


- Customize password generation rules for tools and environments that don't support certain symbols in passwords that the Operator generates. Modify the Custom Resource and specify your rules for password generation:

   ```yaml
   spec:
    passwordGenerationOptions:
      symbols: "!#$%&()*+,-.<=>?@[]^_{}~"
      maxLength: 20
      minLength: 16
   ```

   This flexibility helps ensure compatibility with various tools and environments while maintaining secure password practices and benefiting from automated password generation.

Learn more in Percona Operator for MySQL based on Percona XtraDB Cluster 1.19.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.19.0.html){:target="_blank"}.

