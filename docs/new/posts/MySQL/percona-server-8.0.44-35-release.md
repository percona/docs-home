---
date: 2025-11-27
description: >
  Percona Server for MySQL 8.0.44-35 has been released on Thursday, November 27, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - Percona Server for MySQL
---

# Percona Server for MySQL 8.0.44-35 has been released

<!-- more -->

[Percona Server for MySQL 8.0.44-35](https://docs.percona.com/percona-server/8.0/){:target="_blank"} has been released on Thursday, November 27, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server/8.0/quickstart-overview.html){:target="_blank"}.

Percona Server for MySQL 8.0.44-35 includes all the features and bug fixes available in the MySQL 8.0.44 Community Edition in addition to enterprise-grade features developed by Percona.

Percona has consolidated its build offerings. The Pro builds are no longer required, and all features have been merged into the main open source Community release.

* Adds the `performance_schema.account_failed_login_lock_status` table, which lists user accounts that have been temporarily locked after exceeding the failed‑login limit.

* During slow‑query‑log rotation the server attempts to write to the base file `slow.log` (which isn't created), raises an error - `errno 2 – No such file or directory`, but the logs are written with numeric suffixes (for example, `slow.log.000087`) that obey the configured size and file‑count limits.

* The server’s estimate for how many rows fit in one index leaf (`guess_rec_per_key()`) uses two numbers: `used_keyparts` (the parts actually stored in the index) and `user_defined_key_parts` (the parts the user declared).
If these two counts differ, the formula calculates the wrong capacity, leading to inaccurate index‑size estimates.

Learn more in Percona Server for MySQL 8.0.44-35 [release notes](https://docs.percona.com/percona-server/8.0/release-notes/8.0.44-35.html){:target="_blank"}.