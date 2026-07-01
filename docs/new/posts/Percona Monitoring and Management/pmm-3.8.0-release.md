---
date: 2026-05-28
description: >
  Percona Monitoring and Management 3.8.0 has been released on Thursday, May 28, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.8.0 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.8.0, available since Thursday, May 28, 2026.

This release upgrades Grafana to 12.4, adds encrypted PMM dumps for safer data sharing, and continues the native PMM UI migration with an updated Settings page and refreshed visual identity. It also improves dashboard readability and navigation, includes security hardening updates, and announces the deprecation of UI-based upgrades ahead of their removal in PMM 3.9.0.

Get hands-on with PMM 3.8.0 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Grafana 12.4 upgrade](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#grafana-124-upgrade){:target="_blank"} with faster dashboard tables, a new Recovering alert state to reduce noisy notifications, support for recording rules, and automatic migration of legacy Angular panels to modern equivalents
- [Encrypted PMM data dumps](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#encrypted-pmm-data-dumps){:target="_blank"} using AES-256-CTR so you can safely share diagnostic data externally without exposing monitoring data
- [Settings page in native PMM UI](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#settings-page-now-in-native-pmm-ui){:target="_blank"} for a faster and more consistent experience, building on the native navigation introduced in PMM 3.6.0
- [Refreshed visual identity](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#refreshed-look-and-feel){:target="_blank"} with an updated logo, new technology icons for MySQL, PostgreSQL, MongoDB, and Valkey, and a cleaner color palette across the UI
- [Connection timeout setting](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#improvements){:target="_blank"} when adding services, useful for monitoring remote or high-latency databases
- [Security hardening](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#security-updates){:target="_blank"} with zero known vulnerabilities in PMM's own components and assessed third-party risks with mitigating factors documented
- [Deprecation notice](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html#deprecations){:target="_blank"} for UI-based PMM Server upgrades, to be removed in PMM 3.9.0 (July 2026) — switch to Docker, Podman, or Helm upgrade paths now

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.0.html){:target="_blank"}. 
