---
date: 2026-02-05
description: >
  Percona Monitoring and Management 3.6.0 has been released on Thursday, February 5, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.6.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.6.0, available since Thursday, February 5, 2026.

This release delivers a redesigned interface with native PMM navigation, introduces High Availability Cluster (Technical Preview) for zero-downtime failover, and includes improved MongoDB dashboards. 

It also expands platform support for PostgreSQL 18 on RHEL 10 and Debian 13, addresses a critical security vulnerability, and completes the VMware deprecation.

Get hands-on with PMM 3.6.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [New native PMM navigation](https://docs.percona.com/percona-monitoring-and-management/3/reference/ui/ui_components.html){:target="_blank"} with an always-visible sidebar, persistent time ranges across dashboards, and integrated theme switching
- [High Availability Cluster (Technical Preview)](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/HA-clustered.html){:target="_blank"} with three-node Raft consensus, HAProxy load balancing, and Helm-based installation for zero-downtime monitoring
- [HA status monitoring enhancements](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-ha-health-overview.html){:target="_blank"} including new HA badge, Inventory integration, and HA Health Overview dashboard for all HA deployment types
- [Simplified MongoDB dashboards](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html#mongodb-dashboard-improvements){:target="_blank"} for faster cluster health monitoring with streamlined Instances Overview, Instance Summary, and Router Summary panels
- [Redesigned MongoDB Backup Details dashboard](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html#redesigned-mongodb-backup-details-dashboard){:target="_blank"} with new panels for monitoring backup agent health and enhanced backup history tracking
- [PostgreSQL 18 monitoring support on RHEL 10](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/package_manager.html){:target="_blank"} extending platform coverage for AMD64 and ARM64 systems
- [Debian 13 (Trixie) support for PMM Client](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/package_manager.html){:target="_blank"} enabling monitoring on the latest Debian release
- [Critical security fix](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html#authenticated-remote-code-execution-vulnerability){:target="_blank"} addressing an authenticated remote code execution vulnerability—upgrade strongly recommended
- [VMware support removed](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html#vmware-support-removed){:target="_blank"} completing the deprecation announced in PMM 3.4.0; migrate to Docker, Podman, VirtualBox, or Kubernetes
- [Key components upgraded](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html#components-upgrade){:target="_blank"}: Nomad v1.11.1 with security enhancements, Percona Toolkit 3.7.1, and Valkey Exporter 1.80.2

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.6.0.html){:target="_blank"}.