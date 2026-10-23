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

    To report a bug or ask a question, open an issue in the project's GitHub repository.

---

## Quick navigation

<div class="splash-links splash-row">
  <a href="#extensions" class="splash-card">
    <h3>Database extensions</h3>
    <p>Components that run inside the database engine.</p>
  </a>
  <a href="#tools" class="splash-card">
    <h3>Tools and utilities</h3>
    <p>Diagnostics, backup and recovery, and load generation.</p>
  </a>
  <a href="#deployment" class="splash-card">
    <h3>Deployment and infrastructure</h3>
    <p>Tools for provisioning or managing database environments.</p>
  </a>
  <a href="#migration" class="splash-card">
    <h3>Migration</h3>
    <p>Tools for moving data between systems.</p>
  </a>
</div>

Want to add your project? See [Contributing](#contributing).

## 🧩 Database extensions {#extensions}

Components that run inside the database engine.

| Project | Database | Description | Managed by |
|---|---|---|---|
| OIDC Validator ([pg_oidc_validator :octicons-link-external-16:](https://github.com/Percona-Lab/pg_oidc_validator)) | PostgreSQL | PostgreSQL library that validates OIDC tokens and supports providers issuing JWT access tokens. | Zsolt Parragi |

---

## 🛠️ Tools and utilities {#tools}

External applications that interact with databases.

### Diagnostics and monitoring {#diagnostics}

| Project | Database | Description | Managed by |
|---|---|---|---|
| [Big Hole :octicons-link-external-16:](https://github.com/zelmario/Big-hole) | MongoDB | Browser-based, offline viewer for MongoDB FTDC diagnostic data. Plots metrics alongside the mongod log and flags common issues such as ticket exhaustion and cache pressure. Data never leaves your machine. | Zelmar Michelini |
| [mongo-health :octicons-link-external-16:](https://github.com/zelmario/mongo-health) | MongoDB | Collects and retains FTDC data from Atlas and self-managed replica sets, runs hourly health checks, and reports a per-replica-set verdict with supporting evidence. | Zelmar Michelini |
| [mongodb-log-obfuscator :octicons-link-external-16:](https://github.com/zelmario/mongodb-log-obfuscator) | MongoDB | Obfuscates sensitive data in MongoDB logs and FTDC diagnostic files while preserving structure for analysis and safe sharing. | Zelmar Michelini |
| [MongoDB-Log-Plotter :octicons-link-external-16:](https://github.com/zelmario/MongoDB-Log-Plotter) | MongoDB | Python script that parses MongoDB 4.4+ log files and plots slow queries, connections, and errors in an interactive dashboard. | Zelmar Michelini |
| [pg_gather :octicons-link-external-16:](https://github.com/jobinau/pg_gather) | PostgreSQL | Collects minimal diagnostic data from PostgreSQL instances and generates an analysis report to identify potential issues. | Jobin Augustine |

### Backup and recovery {#backup}

| Project | Database | Description | Managed by |
|---|---|---|---|
| [mongorewind :octicons-link-external-16:](https://github.com/zelmario/mongorewind) | MongoDB | Terminal app that records inserts, updates, and deletes in a MongoDB replica set or sharded cluster and rolls them back, newest first. Resets test environments without a full restore. | Zelmar Michelini |
| [mysqldumpsplitter :octicons-link-external-16:](https://github.com/kedarvj/mysqldumpsplitter) | MySQL | Utility that splits and extracts databases or tables from mysqldump files with additional processing functionality. | Kedar Vaijanapurkar |
| [PBM UI :octicons-link-external-16:](https://github.com/zelmario/pbm-ui) | MongoDB | Web interface for Percona Backup for MongoDB that manages backups, restores, point-in-time recovery, configuration, and logs for replica sets. | Zelmar Michelini |

### Data and load generation {#load-generation}

| Project | Database | Description | Managed by |
|---|---|---|---|
| [github-stat :octicons-link-external-16:](https://github.com/dbazhenov/github-stat) | MySQL, PostgreSQL, MongoDB | Application for MySQL, PostgreSQL, and MongoDB load simulation with a web interface and database monitoring capabilities. | Daniil Bazhenov |
| [mysql-random-data-generator :octicons-link-external-16:](https://github.com/kedarvj/mysql-random-data-generator) | MySQL | MySQL tool that automatically detects column types and generates random data to populate tables. **Consider using `random-data-load` for multi-database support.** | Kedar Vaijanapurkar |
| plgm ([percona-load-generator-mongodb :octicons-link-external-16:](https://github.com/Percona-Lab/percona-load-generator-mongodb)) | MongoDB | High-performance load generator written in Go that simulates heavy workloads for both sharded and non-sharded MongoDB clusters. | Daniel Almeida |
| [random-data-load :octicons-link-external-16:](https://github.com/Percona-Lab/random-data-load) | MySQL, PostgreSQL | Generates synthetic datasets based on schema, constraints, and cardinality to reproduce and optimize query execution behavior for MySQL and PostgreSQL. | Yoann La Cancellera |

### Other utilities {#other-utilities}

| Project | Database | Description | Managed by |
|---|---|---|---|
| [Hackorum :octicons-link-external-16:](https://github.com/Percona-Lab/hackorum) | PostgreSQL | Open-source web application that archives, indexes, and makes the PostgreSQL hackers mailing list easier to read, search, and analyze. | Zsolt Parragi |

---

## 🚀 Deployment and infrastructure {#deployment}

Tools for provisioning or managing database environments.

| Project | Database | Description | Managed by |
|---|---|---|---|
| [anydbver :octicons-link-external-16:](https://github.com/ihanick/anydbver) | MySQL, PostgreSQL, MongoDB | Creates local multi-node clusters of exact Percona and upstream database versions using Docker containers, with optional Kubernetes deployment via K3d. A [fork :octicons-link-external-16:](https://github.com/zelmario/anydbver) is also maintained. | Nickolay Ihalainen (author), Zelmar Michelini (fork) |
| [dbdeployer :octicons-link-external-16:](https://github.com/Robertoh98/dbdeployer) | MySQL | Tool for quickly deploying MySQL database servers. A Go-based redesign of MySQL-Sandbox. | Roberto Garcia de Bem |
| [mongo_terraform_ansible :octicons-link-external-16:](https://github.com/percona/mongo_terraform_ansible) | MongoDB | Automation toolkit for deploying MongoDB environments using Terraform and Ansible. | Ivan Groenewold |

---

## 🔄 Migration {#migration}

Tools for moving data between systems.

| Project | Database | Description | Managed by |
|---|---|---|---|
| docMongoStream ([percona-docstreamer :octicons-link-external-16:](https://github.com/Percona-Lab/percona-docstreamer)) | MongoDB | Automated end-to-end tool for migrating data from Amazon DocumentDB to MongoDB. | Daniel Almeida |

---

## Contributing {#contributing}

To add a project to this page, open [a pull request](https://github.com/percona/docs-home/pulls) that:

- Places the project in the appropriate section
- Keeps entries alphabetically ordered
- Provides a concise description (1–2 lines)
- Specifies the supported database(s)
- Specifies the name of the author or maintainer

---

## Other resources

<div data-resources markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/)
[:material-newspaper-variant-outline: The Percona Database Performance Blog](https://www.percona.com/blog/)
[:percona-logo: Get a Percona Expert](https://www.percona.com/services/consulting)
[:material-account-group: Community Website](https://percona.community/)
[:material-newspaper-variant-outline: Community Blog](https://percona.community/blog/)

</div>
<br>
