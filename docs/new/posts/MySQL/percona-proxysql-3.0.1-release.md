---
date: 2025-09-17
description: >
  ProxySQL 3.0.1 has been released on Wednesday, September 17, 2025.
authors: [patrickbirch]
categories:
  - MySQL
tags:
  - ProxySQL
---

# ProxySQL 3.0.1 has been released

<!-- more -->

[ProxySQL](https://docs.percona.com/proxysql/){:target="_blank"} 3.0.1 has been released on Wednesday, September 17, 2025.

Try it out using the [Installation guide](https://docs.percona.com/proxysql/install-v3.html){:target="_blank"}.

This version updates ProxySQL to version 3.0.1. 

ProxySQL now uses a dynamically linked version of the system's OpenSSL library instead of a statically linked one. This change allows ProxySQL to more easily use the most up-to-date and secure versions of OpenSSL already present on the host system. Additionally, ProxySQL now logs a warning message if it detects a problematic or outdated OpenSSL version, alerting administrators to potential security risks.

A bug has been fixed where the `syncusers` command would delete and recreate users when a password hash difference was detected, which incorrectly removed the `default_schema` property. This operation now correctly preserves the property. We thank George Mess for reporting this issue and contributing a patch.

ProxySQL 3 has removed support for several distributions ([#4749](https://github.com/sysown/proxysql/pull/4749)) due to them being officially past their end-of-life or lacking native support for OpenSSL 3.0, a library required for modern security features.

| Distribution | Reason for Removal | EOL Date / Notes |
| :--- | :--- | :--- |
| CentOS 8 | Past official EOL | December 31, 2021 |
| Debian 10 (Buster) | Does not ship with OpenSSL 3.0 | LTS ended June 30, 2024 |
| Debian 11 (Bullseye) | Does not include OpenSSL 3.0 | Currently in LTS until Aug 2026 |
| Ubuntu 18.04 (Bionic Beaver) | EOL and does not support OpenSSL 3.0 | EOL May 2023 |
| Ubuntu 20.04 (Focal Fossa) | Does not ship with OpenSSL 3.0 | EOL April 2025 |

Learn more in ProxySQL 3.0.1 [release notes](https://docs.percona.com/proxysql/3.0.1.html){:target="_blank"}.

