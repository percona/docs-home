---
hide:
- feedback
- navigation
- toc
---

<div class="landing" markdown>
<div class="splash header subpage utilities dark" markdown>

![Percona Lab](assets/percona-utilities.svg)

# Percona Lab projects

This section lists experimental projects created by Perconians and shared with the open-source community.

These projects are typically early-stage tools, research prototypes, or utilities developed to explore new ideas in open-source databases.

</div>
</div>

!!! warning "Disclaimer"

    **Percona-Lab and other repositories listed in this section focus on bringing innovations to the world of open-source databases.**

    These repositories are provided **without warranty or official Percona support**. They are intended for users who want to **experiment, test new ideas, or contribute to early-stage code**.

    Use them at your own risk and carefully evaluate any code or binaries before deploying them in production.

---

## Quick navigation

- [Database extensions](#extensions)
- [Tools and utilities](#tools)
- [Deployment and infrastructure](#deployment)
- [Migration](#migration)

## 🧩 Database extensions {#extensions}

Components that run inside the database engine.

| Project | Database | Description | Managed by |
|---|---|---|---|
| OIDC Validator ([pg_oidc_validator :octicons-link-external-16:](https://github.com/Percona-Lab/pg_oidc_validator)) | PostgreSQL | PostgreSQL library that validates OIDC tokens and supports providers issuing JWT access tokens. | Zsolt Parragi |

---

## 🛠️ Tools and utilities {#tools}

External applications that interact with databases.

| Project | Database | Description | Managed by |
|---|---|---|---|
| github-stat ([github-stat :octicons-link-external-16:](https://github.com/dbazhenov/github-stat)) | MySQL, PostgreSQL, MongoDB | Application for MySQL, PostgreSQL, and MongoDB load simulation with a web interface and database monitoring capabilities. | Daniil Bazhenov |
| Hackorum ([hackorum :octicons-link-external-16:](https://github.com/Percona-Lab/hackorum)) | PostgreSQL | Open-source web application that archives, indexes, and makes the PostgreSQL hackers mailing list easier to read, search, and analyze. | Zsolt Parragi |
| mongodb-log-obfuscator ([mongodb-log-obfuscator :octicons-link-external-16:](https://github.com/zelmario/mongodb-log-obfuscator)) | MongoDB | Obfuscates sensitive data in MongoDB logs and FTDC diagnostic files while preserving structure for analysis and safe sharing. | Zelmar |
| mysql-random-data-generator ([mysql-random-data-generator :octicons-link-external-16:](https://github.com/kedarvj/mysql-random-data-generator)) | MySQL | MySQL tool that automatically detects column types and generates random data to populate tables. **Consider using `random-data-load` for multi-database support.** | Kedar |
| mysqldumpsplitter ([mysqldumpsplitter :octicons-link-external-16:](https://github.com/kedarvj/mysqldumpsplitter)) | MySQL | Utility that splits and extracts databases or tables from mysqldump files with additional processing functionality. | Kedar |
| random-data-load ([random-data-load :octicons-link-external-16:](https://github.com/Percona-Lab/random-data-load)) | MySQL, PostgreSQL | Generates synthetic datasets based on schema, constraints, and cardinality to reproduce and optimize query execution behavior for MySQL and PostgreSQL. | Yoann La Cancellera |
| pg_gather ([pg_gather :octicons-link-external-16:](https://github.com/jobinau/pg_gather)) | PostgreSQL | Collects minimal diagnostic data from PostgreSQL instances and generates an analysis report to identify potential issues. | Jobin Augustine |
| plgm ([percona-load-generator-mongodb :octicons-link-external-16:](https://github.com/Percona-Lab/percona-load-generator-mongodb)) | MongoDB | High-performance load generator written in Go that simulates heavy workloads for both sharded and non-sharded MongoDB clusters. | Daniel Almeida |

---

## 🚀 Deployment and infrastructure {#deployment}

Tools for provisioning or managing database environments.

| Project | Database | Description | Managed by |
|---|---|---|---|
| dbdeployer ([dbdeployer :octicons-link-external-16:](https://github.com/Robertoh98/dbdeployer)) | MySQL | Tool for quickly deploying MySQL database servers. A Go-based redesign of MySQL-Sandbox. | Roberto Garcia de Bem |
| mongo_terraform_ansible ([mongo_terraform_ansible :octicons-link-external-16:](https://github.com/percona/mongo_terraform_ansible)) | MongoDB | Automation toolkit for deploying MongoDB environments using Terraform and Ansible. | — |

---

## 🔄 Migration {#migration}

Tools for moving data between systems.

| Project | Database | Description | Managed by |
|---|---|---|---|
| docMongoStream ([percona-docstreamer :octicons-link-external-16:](https://github.com/Percona-Lab/percona-docstreamer)) | MongoDB | Automated end-to-end tool for migrating data from Amazon DocumentDB to MongoDB. | Daniel Almeida |

---

## Other resources

<div data-resources markdown>

[:material-account-group: Community Website](https://percona.community/)
[:material-forum-outline: Community Forum](https://forums.percona.com/)
[:percona-logo: Get a Percona Expert](https://www.percona.com/services/consulting)
[:material-newspaper-variant-outline: Community Blog](https://www.percona.com/blog/)

</div>
<br>

<!-- >
## Contributing

To add a new project:
- Place it in the appropriate section
- Keep entries alphabetically ordered
- Provide a concise description (1–2 lines)
- Specify supported database(s)
- Specify the name of the author
-->
