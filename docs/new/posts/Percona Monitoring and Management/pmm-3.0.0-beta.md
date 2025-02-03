---
date: 2024-11-22
description: >
  Percona Monitoring and Management 3.0.0 Beta has been released on Friday, November 22, 2024.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.0.0 Beta has been released

<!-- more -->

[Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/3/index.html){:target="_blank"} 3.0.0 Beta, available since Friday, November 22, 2024. This release brings important enhancements to security, stability, and user experience. 

Get hands-on with PMM 3.0.0 Beta by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart.html){:target="_blank"}.

Here's a summary of the main changes in this release:

- [Rootless deployments](https://docs.percona.com/percona-monitoring-and-management/3/setting-up/index.html#set-up-pmm-server){:target="_blank"}: Now supported across Podman, Helm, Docker, Virtual Appliance, and AWS deployments for enhanced security
- [Sensitive data encryption](https://docs.percona.com/percona-monitoring-and-management/3/pmm-admin/security/data_encryption.html){:target="_blank"}: All database credentials, AWS keys, and certificates are now automatically encrypted.
- [Enhanced API authentication](https://docs.percona.com/percona-monitoring-and-management/3/api/authentication.html){:target="_blank"}: Transition to Grafana service accounts from API keys for better security and audit capabilities.
- [Unified container architecture](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#containerized-pmm-architecture-for-ami-and-ovf-deployments){:target="_blank"}: AMI and OVF deployments now use containerized architecture with Podman.
- [Streamlined upgrades](https://docs.percona.com/percona-monitoring-and-management/3/pmm-upgrade/ui_upgrade.html){:target="_blank"}: New container-based upgrade system replaces RPM updates for more reliable updates.
- [ARM support](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#official-arm-support-for-pmm-client){:target="_blank"}: Official support for ARM architecture on PMM Client, graduating from experimental status.
- [Flexible monitoring](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#flexible-monitoring-configurations){:target="_blank"}: New UI-driven database monitoring setup with distributed monitoring capabilities.
- [Enhanced navigation](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#improved-navigation){:target="_blank"}: Revamped header with improved search and reorganized menus.
- [Simplified AWS installation](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/aws/aws.html){:target="_blank"}: Streamlined installation process with immediate login access.
- [Grafana 11.1.8 integration](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#improved-ux-with-grafanas-latest-release){:target="_blank"}: Latest Grafana features with improved navigation and alerting workflow.
- [PostgreSQL enhancements](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#added-monitoring-support-for-default-postgresql-database){:target="_blank"}: Full monitoring support for default postgres database.
- [MongoDB support](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#tech-preview-support-for-psmdb-and-community-mongodb-80){:target="_blank"}: [Tech Preview] Support for MongoDB 8.0 and PSMDB 8.0.
- [Increased MongoDB query length limit to 4096 characters](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#increased-query-length-limit-for-mongodb-in-qan){:target="_blank"}.
- [Enhanced MySQL SlowLog query identification with extended query ID length](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html#enhanced-mysql-slowlog-query-identification){:target="_blank"}.

You can find the full list of changes in the [release notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0_Beta.html){:target="_blank"}.


