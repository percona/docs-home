---
date: 2024-11-22
description: >
  PMM now encrypts all sensitive information stored in its database. This includes usernames, passwords, AWS keys, Azure credentials, and TLS/SSL certificates, significantly enhancing the security of your monitoring environment. 

authors: [catalinaadam]
categories:
  - Percona Monitoring and Management
tags:
  - Percona Monitoring and Management
---

# Encryption of sensitive data in Percona Monitoring and Management

<!-- more -->

Get hands-on with [Percona Monitoring and Management](https://docs.percona.com/percona-monitoring-and-management/index.html){:target="_blank"} by setting up your instance using our [quickstart guide](https://docs.percona.com/percona-monitoring-and-management/3/quickstart/quickstart.html){:target="_blank"}, or explore the new changes through our [live demo environment](https://pmmdemo.percona.com){:target="_blank"}.


Plaintext passwords and credentials are among the top ten security risks identified by OWASP (Open Web Application Security Project).

To address this risk, PMM now encrypts all sensitive information stored in its database. This includes usernames, passwords, AWS keys, Azure credentials, and TLS/SSL certificates, significantly enhancing the security of your monitoring environment.

Even though we recommend minimal privileges for monitoring user accounts, you can rest assured that the sensitive data is protected! 

Learn more in [PMM 3.0.0 Beta release notes](https://pmm-doc-3-0.onrender.com/release-notes/3.0.0_Beta.html#encryption-of-sensitive-data){:target="_blank"}.
