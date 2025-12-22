---
date: 2025-12-22
description: >
  Percona Server for MySQL 8.4.7-7 has been released on Monday, December 22, 2025.
authors: [alina-derkach-oaza]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.4.7-7 has been released

<!-- more -->

[Percona Server for MySQL 8.4.7-7](https://docs.percona.com/percona-server/8.4/index.html){:target="_blank"} has been released on Monday, December 22, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.4/quickstart-overview.html){:target="_blank"}.

### Percona Server for MySQL 8.4.7-7

* Announcement – Discontinuation of the Percona PRO Program

  Percona has consolidated its build offerings. The Pro builds are no longer required. All features from the Percona Server for MySQL 8.0.x Pro build series have been merged into the main open source Community release. [FIPS-capable binaries](https://docs.percona.com/percona-server/8.4/fips.html) are included in all builds starting with this release. The FIPS mode remains off by default and must be enabled via [OS/OpenSSL configuration](https://docs.percona.com/percona-server/8.4/fips.html#prerequisites).

* The audit log plugin has been reintroduced in Percona Server for MySQL 8.4. However, it is already marked as deprecated and is planned for removal in a future release. This deprecation is due to the availability of the [audit log filter component](https://docs.percona.com/percona-server/8.4/audit-log-filter-overview.html), which is the recommended replacement. Users should migrate to this component, which provides equivalent functionality with enhanced flexibility, performance, and filtering capabilities, ensuring continued support for auditing and compliance requirements.

### MySQL 8.4.7

Improvements and bug fixes introduced by Oracle for MySQL 8.4.7 and included in Percona Server for MySQL are the following:

* Fixed an issue where parallel scan thread creation could fail, causing assertion failures when falling back to single-thread mode. (Bug #38325137)

* Fixed an issue where virtual index rollback could fail on 32-bit builds of MySQL Server under certain circumstances. (Bug #38167527)

* Fixed an issue where very large buffer pools could require excessive memory chunks per instance, potentially causing allocation failures. The allocation is now validated to ensure proper memory allocation. (Bug #37994397)

* Fixed an issue where assertion failures could occur due to data size and bounds mismatches during DDL file operations. (Bug #37882398)

* Fixed an issue related to modifying the internal Full-Text Search (FTS) configuration. (Bug #37792010)

* Fixed an issue related to virtual indexes. (Bug #37602657)

* Fixed an issue where confusing warning messages could appear when row sizes exceeded maximum allowed limits with `innodb_strict_mode=OFF`, such as during table selection or column dropping operations. Error messages have been improved for clarity. (Bug #37003342, Bug #36768046, Bug #36867372)

Find the complete list of bug fixes and changes in the [MySQL 8.4.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-7.html){:target="_blank"}.

## Packaging and build notes

* Percona Server for MySQL 8.4 adds support for Debian 13.

* Percona Server for MySQL 8.4 has ended support for Ubuntu 20.04.

## Known limitation

MySQL Shell is not available as a prebuilt package for Debian 11 (Bullseye) in the Percona APT repository. Recent MySQL Shell releases are built with GNU Compiler Collection (GCC) 11 or later, while Debian 11 ships with GCC 10, making these binaries incompatible.

Learn more in Percona Server for MySQL 8.4.7-7 [release notes](https://docs.percona.com/percona-server/8.4/release-notes/8.4.7-7.html){:target="_blank"}.

