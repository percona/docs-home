---
date: 2025-06-26
description: >
  Percona Backup for MongoDB 2.10.0 has been released on June 26, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.10.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.10.0 has been released on June 26, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release provides the following features and improvements:

* Ensure your cluster remains operational even if errors occur during a physical restore by [making restores with a fallback directory](https://docs.percona.com/percona-backup-mongodb/features/physical.html/#physical-restores-with-a-fallback-directory){:target="_blank"}. PBM copies the `dbPath` contents to a special fallback directory at the restore start and proceeds with the restore as usual. If an error occurs during the restore, PBM uses the fallback directory contents to roll back the cluster to its pre-restore state. Note that to use this feature you must have enough free disk space on each `mongod` instance to store the `dbPath` contents.

* Improved compatibility with Google Cloud Storage (GCS) by using a native Google Cloud Client library. PBM communicates with GCS both via JSON API and XML API and supports both types of credentials: storage account credentials for JSON API and HMAC keys for XML API requests. The use of a new library resulted in PBM configuration changes which you need to when you upgrade to this PBM version. Read more about these steps in the [documentation](https://docs.percona.com/percona-backup-mongodb/details/gcs.html/#adjust-pbm-configuration-to-use-gcs){:target="_blank"}

* Percona Backup for MongoDB now uses the AWS SDK v2 for Go, which includes the latest features, security updates and improvements. This ensures the secure communication with AWS services.

* Percona Backup for MongoDB is no longer supported on Ubuntu 20.04 (Focal Fossa) as this operating system has reached end of life.
