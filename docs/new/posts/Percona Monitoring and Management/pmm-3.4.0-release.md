---
date: 2025-09-15
description: >
  Percona Monitoring and Management 3.4.0 has been released on Monday, September 15, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.4.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.4.0, available since Monday, September 15, 2025. This release improves enterprise deployments and monitoring reliability, including better OpenShift support and centralized vmagent management. It also enhances RDS tracking, adds RHEL 10 compatibility, and delivers key dashboard updates and bug fixes.

Get hands-on with PMM 3.4.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [OpenShift support for PMM Server](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/deployment-options/helm/index.html){:target="_blank"} 
- [Centralized vmagent settings for all clients](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/deployment-options/docker/env_var.html#configure-vmagent-on-pmm-client){:target="_blank"} using environment variables for simplified configuration across your monitoring infrastructure
- [Support for MySQL Cleartext authentication](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/mysql/mysql.html#add-service-to-pmm#__tabbed_8_){:target="_blank"} including PAM authentication plugins and external authentication methods
- [Enhanced management of RDS instances](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.0.html#enhanced-management-of-rds-instances){:target="_blank"} with Instance ID tracking for better correlation between PMM and AWS console
- [RHEL 10 support for PMM Client](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/package_manager.html){:target="_blank"} on both AMD64 and ARM64 architectures
- [VMware support deprecated](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.0.html#vmware-support-removed){:target="_blank"} and will be fully removed in PMM 3.6.0 (expected January 2026)
- [Upgraded Grafana to version 11.6.3](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.0.html#components-upgrade){:target="_blank"} for enhanced security and improved performance
- [Improved MongoDB dashboards organization](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.0.html#improvements){:target="_blank"} with better navigation and enhanced MongoDB exporter performance

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.0.html){:target="_blank"}.