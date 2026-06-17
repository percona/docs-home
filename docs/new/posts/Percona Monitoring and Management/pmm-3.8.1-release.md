---
date: 2026-06-16
description: >
  Percona Monitoring and Management 3.8.1 has been released on Monday, June 16, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.8.1 has been released

<!-- more -->

We're excited to announce the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.8.1, available since Monday, June 16, 2026.

This is a security-focused release that patches critical and high-severity vulnerabilities in gRPC, Grafana, and nginx, and fixes several ClickHouse and dashboard stability issues.

Get hands-on with PMM 3.8.1 by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Grafana upgraded to 12.4.3+security-02](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.1.html#security-updates){:target="_blank"} — addresses 10 security vulnerabilities; upgrade to PMM 3.8.1 as soon as possible
- [Security fixes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.1.html#security-updates){:target="_blank"} addressing a critical pgx memory-safety vulnerability (CVE-2026-33816), a gRPC authorization bypass (CVE-2026-33186), a Go stdlib MIME header decoding DoS (CVE-2026-42504), Docker engine vulnerabilities in Nomad (CVE-2026-41567 and CVE-2026-42306), and an nginx TLS backend injection (CVE-2026-1642)
- [Zero vulnerabilities in PMM-owned components](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.8.1.html#security-updates){:target="_blank"} — all PMM binaries report