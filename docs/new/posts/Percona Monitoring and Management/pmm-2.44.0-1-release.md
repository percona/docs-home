---
date: 2025-02-10
description: >
  Percona Monitoring and Management 2.44.0-1 has been released on Monday, February 10, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management  2.44.0-1 has been released

<!-- more -->

## PMM 2.44.0-1 Critical security release
We have released a critical security update addressing a vulnerability in PMM Open Virtual Appliance (OVA) installations that could allow unauthorized `root` access. 

The security patch removes unnecessary system accounts during setup and strengthens overall system security. 

!!! warning "Immediate action required: SSH access vulnerability"
    If you're running PMM OVA installations version 2.38 or higher make sure to upgrade immediately to version 2.44.0-1.

Required actions:

- Upgrade to PMM 2.44.0-1
- Change all service credentials
- Review access logs

24/7 support is available through Percona's technical support channels for any assistance needed during the upgrade process.

For detailed upgrade instructions, see the [2.44.0.1 Release Notes](
https://docs.percona.com/percona-monitoring-and-management/2/release-notes/2.44.0.1.html).

For PMM 3.0.0 users, an update to [PMM  3.0.0-1](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_1.html) is available.


