---
date: 2026-07-30
description: >
  Percona Monitoring and Management 3.9.0 has been released on Thursday, July 30, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.9.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.9.0, available since Thursday, July 30, 2026.

This release adds a new **Alert Status** page for viewing all active alerts by node or service, new MongoDB and PostgreSQL dashboard panels, and CSV export for Real-Time Analytics (RTA) data. 

It also removes the provisioned PostgreSQL datasource as a security measure, adds Ubuntu 26.04 LTS support for PMM Client, and completes the removal of UI-based PMM Server upgrades announced in PMM 3.8.0.

Get hands-on with PMM 3.9.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Alert Status page](https://docs.percona.com/percona-monitoring-and-management/3/alert/alert_status.html){:target="_blank"} (**Alerts > Status**) for viewing every active alert affecting a node or service in a single view, with filtering by state and direct silencing from the table
- [Removed provisioned PostgreSQL datasource](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.0.html#removed-provisioned-postgresql-datasource){:target="_blank"} to prevent Viewer-role users from running arbitrary SQL against PMM's internal database — you can still add it manually if needed
- [Data size panels for MongoDB](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-mongodb-replset-summary.html){:target="_blank"} on the ReplSet Summary and Sharded Cluster Summary dashboards to track current data size and growth over time
- [Disable collectors field](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.0.html#disable-individual-metric-collectors-per-service){:target="_blank"} in the Add service form for MySQL, PostgreSQL, MongoDB, and ProxySQL, so you can exclude specific collectors without modifying the exporter configuration
- [Four new PostgreSQL Top Queries panels](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-postgresql-topqueries.html){:target="_blank"} for identifying queries causing high CPU, memory, I/O, and shared block read pressure
- [CSV export for Real-Time Analytics data](https://docs.percona.com/percona-monitoring-and-management/3/use/qan/QAN-realtime-analytics.html#export-rta-data){:target="_blank"} to preserve a snapshot of in-progress query data that would otherwise be lost when queries are killed before finishing
- [UI upgrade functionality removed](https://docs.percona.com/percona-monitoring-and-management/3/pmm-upgrade/index.html){:target="_blank"}. Upgrade PMM Server using Docker, Podman, or Helm from the command line
- [Ubuntu 26.04 LTS support for PMM Client](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/package_manager.html){:target="_blank"} on AMD64 and ARM64, including Percona Distribution for PostgreSQL 18, Percona Server for MySQL 8.4, and Valkey 9.1

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.0.html){:target="_blank"}.