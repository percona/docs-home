---
date: 2025-02-19
description: >
  Percona Backup for MongoDB 2.9.0 has been released on February 19, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.9.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.9.0 has been released on February 19, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Added support for Amazon Linux 2023 simplifies the PBM deployment on AWS. You can safely run PBM on AL23 to build a secure, stable, high-performance environment for developing and running cloud applications, with seamless integration with various AWS services and development tools. 

* [Centralized management of `pbm-agent` setup using the configuration file](https://docs.percona.com/percona-backup-mongodb//manage/start-agent-with-config.html){:target="_blank"}. If you feel more comfortable working with configuration files rather than environment variables, this is the way to go for you. Specify the MongoDB connection URI, the custom log path and the number of parallel workers for a backup and start `pbm-agent` using this file. This helps you keep all your `pbm-agent` setup in a single place and simplifies its management.  

* Improved security for Docker images. The new Universal Base Image (UBI) version 9 base image includes includes the latest security fixes and makes PBM Docker image compliant with the Red Hat certification. This ensures the seamless work of containers on Red Hat OpenShift Container Platform.


