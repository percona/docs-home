# What's new with Percona?

At Percona, we've been hard at work listening to your feedback and developing innovative solutions to improve your database experience.

Our latest releases offer a range of enhancements, from performance optimizations to new features, designed to streamline your database operations and maximize your database's potential.

[Subscribe to RSS feed](https://docs.percona.com/feed_rss_created.xml){.md-button target="_blank"}

## Featured announcements

<div data-grid markdown> <div data-banner="mongodb" markdown>
### <span style="font-size:1.875em;margin-right:0.125em">:percona-mongodb:</span> Percona Search for MongoDB 1.70.4-2: automatic embedding with OpenAI-compatible providers {.title}

Percona Search for MongoDB 1.70.4-2 introduces the OPENAI_COMPATIBLE embedding provider. Automatic embedding no longer requires a Voyage AI account: mongot can generate vector embeddings using any server that implements the OpenAI /v1/embeddings API. That covers local engines such as Ollama, vLLM, and Hugging Face Text Embeddings Inference, alongside OpenAI and Azure OpenAI. Run embeddings on your own hardware with no API key and no per-token charges, or point at a hosted service. Voyage and OpenAI-compatible models can run side by side on the same mongot instance.

<div class="actions" markdown>

Read more :material-arrow-right:{:target="_blank"}

<span style="float: right;">September 03, 2026</span>


<div data-grid markdown>
<div data-banner="pmm" markdown>

### <span style="font-size:1.875em;margin-right:0.125em">:percona-pmm:</span> PMM 3.9.1: Security release: upgrade now {.title}

PMM 3.9.1 fixes a high-severity vulnerability that allowed any signed-in user to run arbitrary SQL via the Grafana ClickHouse data source. This release also removes eight high-severity CVEs and fixes encryption key rotation and client reconnection bugs.

<div class="actions" markdown>

[Read more :material-arrow-right:](../new/posts/Percona%20Monitoring%20and%20Management/pmm-3.9.1-release.md){:target="_blank"}

<span style="float: right;">August 19, 2026</span>

</div>
</div>

<div data-banner="mysql" markdown>

### <span style="font-size:1.875em;margin-right:0.125em">:percona-mysql:</span> Percona Server for MySQL 8.4.11-11: OpenID Connect (OIDC) authentication and authorization {.title}

Percona Server for MySQL 8.4.11-11 introduces OpenID Connect (OIDC) authentication and authorization. Users can authenticate with Identity tokens issued by external Identity Providers (IDPs) instead of MySQL passwords. The OIDC plugin supports multiple IDPs, maps IDP groups to MySQL roles, supports proxy users based on group membership, and refreshes JSON Web Key Set (JWKS) signing keys at runtime.

<div class="actions" markdown>

[Read more :material-arrow-right:](../new/posts/MySQL/percona-server-8.4.11-11-release.md){:target="_blank"}

<span style="float: right;">August 20, 2026</span>

</div>
</div>

<div data-banner="mongodb" markdown>

### <span style="font-size:1.875em;margin-right:0.125em">:percona-mongodb:</span> Percona Server for MongoDB {.title}

Percona Server for MongoDB 7.0.40-22 and 8.0.29-13 are now available. These releases bring the latest fixes from MongoDB Community Edition, keeping your deployments aligned with upstream patches and improvements.

<div class="actions" markdown>

[Read more :material-arrow-right:](../new/posts/MongoDB/psmdb-7.0.40-22-and-8.0.29-13-release.md){:target="_blank"}

<span style="float: right;">August 20, 2026</span>

</div>
</div>
</div>