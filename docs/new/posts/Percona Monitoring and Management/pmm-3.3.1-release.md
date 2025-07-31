---
date: 2025-07-30
description: >
  Percona Monitoring and Management 3.3.1 has been released on Wednesday, July 30, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.3.1 has been released

<!-- more -->

## PMM 3.3.1 Critical security release

We have released a critical security update addressing a Remote Command Execution (RCE) vulnerability affecting all PMM 2.x and PMM 3.x installations. This vulnerability allows users with CLI access to PMM Client nodes or those with admin-level privileges to exploit the API and execute unauthorized commands on registered nodes.

The security vulnerability originates from the `pt-mysql-summary` tool, a component of the Percona Toolkit that automatically collects MySQL system information and diagnostics from PMM Client installations.

!!! warning "Immediate action required: RCE vulnerability in PMM"
    If you're using PMM 2.x or PMM 3.x with connected PMM Client nodes:
    
    - Upgrade IMMEDIATELY to version 3.3.1.
    - Change all credentials for monitored services
    - Review access logs for suspicious activity

For PMM users who cannot immediately migrate to PMM 3.3.1, temporary mitigation options are available but upgrading to PMM 3.3.1 remains the recommended solution.

24/7 support is available through Percona's technical support channels for any assistance needed.

For detailed upgrade instructions, see the [3.3.1 Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.3.1.html).
