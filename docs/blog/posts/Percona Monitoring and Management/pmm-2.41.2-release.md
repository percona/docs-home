---
date: 2024-03-20
description: >
  Percona Monitoring and Management 2.41.2 has been released on Monday, March 20, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 2.41.2 has been released

<!-- more -->

We're excited to announce the release of 
[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} 2.41.2, available since June 11, 2024. This release brings important enhancements to PostgreSQL support, security improvements, and performance optimizations.

Get hands-on with PMM 2.41.2 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/quickstart/index.html){:target="_blank"} or explore the new changes through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.


Here's a summary of the main changes in this release:

- Added support for Debian 12 (Bookworm) pmm-client packages
- Introduced new experimental dashboards:
   - Redesigned Kubernetes dashboards with improved clarity
   - New Databases Overview dashboard for unified monitoring
   - PostgreSQL Instance Summary for quick issue identification
   - PostgreSQL Checkpoints, Buffers and WAL Usage dashboard
   - PostgreSQL Patroni dashboard for external service monitoring
- Enhanced PostgreSQL monitoring:
   - Added fallback to pg_stat_statements when pg_stat_monitor is unavailable
   - Added PostgreSQL wraparound metrics collection
   - Improved connection management in postgres_exporter
   - Optimized heavy queries performance
- Fixed several issues:
   - Updated ClickHouse engine to Atomic
   - Resolved MongoDB disk space consumption issue
   - Fixed PostgreSQL connections alert false positives
   - Corrected PostgreSQL instance uptime information
   - Addressed multiple security CVEs

For detailed information, see the complete release notes.

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/release-notes/2.41.2.html){:target="_blank"}.







---
date: 2024-03-20
description: >
  Percona Monitoring and Management 2.41.2 has been released on Monday, March 20, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 2.41.2 has been released

<!-- more -->

We're excited to announce the release of 
[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} 2.41.2, available since June 11, 2024. This release brings important enhancements to PostgreSQL support, security improvements, and performance optimizations.

Get hands-on with PMM 2.41.2 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/quickstart/index.html){:target="_blank"} or explore the new changes through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.


Here's a summary of the main changes in this release:

- Added support for Debian 12 (Bookworm) pmm-client packages
- Introduced new experimental dashboards:
  - Redesigned Kubernetes dashboards with improved clarity
  - New Databases Overview dashboard for unified monitoring
  - PostgreSQL Instance Summary for quick issue identification
  - PostgreSQL Checkpoints, Buffers and WAL Usage dashboard
  - PostgreSQL Patroni dashboard for external service monitoring
- Enhanced PostgreSQL monitoring:
  - Added fallback to pg_stat_statements when pg_stat_monitor is unavailable
  - Added PostgreSQL wraparound metrics collection
  - Improved connection management in postgres_exporter
  - Optimized heavy queries performance
- Fixed several issues:
  - Updated ClickHouse engine to Atomic
  - Resolved MongoDB disk space consumption issue
  - Fixed PostgreSQL connections alert false positives
  - Corrected PostgreSQL instance uptime information
  - Addressed multiple security CVEs

For detailed information, see the complete release notes.

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/release-notes/2.41.2.html){:target="_blank"}.







