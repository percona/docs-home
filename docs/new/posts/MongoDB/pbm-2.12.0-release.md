---
date: 2025-11-04
description: >
  Percona Backup for MongoDB 2.12.0 has been released on November 4, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Backup for MongoDB
---

# Percona Backup for MongoDB 2.12.0 has been released

<!-- more -->

[Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"} 2.12.0 has been released on November 4, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} 

This release focuses on improvements to backup storages. It includes new storage types, enhances Azure Blob storage implementation, and fixes issues with S3-compatible storage services. 

Details below:

* Integrate your backup workflows into the Alibaba Cloud ecosystem seamlessly using Alibaba Cloud Object Storage Service (OSS) as the remote backup storage. Authenticate to Alibaba Cloud OSS directly using your AccessKey pair, or ensure compliance with your org's security policies with a full support for Alibaba Cloud's Security Token Service (STS) AssumeRole, which includes automatic security token refresh. This integration empowers teams operating in Asia-Pacific or invested in Alibaba Cloud to adopt PBM better. Read more about Alibaba Cloud OSS support in our [documentation](https://docs.percona.com/percona-backup-mongodb/details/oss.html){:target="_blank"}

* Ensure data upload to Azure Blob storage even during unstable network. You can now control the number of upload retries to Azure in PBM configuration. This enhancement ensures your data reaches its destination—even when the network is unstable or intermittent. Check [PBM configuration file reference](https://docs.percona.com/percona-backup-mongodb/reference/configuration-options.html#microsoft-azure-blob-storage-options){:target="_blank"} for available options.

* Improved usage of custom S3-compatible storage service implementations with a native support for MinIO client library in PBM. To prevent potential compatibility and connectivity issues if anS3-compatible storage service doesn't support Signature Version 4 (SigV4) used in AWS SDK v2, PBM now uses the MinIo Go client and supports a new `minio` storage type in its configuration. If your custom S3-compatible storage is not compatible with AWS SDK v2, consider re-configuring PBM to use the `minio` storage type after the upgrade. Check the [documentation](https://docs.percona.com/percona-backup-mongodb/details/minio.html){:target="_blank"} for steps. Also, be aware of the current known limitation that currently PBM uploads backups in a single thread which may result in slower performance. 

* Deprecation of HMAC keys support for Google Cloud Storage. Google Cloud Storage doesn't support a new Signature Version 4 (SigV4) and only supports SigV2 for HMAC authentication. Signature Version 2 (SigV2) authentication is not recommended because it lacks important security enhancements, is no longer maintained, and can introduce critical reliability issues. To prevent these, HMAC support in PBM is deprecated and will be removed in the release following after April 30, 2026. We strongly recommend migrating to a native GCS connection type [with JSON keys](https://cloud.google.com/iam/docs/keys-create-delete#creating). Refer to the [documentation](https://docs.percona.com/percona-backup-mongodb/details/gcs.html#adjust-pbm-configuration-to-use-gcs){:target="_blank"} for guidance on adjusting PBM configuration to use JSON keys.


