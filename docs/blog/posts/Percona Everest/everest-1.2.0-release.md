---
date: 2024-10-01
description: >
  Percona Everest 1.2.0 has been released on Monday, October 01, 2024.
authors: [rasika-chivate]
categories:
  - Percona Everest
tags:
  - Percona Everest
---

# Percona Everest 1.2.0 has been released

<!-- more -->

[Percona Everest](https://docs.percona.com/everest/index.html){:target="_blank"} 1.2.0 has been released on Monday, October 01, 2024. 

Try it out using our [Quickstart guide](https://docs.percona.com/everest/quickstart-guide/quick-install.html){:target="_blank"}.

Here's a brief overview of what's been added in Percona Everest 1.2.0:

- [Role-based access control (RBAC)](https://docs.percona.com/everest/administer/rbac.html){:target="_blank"}: Percona Everest introduces Role-Based Access Control (RBAC), which regulates resource access for better management and security.

    With RBAC, only authorized individuals can access specific resources or perform certain actions based on their assigned roles. This method improves security by minimizing the risk of unauthorized access and helps manage permissions more efficiently across Percona Everest.

- [Breaking API changes](https://docs.percona.com/everest/api_rbac.html){:target="_blank"}: Percona Everest introduces breaking changes to the API for monitoring-instances and backup-storages resources.

- [Operator upgrades](https://docs.percona.com/everest/upgrade_operators.html?h=operator){:target="_blank"}: Due to limitations with the Operator Lifecycle Manager (OLM), all the database operators are now concurrently upgraded with their components across any namespace. The upgrade process is easily accomplished using our intuitive UI.

- Supported operators: Percona Everest now supports PostgreSQL operator version 2.4.1 MySQL operator version 1.15.0.

Explore the new features, improvements, bug fixes, and known issues in Percona Everest 1.3.0 [release notes](https://docs.percona.com/everest/release-notes/Percona-Everest-1.3.0-%282024-11-18%29.html){:target="_blank"}.