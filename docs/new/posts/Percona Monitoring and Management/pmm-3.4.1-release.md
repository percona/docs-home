---
date: 2025-10-13
description: >
  Percona Monitoring and Management 3.4.1 has been released on Monday, October 13, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.4.1 has been released

<!-- more -->

We're pleased to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.4.1, available since Monday, October 13, 2025.

This maintenance release focuses on security improvements, addressing several high-severity vulnerabilities and upgrading critical dependencies to enhance the stability and security of your monitoring infrastructure.

Get hands-on with PMM 3.4.1 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Nomad DoS vulnerability mitigation (CVE-2025-8959)](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html#nomad-denial-of-service-dos-vulnerability-cve-2025-8959){:target="_blank"} with upgrade to Nomad v1.10.5 and minimal risk for default deployments where Nomad is disabled
- [Fixed DoS vulnerability in Percona Toolkit](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html#fixed-dos-in-percona-toolkit-logrus){:target="_blank"} by upgrading to v3.7.0-2, resolving the Logrus dependency issue that could disrupt data collection
- [Clarification on false-positive CVEs](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html#false-positive-reported-cves-pmm-not-affected){:target="_blank"} including OpenSSL cipher processing (CVE-2023-5363), Python Setuptools RCE (CVE-2024-6345), and ClickHouse/Go runtime vulnerabilities (CVE-2024-24790)
- [Removed clickhouse-diagnostics package](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html#clickhouse-vulnerabilities-related-to-outdated-go-runtime-cve-2024-24790){:target="_blank"} to eliminate potential exposure from unused diagnostic utility
- [Transparent disclosure of accepted risks](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html#accepted-risk-openssl-buffer-overflow-vulnerabilities-cve-2022-3786-and-cve-2022-3602){:target="_blank"} for OpenSSL buffer overflow vulnerabilities (CVE-2022-3786 and CVE-2022-3602) pending public Oracle Linux patches

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.4.1.html){:target="_blank"}.