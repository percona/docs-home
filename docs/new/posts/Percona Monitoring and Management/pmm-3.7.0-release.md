---
date: 2026-04-01
description: >
  Percona Monitoring and Management 3.7.0 has been released on Wednesday, April 1, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.7.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.7.0, available since Wednesday, April 1, 2026.

This release introduces Real-time Query Analytics (RTA) for MongoDB, completes the Percona Platform removal, and adds the ability to update MongoDB agent configurations on the fly. It also includes PMM Client config file encryption, security fixes, component upgrades, and multiple bug fixes.

Get hands-on with PMM 3.7.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Real-time Query Analytics (RTA) for MongoDB](https://docs.percona.com/percona-monitoring-and-management/3/use/qan/QAN-realtime-analytics.html){:target="_blank"} with live query streaming, pause/resume, and cluster/service filtering to troubleshoot running queries as they execute
- [Change MongoDB monitoring settings on the fly](https://docs.percona.com/percona-monitoring-and-management/3/use/commands/pmm-admin/inventory.html#pmm-admin-inventory-change-agent){:target="_blank"} with the new `pmm-admin inventory change agent` command — update agent configurations without removing and re-adding services
- [PMM Client configuration file encryption](https://docs.percona.com/percona-monitoring-and-management/3/admin/security/client_config_encryption.html){:target="_blank"} to protect sensitive credentials like server passwords and API tokens on disk
- [Percona Platform connectivity removed](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.0.html#percona-platform-connectivity-removed){:target="_blank"} completing the Platform sunset since advisors and alert templates now ship directly with PMM
- [Improved MySQL Replication Summary dashboard](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-mysql-replication-summary.html){:target="_blank"} with unique colors and service names in legends for multi-source replication monitoring
- [Security fixes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.0.html#security-updates){:target="_blank"} addressing an authenticated remote code execution vulnerability (CVE-2026-25212) and multiple Go standard library vulnerabilities
- [Deprecation notices](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.0.html#added-support-and-deprecations){:target="_blank"} for UI-based PMM Server upgrades, OVF virtual appliance images (both after PMM 3.9.0), and direct migration from PMM 2.x (after PMM 3.13.0)
- [Key components upgraded](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.0.html#components-upgrade){:target="_blank"}: VictoriaMetrics v1.138.0, Grafana 11.6.13, and Nomad 1.11.3

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.7.0.html){:target="_blank"}.