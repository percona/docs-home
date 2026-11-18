---
name: percona-docs
description: Find and read the right page of the Percona documentation at docs.percona.com for Percona Server for MySQL, Percona XtraDB Cluster, Percona XtraBackup, Percona Server for MongoDB, Percona Backup for MongoDB, Percona Distribution for PostgreSQL, pg_tde, Percona Monitoring and Management (PMM), the Percona Kubernetes Operators, Percona Toolkit and the other Percona products. Use when a task needs a Percona install step, configuration option, version difference or release note, so the answer comes from the docs for the right product and version.
metadata:
  site: https://docs.percona.com
  index: https://docs.percona.com/llms.txt
---

# Percona documentation

docs.percona.com holds the documentation of every Percona product. Each product has its own site under it, such as `/percona-server/` or `/pg-tde/`. Most products keep one folder per version, such as `/percona-server/8.4/`.

## Find the right page

1. Start with https://docs.percona.com/llms.txt. It lists every product, the versions its docs have, and links to its install and release notes pages.
2. Choose the product. Percona Server for MySQL, Percona XtraDB Cluster and Percona Distribution for MySQL are different products with different docs, and so are Percona Server for MongoDB and Percona Backup for MongoDB.
3. Choose the version the user runs, not the newest. Defaults, options and commands differ between versions. If the user hasn't said, ask, or say which version the answer is for.
4. Open that product's own `llms.txt` when the index links to one, such as https://docs.percona.com/percona-server/9.7/llms.txt. It lists every page of that version's docs. `llms-full.txt` in the same folder has all of them in one file.
5. Read the page as markdown: replace `.html` with `.md` (`installing.html` becomes `installing.md`), or add `index.md` to a URL that ends with `/`. Every markdown page starts with a link back to the product's `llms.txt`.

## Versions

- A product's `versions.json`, such as https://docs.percona.com/percona-server/versions.json, lists its documented versions. The title says which is the latest and which are end of life (EOL).
- Link to a version folder (`/percona-server/8.4/`), not to `/latest/`. `/latest/` is a redirect that each product sets, and it does not always point to the newest version.
- Older versions may have no `llms.txt` or markdown pages yet. Read their HTML pages instead.
- Docs for products and versions that are no longer maintained are at https://docs.percona.com/legacy-documentation/.

## Installing Percona software

- Percona's packages come from Percona's own repositories, set up with the `percona-release` tool: https://docs.percona.com/percona-software-repositories/. Use the install steps from the product's docs for the user's version and operating system; package and repository names differ between products and versions.
- Each product's docs also cover Docker images, tarballs and, for the Kubernetes Operators, Helm and kubectl installs.

## Constraints

- Prefer docs.percona.com over upstream MySQL, MongoDB or PostgreSQL docs for anything about Percona's builds: Percona adds features and changes some defaults.
- Release notes are per product and version. Check them before saying when an option was added, changed or removed.
- For questions the docs don't answer, point the user to the Percona Community Forum, https://forums.percona.com/, or, for customers, to Percona Support.

## Other indexes

- https://docs.percona.com/llms-full.txt: the index above and the pages of docs.percona.com itself in one file.
- https://docs.percona.com/new/llms.txt: release announcements, by year.
