---
date: 2024-09-09
description: >
  Percona Operator for MongoDB 1.17.0 has been released on Monday, September 9, 2024.
authors: [fiowro]
categories:
  - Percona Operators
tags:
  - Percona Operator for MongoDB
---

# Percona Operator for MongoDB 1.17.0 has been released

<!-- more -->

[Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/){:target="_blank"} 1.17.0 has been released on Monday, September 9, 2024.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-mongodb/quickstart.html){:target="_blank"}.

New features and improvements introduced by these release include:

* [Declarative user management](https://docs.percona.com/percona-operator-for-mongodb/users.html#unprivileged-users){:target="_blank"} (it has a technical preview) makes it possible to create and manage users via the Custom Resource
* [Logging improvements](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.17.0.html#liveness-check-improvements){:target="_blank"} related to the liveness checks allow getting more information for debugging, and make these probes logs persist on failures to allow further examination

[Important changes in the existing functionality](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.17.0.html#deprecation-rename-and-removal){:target="_blank"} ate the following ones:

* Finalizers [were renamed](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.17.0.html#deprecation-rename-and-removal){:target="_blank"} to contain fully qualified domain names to comply with the Kubernetes standards
* The [psmdb-db Helm chart](https://github.com/percona/percona-helm-charts/tree/main/charts/psmdb-db) parameter for defining system users is renamed from `users` to `systemUsers`

Learn more in Percona Operator for MongoDB 1.17.0 [release notes](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.17.0.html){:target="_blank"}.
