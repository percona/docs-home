---
date: 2025-04-03
description: >
  Percona Everest 1.5.0 now includes Helm charts
authors: [rasika-chivate]
categories:
  - Percona Everest
tags:
  - Percona Everest
---

# Streamlining RBAC with enhanced IdP group integration

<!-- more -->

Give [Percona Everest](https://docs.percona.com/everest/index.html){:target="_blank"} a go by following our [Quickstart guide](https://docs.percona.com/everest/quick-install.html){:target="_blank"}.


Starting with Percona Everest 1.5.0, you can now assign RBAC policies to user groups obtained from the external IDP. This enhancement simplifies permissions management for external users without the need for unique sub IDs. To use IdP groups in Percona Everest RBAC, you must set up the groups claim in your IdP provider configuration.

Configure your Identity Provider (IdP) to provide the user’s groups claim by following our [documentation](https://docs.percona.com/everest/administer/Idp_groups_integration.html).

To retrieve the IdP groups, you need to include the groups scope by specifying the following fields:

    everestctl settings oidc configure --issuer-url=http://url.com --client-id=<your-app-client-id> --scopes openid,profile,email,groups


Learn more in Percona Everest 1.5.0 [release notes](https://docs.percona.com/everest/release-notes/Percona-Everest-1.5.0-%282025-03-04%29.html){:target="_blank"}.

