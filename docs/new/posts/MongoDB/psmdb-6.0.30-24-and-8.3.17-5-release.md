---
date: 2026-11-19
description: >
  Percona Server for MongoDB 6.0.30-24 and 8.3.17-5 were released on November 19 and November 18, 2026, respectively.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 6.0.30-24 and 8.3.17-5 have been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/){:target="_blank"} 6.0.30-24 was released on November 19, 2026, following 8.3.17-5 on November 18, 2026.

Both releases include critical and high-severity security fixes inherited from upstream MongoDB. Percona strongly recommends upgrading to the latest release in your series.

| Release | Release date | Release notes |
| --- | --- | --- |
| 6.0.30-24 | November 19, 2026 | [6.0.30-24 release notes](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.30-24.html){:target="_blank"} |
| 8.3.17-5 | November 18, 2026 | [8.3.17-5 release notes](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.17-5.html){:target="_blank"} |

## Security fixes in 6.0.30-24

This release addresses two upstream vulnerabilities, also fixed in 8.3.17-5:

- **Replica set primary catch-up.** A use-after-free could allow unauthenticated requests to crash a server or, under certain conditions, execute arbitrary code. It affects replica set members, including shard and config server members, but not standalone `mongod` instances.
- **Memory exhaustion.** An unauthenticated user with network access could send read requests for an unreachable point in time. Internal wait records could accumulate after those requests ended, exhausting server memory and causing a denial of service.

## Additional changes in 8.3.17-5

Version 8.3.17-5 includes additional upstream security fixes, improves AWS IAM authentication for assumed roles in non-commercial AWS partitions, and deprecates the `createBackup` command.

The `createBackup` command still works in 8.3, but each call now adds a warning to the response and server log. Before upgrading to 9.0, where the command will be removed, switch your backup workflow to [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html){:target="_blank"}. See the [PBM quickstart guide](https://docs.percona.com/percona-backup-mongodb/installation.html){:target="_blank"}.

Before upgrading to 8.3.17-5 in GovCloud, China, or ISO partitions, review existing `$external` users named with IAM role ARNs: all sessions of the matching role can now authenticate as that user. Users named with full STS assumed-role session ARNs no longer match. Replace these per-session users with appropriately authorized IAM role-ARN users.

For 8.3.17-5, also review the [known issue affecting file-copy-based initial sync after an unclean shutdown](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.17-5.html#known-issues){:target="_blank"} before upgrading.

Follow the minor upgrade guide for your release series: [6.0](https://docs.percona.com/percona-server-for-mongodb/6.0/install/minor-upgrade.html){:target="_blank"} or [8.3](https://docs.percona.com/percona-server-for-mongodb/8.3/install/minor-upgrade.html){:target="_blank"}.
