---
date: 2026-10-22
description: >
  Percona Monitoring and Management 3.10.0 has been released on Thursday, October 22, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.10.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.10.0, available since Thursday, October 22, 2026.

This release makes **PMM HA Cluster generally available**, with OpenShift support, in-place Helm upgrades, and backup and restore. It also introduces PMM's first database management **Apps**, native ARM64 support for PMM Server, MySQL 9.7 support, and a new MongoDB Unused Indexes dashboard.

It also adds built-in alerts for PMM's own components, per-node alert threshold overrides, and security fixes, and removes PMM Client packages for Debian 11 (Bullseye).

Get hands-on with PMM 3.10.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [PMM HA Cluster is now generally available](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html#pmm-ha-cluster-is-now-generally-available){:target="_blank"} with backup and restore, built-in HA alert rules, OpenShift 4.19–4.22 and Amazon EKS support, in-place `helm upgrade`, scaling to 1, 3, or 5 replicas, and multi-namespace deployments
- [Built-in alerts for PMM's own components](https://docs.percona.com/percona-monitoring-and-management/3/alert/templates_list.html#pmm_component_alerts){:target="_blank"} that warn you when VictoriaMetrics, ClickHouse, Grafana, or the Query Analytics API stop responding, turned on automatically on every PMM Server
- [Database management Apps](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html#database-management-apps-mysql-backups-and-support-diagnostics){:target="_blank"} (Tech Preview) with **MySQL Backups** and **Support diagnostics**, so you can run operations on your hosts directly from PMM without SSH access
- [MongoDB Unused Indexes dashboard](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-mongodb-unused-indexes.html){:target="_blank"} for spotting indexes with zero accesses since the last `mongod` restart across clusters, replica sets, nodes, and databases
- [Per-node alert threshold overrides](https://docs.percona.com/percona-monitoring-and-management/3/alert/alert-thresholds.html){:target="_blank"} so a single alert rule can use a custom sensitivity for specific nodes without editing or duplicating the rule
- [MySQL 9.7 support](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html#mysql-97-support-and-monitoring-improvements){:target="_blank"} for Oracle MySQL and Percona Server, with dashboard and advisor fixes that also improve MySQL 8.0 and newer monitoring
- [Environment filter for MySQL Replication Summary](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-mysql-replication-summary.html){:target="_blank"} to quickly narrow replication data to a specific environment
- [Native ARM64 support for PMM Server](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/deployment-options/docker/index.html){:target="_blank"}, so you can run it on hosts such as AWS Graviton without x86_64 emulation
- [Removed Debian 11 (Bullseye) support for PMM Client](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html#removed-support-for-debian-11-bullseye){:target="_blank"}. Upgrade to Debian 12 or later to keep getting PMM Client updates
- [Security fixes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html#security-updates){:target="_blank"} for Grafana port 3000 bypassing nginx authentication, and for the HAProxy statistics page and default Grafana credentials in PMM HA Cluster

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.10.0.html){:target="_blank"}.
