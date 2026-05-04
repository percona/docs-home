---
date: 2026-04-30
description: >
  Percona Monitoring and Management 3.7.1 has been released on Thursday, April 30, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.7.1 has been released

<!-- more -->

We're announcing the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.7.1, available since Thursday, April 30, 2026.

This is primarily a security release. It fixes several CVEs in third-party dependencies, upgrades Grafana, Nomad, and VictoriaMetrics, and masks database credentials in logs to make log sharing safer. It also adds a MongoDB storage fragmentation view, makes PMM Client setup more flexible for containerized environments, and fixes issues in Real-Time Analytics, dashboards, and exporters.

Get hands-on with PMM 3.7.1 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [MongoDB storage fragmentation analysis](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html#spot-mongodb-storage-fragmentation-at-a-glance){:target="_blank"} — the MongoDB Cluster Summary and MongoDB ReplSet Summary dashboards now include a Fragmentation Analysis panel showing the ratio of free to allocated storage per collection
- [Automatic credential masking in logs](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html#safer-log-sharing-with-automatic-credential-masking){:target="_blank"} — PMM now masks database passwords and connection-string credentials in logs, so you can share logs for troubleshooting without exposing sensitive values
- [Flexible PMM Client setup for containers](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html#improvements){:target="_blank"} — use the new `--proc-mounts-path` flag or `PMM_AGENT_SETUP_PROC_MOUNTS_PATH` environment variable to tell PMM Client where to find `/proc/mounts` in non-standard environments
- [Security fixes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html#security-updates){:target="_blank"} addressing a gRPC authorization bypass (CVE-2026-33186), a Grafana SQL expressions remote code execution vulnerability (CVE-2026-27876), and multiple Go standard library vulnerabilities
- [Key components upgraded](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html#components-upgrade){:target="_blank"}: VictoriaMetrics v1.140.0, Nomad v2.0.0, Grafana 11.6.14, and Grafana ClickHouse Datasource v4.15.0

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.1.html){:target="_blank"}.