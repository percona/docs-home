---
date: 2025-02-10
description: >
  Percona Monitoring and Management 3.0.0-1 has been released on Monday, February 10, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management  3.0.0-1 has been released

<!-- more -->


## PMM 3.0.0-1 Critical security release
We have released a critical security update addressing a vulnerability in PMM Open Virtual Appliance (OVA) installations that could allow unauthorized `root` access. 

The security patch removes unnecessary system accounts during setup and strengthens overall system security. 

!!! warning "Immediate action required: SSH access vulnerability"
    If you're using PMM 3.0.0 OVA:
    
    - Upgrade IMMEDIATELY to version 3.0.0-1.
    - Change all service credentials
    - Review access logs

24/7 support is available through Percona's technical support channels for any assistance needed during the upgrade process.

For detailed upgrade instructions, see the [3.0.0.1 Release Notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_1.html).

For PMM 2.x users, an update to [PMM  2.44.0-1](https://docs.percona.com/percona-monitoring-and-management/2/release-notes/2.44.0.1.html) is available.