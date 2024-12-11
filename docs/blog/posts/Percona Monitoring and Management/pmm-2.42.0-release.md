---
date: 2024-06-11
description: >
  Percona Monitoring and Management 2.42.0 has been released on Tuesday, June 11, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 2.42.0 has been released

<!-- more -->

We're excited to announce the release of 
[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} 2.42.0, available since June 11, 2024. This release brings important enhancements to PostgreSQL support, security improvements, and performance optimizations.

Get hands-on with PMM 2.42.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/quickstart/index.html){:target="_blank"} or explore the new changes through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.


Here's a summary of the main changes in this release:

- Added official support for Ubuntu 24.04 Noble Numbat operating system
- Introduced configurable metrics resolutions (Low, Medium, High) per service via API
- Improved PostgreSQL and PMM Agent connection management with configurable limits
- Added new experimental PMM Health dashboard for self-monitoring
- Released experimental redesigned MongoDB dashboards for Sharded Cluster and Replica Set
- Enhanced MySQL Query Response Time Distribution graphs with sub-100ms resolution
- Added per-database metrics collection and control parameters
- Added new PostgreSQL replication metrics labels
- Added support for MySQL 8.0's innodb_redo_log_capacity variable
- Fixed MongoDB RepSet Summary dashboard data accuracy
- Fixed MongoDB sharding information collection timeouts
- Fixed PMM Server upgrade issues for AMI/OVF installations
- Fixed incorrect MongoDB replication lag graph values

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/release-notes/2.42.0.html){:target="_blank"}.







