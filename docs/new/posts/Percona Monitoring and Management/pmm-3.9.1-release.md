---
date: 2026-08-19
description: >
  Percona Monitoring and Management 3.9.1 has been released on Wednesday, August 19, 2026.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.9.1 has been released

<!-- more -->

We're announcing the release of [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.9.1, available since Wednesday, August 19, 2026.

PMM 3.9.1 is a security-focused release. It fixes a high-severity vulnerability where the Grafana ClickHouse data source connected using a privileged account, giving any signed-in user — including those with the lowest-privilege Viewer role — the ability to run arbitrary SQL. We strongly recommend upgrading as soon as possible. This release also removes eight high-severity CVEs by dropping the `percona-telemetry-agent` binary, fixes an encryption key rotation bug that corrupted stored credentials, and resolves an issue where PMM Client stayed disconnected after a network interruption.

Get hands-on with PMM 3.9.1 using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [High-severity vulnerability fixed](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html#high-severity-vulnerability-fixed-upgrade-now){:target="_blank"}: the Grafana ClickHouse data source now connects as a dedicated, read-only user instead of a privileged account — upgrade immediately and, if you use an external ClickHouse instance, create the read-only user before upgrading
- [Removed percona-telemetry-agent](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html#removed-percona-telemetry-agent-from-pmm-server-image){:target="_blank"}: eliminates eight high-severity Go standard library CVEs carried by that binary
- [Encryption key rotation fix](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html#fixed-issues){:target="_blank"}: `pmm-encryption-rotation` no longer corrupts TLS certificates, keys, and cloud credentials for monitored services
- [PMM Client reconnection fix](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html#fixed-issues){:target="_blank"}: the agent no longer stays stuck as Disconnected after a network interruption — it recovers automatically within about a minute
- [MongoDB sharded cluster fix](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html#fixed-issues){:target="_blank"}: index and collection statistics from mongos nodes are now correctly labeled per shard, with no duplicate-metric log flooding

You can find the full list of changes in the [Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.9.1.html){:target="_blank"}.
