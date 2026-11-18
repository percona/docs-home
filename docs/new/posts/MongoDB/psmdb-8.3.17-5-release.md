---
date: 2026-11-18
description: >
  Percona Server for MongoDB 8.3.17-5 has been released on November 18, 2026, with security fixes and a backup command deprecation.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 8.3.17-5 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/8.3/){:target="_blank"} 8.3.17-5 has been released on November 18, 2026.

This release includes upstream security fixes and improves AWS IAM authentication for assumed roles in non-commercial AWS partitions. Percona strongly recommends upgrading to 8.3.17-5.

- **Security fixes.** The release addresses critical and high-severity vulnerabilities inherited from upstream MongoDB, including a use-after-free during replica set primary catch-up and issues affecting authorization and server availability. See the release notes for affected configurations and platform-specific scope.
- **AWS IAM authentication.** The server now preserves the AWS partition when converting an STS assumed-role ARN to the IAM role ARN used to match a user in `$external`, including in GovCloud and China.
- **Backup command deprecation.** The `createBackup` command still works in 8.3, but each call now adds a deprecation warning to the response and server log. Before upgrading to 9.0, where the command will be removed, switch your backup workflow to [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"}. See the [PBM quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"} to get started.

Before upgrading in GovCloud, China, or ISO partitions, review existing `$external` users named with IAM role ARNs: all sessions of the matching role can now authenticate as that user. Users named with full STS assumed-role session ARNs no longer match. Replace these per-session users with appropriately authorized IAM role-ARN users.

Review the [known issue affecting file-copy-based initial sync after an unclean shutdown](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.17-5.html#known-issues){:target="_blank"} before upgrading.

Follow the [minor upgrade guide](https://docs.percona.com/percona-server-for-mongodb/8.3/install/minor-upgrade.html){:target="_blank"}.

Learn more in the [8.3.17-5 release notes](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.17-5.html){:target="_blank"}.

