---
date: 2025-01-30
description: >
  Percona Monitoring and Management 3.0.0 has been released on Friday, January 30, 2025.
authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Percona Monitoring and Management 3.0.0 has been released

<!-- more -->


## General Availability of PMM 3.0.0

We're excited to announce the General Availability of PMM 3.0.0, a new major version that introduces a complete architectural overhaul of PMM. 

This milestone delivers major security improvements with rootless deployments, encryption of sensitive data, enhanced stability through containerized architecture, and improved user experience with flexible monitoring configurations. 

### Ready to install or migrate to PMM 3?
We provide two installation scripts to help you get started with this new version:

- For new installations, the [Easy-Install script](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/index.html){:target="_blank"} comes with Watchtower pre-configured, enabling one-step PMM setup with automatic updates.
- For existing PMM 2 users, we provide a dedicated [Upgrade script](https://docs.percona.com/percona-monitoring-and-management/3/pmm-upgrade/migrating_from_pmm_2.html#step-2-migrate-pmm-2-server-to-pmm-3){:target="_blank"} that safely migrates your installation to PMM 3 and ensures data is backed up before the upgrade.

For detailed information about all changes and new features, see  the full [release notes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html){:target="_blank"}.

## Key features

### Security enhancements
- [Rootless deployment](https://docs.percona.com/percona-monitoring-and-management/3/setting-up/index.html#set-up-pmm-server){:target="_blank"}: Now supported across Podman, Helm, Docker, Virtual Appliance, and AWS deployments for enhanced security
- [UI-based upgrades for Podman installations](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/baremetal/podman/index.html){:target="_blank"}: You can now upgrade PMM Server installations running under Podman directly through the **Updates** panel in the UI.
- [Encryption of sensitive data](https://docs.percona.com/percona-monitoring-and-management/3/pmm-admin/security/data_encryption.html){:target="_blank"}: All database credentials, AWS keys and certificates are now automatically encrypted.
- [Enhanced API authentication](https://docs.percona.com/percona-monitoring-and-management/3/api/authentication.html){:target="_blank"}: Transition to Grafana service accounts from API keys for better security and audit capabilities. 
- [Multiple CVE vulnerabilities eliminated through architectural changes](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#cves-eliminated-through-architectural-changes){:target="_blank"}: Legacy component removal (Integrated Alerting and DBaaS) alongside security enhancements has eliminated multiple vulnerabilities, making PMM 3 the most secure release to date.

### Stability improvements
- [Unified containerized architecture for AMI and OVF deployments](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#containerized-pmm-architecture-for-ami-and-ovf-deployments){:target="_blank"}: PMM now uses a unified containerized architecture across all deployment methods. In AMI and OVF environments, PMM components run as Podman-managed containers in rootless mode, eliminating the need for elevated system privileges.

- [More stable and quicker upgrades through container-based updates](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#more-stable-and-quicker-upgrades){:target="_blank"}: PMM 3 transitions from RPM-based updates to a more reliable container-based upgrade system using Watchtower, providing consistent upgrades across all deployment types while maintaining UI-based upgrade convenience. 
- [Reduced container image size](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#reduced-pmm-container-image-size){:target="_blank"} from 3.1GB to 2.6GB

### Improved user experience
- [Streamlined upgrade process](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#new-upgrade-ui){:target="_blank"}: A new **Updates** page under **PMM Configuration** provides centralized visibility of PMM Server and Client versions, with proactive notifications about new releases to help inform upgrade decisions.  

- [Flexible monitoring configurations](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/index.html#connect-services){:target="_blank"}: PMM 3.0 introduces UI-based monitoring setup and distributed monitoring capabilities, allowing database exporters to run on any PMM Client node instead of only on PMM Server.
- [Simplified AWS installation](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-server/aws/aws.html){:target="_blank"}: We’ve simplified AWS installations to match our standard Docker/Podman workflow. 
- [Official ARM support for PMM Client](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#official-arm-support-for-pmm-client){:target="_blank"}: PMM 3 now officially supports ARM architecture, upgrading from its experimental status in PMM 2.43.
- [Improved navigation with Grafana 11.1.8 integration](https://community.grafana.com/t/changelog-updates-in-grafana-11-1-8/134843){:target="_blank"}: PMM's upgrade to Grafana 11.1.8 introduces a streamlined navigation system with an improved header, enhanced search capabilities, and logically grouped tools for better user experience.
- [Enhanced alerting workflow and administration settings](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#improved-alerting-workflow){:target="_blank"}: PMM's updated interface streamlines workflows with dedicated menus for alerts, Grafana administration, and PMM configuration settings.


### Monitoring improvements
- [Full monitoring support for default PostgreSQL database](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#added-monitoring-support-for-default-postgresql-database){:target="_blank"}: PMM now provides full monitoring support for the default postgres database on PostgreSQL instances, with metrics displayed across Query Analytics (QAN).
- [Added Oplog generation rate panel to MongoDB dashboards](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#added-oplog-generation-rate-panel-to-mongodb-dashboards){:target="_blank"}: New **Oplog GB/Hour** panels in MongoDB cluster dashboards provide hourly oplog generation metrics within the **Replication** section.

- [MongoDB Router Summary](https://docs.percona.com/percona-monitoring-and-management/3/reference/dashboards/dashboard-mongodb-router-summary.html){:target="_blank"}: dashboard is now generally available
- [Tech Preview support for MongoDB 8.0](https://www.mongodb.com/docs/manual/release-notes/8.0/){:target="_blank"}: PMM now offers technical preview support for MongoDB 8.0 and Percona Server for MongoDB 8.0, with updated exporters to handle revised metrics structures and renamed metrics.
- [Increased query length limit for MongoDB in QAN](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#increased-query-length-limit-for-mongodb-in-qan){:target="_blank"}: PMM extends MongoDB query length limits to 4096 characters and MySQL SlowLog query IDs to 32 characters, improving Query Analytics accuracy for both databases.

### Breaking changes and deprecations

- [Oracle Enterprise Linux 9 images only](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#oracle-enterprise-linux-9-images-only){:target="_blank"}: PMM 3 now exclusively uses Oracle Enterprise Linux 9 (EL9) as its base system for all images, replacing EL7 to ensure better security updates and compatibility with new technologies.

- [DBaaS functionality moved to Percona Everest](https://www.percona.com/resources/percona-everest){:target="_blank"}: PMM 3 has deprecated its DBaaS functionality in favor of Percona Everest, a cloud-native database platform that offers infrastructure control and monitoring integration while eliminating cloud vendor lock-in.

- [Integrated Alerting deprecated and APIs removed](https://docs.percona.com/percona-monitoring-and-management/3/alert/index.html){:target="_blank"}
- [Breaking API changes including simplified feature toggles](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#breaking-api-changes){:target="_blank"}: PMM's API has been overhauled with simplified identifiers, streamlined feature controls, consistent response fields, and consolidated management endpoints.

- [Grafana Angular support to be discontinued](https://docs.percona.com/percona-monitoring-and-management/3/release-notes/3.0.0.html#grafana-angular-support-discontinuation){:target="_blank"}: PMM is proactively migrating plugins to newer technologies ahead of Grafana's Angular deprecation in version 12 (2025), with recommendations to review and update dashboard plugins.


## Component upgrades
- Grafana upgraded to 11.1.8
- Node Exporter updated to 1.8.2
- ClickHouse Datasource plugin updated
- ClickHouse-go driver upgraded to version 2

