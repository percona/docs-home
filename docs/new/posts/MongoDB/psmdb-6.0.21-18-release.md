---
date: 2025-04-22
description: >
  Percona Server for MongoDB 6.0.21-18 has been released on April 22, 2025.
authors: [nastena1606]
categories:
  - MongoDB
tags:
  - Percona Server for MongoDB
---

# Percona Server for MongoDB 6.0.21-18 has been released

<!-- more -->

[Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/6.0/index.html){:target="_blank"} 6.0.21-18 has been released on April 22, 2025.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-server-for-mongodb/6.0/install/index.html){:target="_blank"}. 

This release provides the following improvements:

* Now you now longer have to modify the configuration file to migrate from MongoDB Advanced to Percona Server for MongoDB if you use the data-at-rest encryption with KMIP. We have improved compatibility between these solutions to simplify this process for you. 

* Better user experience with improved audit logging:

   * Keep your system clean by having an audit log file only if you explicitly defined it as a destination in the logging configuration
   * Regardless whether you use a default or a custom path for an audit log file, Percona Server for MongoDB checks if it can write to this path to ensure that logging information is written and available

* Improve observability of your Percona Server for MongoDB Pro via binaries that include debug symbols. These binaries are added to Percona Server for MongoDB Pro packages and tarballs and make it compatible for runtime instrumentation to collect more detailed telemetry data. By integrating Percona Server for MongoDB Pro with advanced monitoring tools that use debug symbols, you receive detailed diagnostic data and logs.

* Compatibility with Amazon Linux 2023. Because of the way Amazon Linux updates their libraries, Percona Server for MongoDB 6.0.21-18 is compatible only with Amazon Linux 2023.7.x and won't work on Amazon Linux 2023.6.x and older. 

   To upgrade to 6.0.21-18, make sure that you run Amazon Linux 2023.7.x. Use the [update instructions :octicons-link-external-16:](https://docs.aws.amazon.com/linux/al2023/ug/updating.html){:target="_blank"}.

Learn more about this release in Percona Server for MongoDB 6.0.21-18 [release notes](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.21-18.html){:target="_blank"}.

