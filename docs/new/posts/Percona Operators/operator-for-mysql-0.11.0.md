---
date: 2025-09-01
description: >
  Percona Operator for MySQL based on Percona Server for MySQL 0.11.0 has been released on September 1, 2025.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for MySQL
---

# Percona Operator for MySQL based on Percona Server for MySQL 0.11.0 has been released

<!-- more -->

[Percona Operator for MySQL based on Percona Server for MySQL](https://docs.percona.com/percona-operator-for-mysql/ps/index.html){:target="_blank"} 0.11.0 has been released on September 1, 2025.

Version 0.11.0 of the Percona Operator for MySQL is still **a tech preview release**, and it is **not recommended for production environments**. You can try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mysql/ps/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* Support of MySQL 8.4. The Operator supports all major functionality for this latest major version except data-at-rest encryption. Note that we don't recommend using this version for production environment yet.

* Ensure data security with [data-at-rest encryption](https://docs.percona.com/percona-operator-for-mysql/ps/encryption.html){:target="_blank"}. Data is encrypted automatically, in real time, prior to writing to storage and decrypted when read from storage. The Operator uses the `keyring_vault` plugin to encrypt tablespace files and binlog. It integrates directly with HashiCorp Vault, giving you a secure and automated solution for managing encryption keys.

    Note that data-at-rest encryption is currently not supported for Percona Server for MySQL 8.4.x. We plan to add it in future releases.

* You can now configure the Operator to use `emptyDir` or `hostPath` volumes for MySQL Pods, in addition to `persistentVolumeClaim` volumes. This extends the number of use cases for using the Operator, such as configuring additional storage for the data you don't need to persist when a Pod restarts, ephemeral workloads, testing CI/CD automation against a database and more.

* Improved security for user secrets with special characters in passwords. The Operator now generates stronger passwords using the combination of uppercase and lowercase letters, digits, and special characters like `! $ % & ( ) * + , - . < = > ? @ [ ] ^ _ { } ~ #`. These have been tested to ensure compatibility across SQL queries, shell scripts, YAML files, and connection strings.

    When defining user passwords yourself, use the approved character set to ensure your services run smoothly.

* You can now modify existing ports for the MySQL Router service, as well as add new custom ports. For example, you can separate access to the database for different applications, so that each one connects to the same MySQL Router but gets a tailored experience based on the port.

* You can now scale Percona Server for MySQL storage automatically by configuring the Custom Resource manifest. Your Persistent Volume must support PVC expansion. Find exact steps in our [documentation](https://docs.percona.com/percona-operator-for-mysql/ps/scaling.html#automated-scaling-with-volume-expansion-capability){:target="_blank"}.

* Deprecation, rename and removal

    * `.spec.pmm.runtimeClassName` field has been removed from the `crd.yaml` and code because it wasn't being used
    * `.spec.backup.imagePullSecrets` will now be applied to the backup and restore jobs
    * `.spec.proxy.haproxy.runtimeClassName` will be applied to the HAProxy Pods
    * `.spec.pmm.serverUser` is removed as not used in PMM3


Learn more in Percona Operator for MySQL based on Percona Server for MySQL 0.11.0 [release notes](https://docs.percona.com/percona-operator-for-mysql/ps/ReleaseNotes/Kubernetes-Operator-for-PS-RN0.11.0.html){:target="_blank"}.
