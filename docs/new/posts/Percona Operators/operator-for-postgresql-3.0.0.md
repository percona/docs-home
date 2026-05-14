---
date: 2026-05-15
description: >
  Percona Operator for PostgreSQL 3.0.0 has been released on May 15, 2026.
authors: [nastena1606]
categories:
  - Percona Operators
tags:
  - Percona Operator for PostgreSQL
---

# Percona Operator for PostgreSQL 3.0.0 has been released

<!-- more -->

[Percona Operator for PostgreSQL](https://docs.percona.com/percona-operator-for-postgresql/3.0/){:target="_blank"} 3.0.0 has been released on May 15, 2026.

This version establishes Percona Operator for PostgreSQL as a **hard fork of the [Crunchy PGO project :octicons-link-external-16:](https://github.com/CrunchyData/postgres-operator){:target="_blank"}**, making it fully independent and empowering the Percona team and community to drive and rapidly deliver features and improvements tailored to user needs.

Try it out using the [Quickstart guide](https://docs.percona.com/percona-operator-for-postgresql/3.0.0/quickstart.html){:target="_blank"}.

New features and improvements introduced by this release include:

* [Crunchy CRD renaming and seamless resource migration](https://docs.percona.com/percona-operator-for-postgresql/3.0.0/upgrade-operator.html#renamed-upstream-crds-operator-300-and-later){:target="_blank"} — Upstream Crunchy Custom Resource Definitions (CRDs) are now moved to a new API group `upstream.pgv2.percona.com` and the Operator automatically migrates all dependent resources to this API group. This change enables seamless coexistence of Crunchy and Percona Operators in the same Kubernetes cluster and provides a smooth migration path from one to another.

* Improved namespace scoping for Operator OLM installations from Community catalogues - Operator installs from Community catalogues now respect the OperatorGroup namespace scope. In the *all-namespaces* mode it now correctly watches the whole cluster instead of its install namespace as in previous versions. In the *single-namespace* mode it only watches the namespaces listed in `olm.targetNamespaces`. After upgrade, the Operator may start reconciling `PerconaPostgreSQL` resources in namespaces it previously ignored. [Check the Operator installation mode before you upgrade](https://docs.percona.com/percona-operator-for-postgresql/3.0.0/update-openshift.html#before-you-start){:target="_blank"}, especially if several Operators share a cluster; consider enabling the single-namespace mode per Operator to avoid overlapping reconciliation.

* The `stable` channel for Certified Operator catalogues on OpenShift now supports both single-namespace and all-namespace installation modes. For this reason, the `stable-cw` channel is now deprecated and will be removed. We encourage users to switch to using the `stable` channel. If you use OLM console, change the channel to `stable`, preview and approve the Install Plan. 

  If you use the command-line, update the subscription and approve the Install Plan in case of manual approval is required. 


* Deprecation, rename and removal:

    * The `stable-cw` installation channel for Certified Operator catalogues on OpenShift is deprecated. Switch to using the `stable` channel as it now supports both single-namespace and all-namespace installation modes.

Learn more in Percona Operator for PostgreSQL 3.0.0 [release notes](https://docs.percona.com/percona-operator-for-postgresql/3.0/ReleaseNotes/Kubernetes-Operator-for-PostgreSQL-RN3.0.0.html){:target="_blank"}.


