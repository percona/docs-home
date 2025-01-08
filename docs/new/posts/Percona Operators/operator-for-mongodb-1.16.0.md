---
date: 2024-05-24
description: >
  Percona Operator for MongoDB 1.16.0 has been released on Friday, May 24, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.16.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.16.0 has been released on Friday, May 24, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Automated volume resizing](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.16.0.html#automated-volume-expansion){:target="_blank"} allows the Operator to detect if the storage usage on the PVC reaches a certain threshold, and trigger the PVC resize
* [Physical Backups and Restores](https://docs.percona.com/percona-operator-for-mongodb/backups.html#physical){:target="_blank"} feature has graduated to general availability
* [MongoDB 7 support](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.16.0.html#support-for-mongodb-7){:target="_blank"} is now available within the Operator
* [Officially certified images for ARM](https://docs.percona.com/percona-operator-for-mongodb/images.html){:target="_blank"} are now available for the Operator, as well as Percona Server for MongoDB and Percona Backup for MongoDB
 
[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.16.0.html#deprecation-and-removal){:target="_blank"} are the following ones:

* Starting from now, `allowUnsafeConfigurations` Custom Resource option is deprecated in favor of a number of options under the [unsafeFlags](https://docs.percona.com/percona-operator-for-mongodb/operator.html#operator-unsafeflags-section){:target="_blank"} subsection
* MongoDB 4.4 support in the Operator has reached its end-of-life. Starting from now Percona [will not provide](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.16.0.html#deprecation-and-removal){:target="_blank"} officially certified images for it

Learn more in Percona Operator for MongoDB 1.16.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.16.0.html){:target="_blank"}.
