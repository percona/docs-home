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

# Encryption of sensitive data

<!-- more -->

Plaintext passwords and credentials are among the top ten security risks identified by OWASP (Open Web Application Security Project).

To address this risk, PMM now encrypts all sensitive information stored in its database. This includes usernames, passwords, AWS keys, Azure credentials, and TLS/SSL certificates, significantly enhancing the security of your monitoring environment. Even though we recommend minimal privileges for monitoring user accounts, you can rest assured that the sensitive data is protected! 

Learn more in [PMM 3.0.0 Beta release notes](https://pmm-doc-3-0.onrender.com/release-notes/3.0.0_Beta.html#encryption-of-sensitive-data){:target="_blank"}.

<div data-banner markdown>

## Get expert help { .title }

If you need assistance, visit the community forum for comprehensive and free database knowledge, or contact our Percona Database Experts for professional support and services.

<div class="actions" markdown>

[:material-forum-outline: Community Forum](https://forums.percona.com/){:target="_blank"} [:percona-logo: Get a Percona Expert](https://www.percona.com/about/contact){:target="_blank"}
</div></div>