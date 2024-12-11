---
date: 2024-10-30
description: >
  Percona Monitoring and Management 2.43.2 has been released on Wednesday, October 30, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 2.43.2 has been released

<!-- more -->

We're excited to announce the release of 
[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} 2.43.2, available since October 30, 2024. This release brings important enhancements to PostgreSQL support, security improvements, and performance optimizations.

Get hands-on with PMM 2.43.2 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/quickstart/index.html){:target="_blank"} or explore the new changes through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.


Here's a summary of the main changes in this release:
- **PostgreSQL 17 support for Query Analytics (QAN)**: This patch release adds PostgreSQL 17 support for Query Analytics with updates to the `pg_stat_statements` and `pg_stat_monitor` extensions.

- **Secure Grafana image rendering**: PMM Server now supports secure Grafana image rendering capabilities through a dedicated container deployment, providing isolated rendering operations without impacting PMM Server resources.

- Fixed high memory consumption in MongoDB exporter.

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/release-notes/2.43.2.html){:target="_blank"}.







