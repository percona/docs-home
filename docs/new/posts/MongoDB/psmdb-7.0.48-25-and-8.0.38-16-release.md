---
date: 2026-11-13
description: >
  Percona Server for MongoDB 7.0.48-25 and 8.0.38-16 have been released on November 13, 2026.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.48-25 and 8.0.38-16 have been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/){:target="_blank"} 7.0.48-25 and 8.0.38-16 have been released on November 13, 2026.

These releases include upstream security fixes and improve AWS IAM authentication for assumed roles in non-commercial AWS partitions, including GovCloud and China. Percona strongly recommends upgrading to the latest release in your series.

- **Security fixes.** Both releases address critical and high-severity vulnerabilities inherited from upstream MongoDB, including a use-after-free during replica set primary catch-up and issues affecting authorization and server availability. See the release notes for the affected configurations and platform-specific scope.
- **AWS IAM authentication.** The server now preserves the AWS partition when converting an STS assumed-role ARN to the IAM role ARN used to match a user in `$external`.

Before upgrading in GovCloud, China, or ISO partitions, review existing `$external` users named with IAM role ARNs: all sessions of the matching role can now authenticate as that user. Users named with full STS assumed-role session ARNs no longer match. Replace these per-session users with appropriately authorized IAM role-ARN users.

| Release | Release date | Release notes |
| --- | --- | --- |
| 7.0.48-25 | November 13, 2026 | [7.0.48-25 release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.48-25.html){:target="_blank"} |
| 8.0.38-16 | November 13, 2026 | [8.0.38-16 release notes](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.38-16.html){:target="_blank"} |

Follow the minor upgrade guide for your release series: [7.0](https://docs.percona.com/percona-server-for-mongodb/7.0/install/minor-upgrade.html){:target="_blank"} or [8.0](https://docs.percona.com/percona-server-for-mongodb/8.0/install/minor-upgrade.html){:target="_blank"}.
