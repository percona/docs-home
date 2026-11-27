---
date: 2026-11-26
description: >
  Percona Monitoring and Management 3.11.0 has been released on Thursday, November 26, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.11.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.11.0, available since Thursday, November 26, 2026.

This release introduces **alerts on slow queries** from Query Analytics data, **smarter Advisors** that run on schedule and email their results, and a native PMM UI **Inventory** page.

It also adds the `pmm-admin update` command, deprecates PostgreSQL 14 in PMM Server and VictoriaMetrics downsampling, and fixes critical vulnerabilities in nginx and ClickHouse. We recommend upgrading as soon as possible.

Get hands-on with PMM 3.11.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Alerts on slow queries](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#alert-on-slow-queries-with-query-analytics-data){:target="_blank"} based on Query Analytics data, with a built-in template that alerts you when the slowest query on a MySQL, PostgreSQL, or MongoDB service runs longer than 10 seconds
- [Smarter Advisors](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#smarter-advisors-that-run-on-schedule-email-results-and-suggest-fixes){:target="_blank"} that run on a schedule, email you a report after each run, and show how to fix most findings on the new **Insights** page. A single version check for each database replaces the overlapping version, end-of-life, and vulnerability checks
- [Inventory page in native PMM UI](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#inventory-page-now-in-native-pmm-ui){:target="_blank"} with filtered views you can bookmark and share, and credentials, TLS, and query source settings you can change without removing a service
- [`pmm-admin update` command](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#change-a-monitored-service-from-the-command-line-without-removing-it){:target="_blank"} to change the settings of a monitored service in one step, while it keeps its metrics, Query Analytics history, alerts, and backups
- [Failing Backup Agents table](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#find-failing-mongodb-backup-agents-at-a-glance){:target="_blank"} on the **MongoDB Backup Details** dashboard, plus [more PBM metrics](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#more-metrics-to-monitor-percona-backup-for-mongodb-pbm){:target="_blank"} for your own dashboards and alerts
- [PostgreSQL 14 deprecated in PMM Server](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#postgresql-14-deprecated-in-pmm-server){:target="_blank"}. If you run PMM 3.9.1 or earlier, upgrade before PMM 3.13.0 (expected January 2027) to keep a one-step upgrade
- [VictoriaMetrics downsampling deprecated](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#victoriametrics-downsampling-deprecated){:target="_blank"}. If you use it, prepare before you upgrade to PMM 3.12.0
- [Security fixes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#security-updates){:target="_blank"} for critical vulnerabilities in [nginx](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#nginx-http2-memory-corruption-cve-2026-123007-123633){:target="_blank"} and [ClickHouse](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html#clickhouse-remote-code-execution-cve-2026-116366){:target="_blank"}, and for Grafana anonymous access exposing PMM features

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.11.0.html){:target="_blank"}.
