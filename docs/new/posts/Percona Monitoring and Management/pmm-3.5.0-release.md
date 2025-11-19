---
date: 2025-11-19
description: >
  Percona Monitoring and Management 3.5.0 has been released on Wednesday, November 19, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.5.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.5.0, available since Wednesday, November 19, 2025.

This release introduces comprehensive Redis and Valkey monitoring, adds PostgreSQL 18 support, and delivers a major milestone: built-in advisors and alert templates that work completely offline. It also includes enhanced TLS flexibility, improved data privacy controls, and critical security updates.

Get hands-on with PMM 3.5.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Free built-in advisors and alert templates](https://docs.percona.com/percona-monitoring-and-management/3/advisors/advisors.html){:target="_blank"} replacing Percona Platform services, working completely offline with no subscription required
- [Native Redis and Valkey monitoring support](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html){:target="_blank"} with ten dedicated dashboards for performance monitoring, replication tracking, and troubleshooting
- [Enhanced MongoDB dashboards](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.5.0.html#mongodb-dashboard-improvements){:target="_blank"} with improved metrics, idle connection tracking, and fixed node filtering
- [PostgreSQL 18 Community edition support](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/postgresql.html){:target="_blank"} with full compatibility for dashboards and Query Analytics
- [Query Analytics now shows only your monitored databases](https://docs.percona.com/percona-monitoring-and-management/3/use/qan/index.html#qan-for-pmm-servers-internal-postgresql){:target="_blank"}, excluding PMM Server's internal PostgreSQL queries by default for a cleaner, more focused view of your database performance
- [Partial TLS certificates for MySQL monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/mysql/mysql.html){:target="_blank"} enabling monitoring of Azure MySQL Flexible Server and Google Cloud SQL using only CA certificates
- [Disable query examples feature](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.5.0.html#improved-data-privacy-disable-query-examples-in-the-ui){:target="_blank"} to enhance data privacy by preventing display of sensitive SQL queries in Query Analytics
- [Configurable Nomad Garbage Collection](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/deployment-options/docker/env_var.html#nomad-garbage-collection-gc-settings){:target="_blank"} through environment variables for efficient resource management
- [Key components upgraded](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.5.0.html#components-upgrade){:target="_blank"}: ClickHouse 25.3.6.56 for enhanced security, Go runtime 1.24.9 resolving multiple CVEs, and Watchtower for Docker API 1.44+ compatibility

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.5.0.html){:target="_blank"}.