---
date: 2024-11-22
description: >
  Percona Monitoring and Management 3.0.0 has been released on Friday, November 22, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.0.0 Beta has been released

<!-- more -->

[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} 3.0.0 Beta, available since Friday, November 22, 2024. This release brings important enhancements to security, stability, and user experience. 

Get hands-on with PMM 3.0.0 Beta by setting up your instance using our [quickstart guide](https://pmm-doc-3-0.onrender.com/quickstart.html) {:target="_blank"} or explore PMM through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.

Here's a summary of the main changes in this release:

- Rootless deployments: Now supported across Podman, Helm, Docker, Virtual Appliance, and AWS deployments for enhanced security.
- Sensitive data encryption: All database credentials, AWS keys, and certificates are now automatically encrypted.
- Enhanced API authentication: Transition to Grafana service accounts from API keys for better security and audit capabilities.
- Unified container architecture: AMI and OVF deployments now use containerized architecture with Podman.
- Streamlined upgrades: New container-based upgrade system replaces RPM updates for more reliable updates.
- ARM support: Official support for ARM architecture on PMM Client, graduating from experimental status.
- Flexible monitoring: New UI-driven database monitoring setup with distributed monitoring capabilities.
- Enhanced Navigation: Revamped header with improved search and reorganized menus.
- Simplified AWS Installation: Streamlined installation process with immediate login access.
- Grafana 11.1.8 integration: Latest Grafana features with improved navigation and alerting workflow.
- PostgreSQL enhancements: Full monitoring support for default postgres database.
- MongoDB Support: [Tech Preview] Support for MongoDB 8.0 and PSMDB 8.0.
- Increased MongoDB query length limit to 4096 characters.
- Enhanced MySQL SlowLog query identification with extended query ID length.

You can find the full list of changes in the [release notes](https://pmm-doc-3-0.onrender.com/release-notes/3.0.0_Beta.html){:target="_blank"}.


