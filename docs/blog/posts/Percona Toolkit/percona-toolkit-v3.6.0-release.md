---
date: 2024-06-12
description: >
  Percona Toolkit v3.6.0 has been released on Wednesday, June 12, 2024.
authors: [patrickbirch]
categories:
  - Percona Toolkit
tags:
  - Percona Toolkit
---

# Percona Toolkit v3.6.0 has been released

<!-- more -->

[Percona Toolkit v3.6.0](https://docs.percona.com/percona-toolkit/){:target="_blank"} has been released on Wednesday, June 12, 2024.

This version has the following new features:

* Port improved pt-pmp (Thanks to Alexey Stroganov for the contribution)

* Adds –where param to pt-online-schema-change

* Resume pt-online-schema-change if interrupted

This version has the following improvements:

* Added support for operf if present, and if `CMD_OPCONTROL` is not set (Thanks to Fernando Ipar for the contribution)

* Adds the CPU cache configuration info to pt-summary (Thanks to Alexey Kopytov for the contribution)

* pt-galera-log-explainer: improvements from feedbacks (Thanks to Yoann La Cancellera for the contribution)

* pt-galera-log-explainer: add custom regexes parameter (Thanks to Yoann La Cancellera for the contribution)

* Fixed a wide character error (Thanks to Satoshi MITANI for the contribution)

* Includes the last inactive check messages on pt-galera-log-explainer (Thanks to Yoann La Cancellera for the contribution)

* pt-k8s-debug-collector needs `psql` in the host node (Thanks to Jobin Augustine for the contribution)

* pt-galera-log-explainer: whois redesign (Thanks to Yoann La Cancellera for the contribution)

* pt-show-grants should use `print_identified_with_as_hex`

* pt-show-grants does not `CREATE USER` (Thanks to Marco Tusa for the contribution)

* Collects the openssl x509 certificate information for each secret

This release also includes fixes.

Learn more in the Percona Toolkit v3.6.0 [release notes](https://docs.percona.com/percona-toolkit/release_notes.html){:target="_blank"}.
