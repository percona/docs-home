---
date: 2026-10-27
description: >
  Percona Server for MongoDB 7.0.45-24, 8.0.34-15, and 8.3.13-4 have been released on October 21, 22, and 27, 2026, respectively.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 7.0.45-24, 8.0.34-15, and 8.3.13-4 have been released

<!-- more -->

The latest Percona Server for MongoDB releases are:

| Release | Release date | Release notes |
| --- | --- | --- |
| 7.0.45-24 | October 21, 2026 | [7.0.45-24 release notes](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.45-24.html){:target="_blank"} |
| 8.0.34-15 | October 22, 2026 | [8.0.34-15 release notes](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.34-15.html){:target="_blank"} |
| 8.3.13-4 | October 27, 2026 | [8.3.13-4 release notes](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.13-4.html){:target="_blank"} |

**Percona Server for MongoDB 8.3 is now generally available.** Version 8.3.13-4 moves the 8.3 series from technical preview to production support.

These releases include improvements and security fixes from their corresponding MongoDB Community Edition versions. They also fix a failure when streaming backups to Google Cloud Storage through its S3-compatible API.

If you install from binary tarballs, download MongoDB Database Tools separately: they are no longer bundled in the server tarball. RPM and DEB installations continue to install these tools as before.

For PSMDB 8.3.13-4, review the [known issue affecting file copy based initial sync after an unclean shutdown](https://docs.percona.com/percona-server-for-mongodb/8.3/release_notes/8.3.13-4.html#known-issues){:target="_blank"} before upgrading.

Follow the minor upgrade guide for your release series: [7.0](https://docs.percona.com/percona-server-for-mongodb/7.0/install/minor-upgrade.html){:target="_blank"}, [8.0](https://docs.percona.com/percona-server-for-mongodb/8.0/install/minor-upgrade.html){:target="_blank"}, or [8.3](https://docs.percona.com/percona-server-for-mongodb/8.3/install/minor-upgrade.html){:target="_blank"}.
