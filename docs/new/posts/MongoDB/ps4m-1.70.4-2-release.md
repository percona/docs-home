---
date: 2026-09-03
description: >
  Percona Search for MongoDB 1.70.4-2 has been released on September 3, 2026.
authors: [rasika-chivate]
categories:
  - MongoDB
tags:
  - Percona Search for MongoDB
---

# Percona Search for MongoDB 1.70.4-2 has been released

<!-- more -->

[Percona Search for MongoDB 1.70.4-2](https://docs.percona.com/percona-search-for-mongodb/){:target="_blank"} has been released on September 3, 2026.

Percona Search for MongoDB now supports automatic embedding with services that implement the OpenAI `/v1/embeddings `API. You are no longer limited to Voyage AI. The new `OPENAI_COMPATIBLE` provider lets you use local or hosted embedding servers, including self-hosted options that can run without API keys or usage-based token charges.

This covers Ollama, vLLM, llama.cpp, LM Studio, LocalAI, and Hugging Face Text Embeddings Inference, alongside OpenAI and Azure OpenAI. Voyage AI and OpenAI-compatible models can be configured on the same mongot instance. The model specified in an autoEmbed index determines which embedding provider mongot uses.

With an autoEmbed Vector Search index, mongot updates embeddings for your documents as they change and creates an embedding for a query text at search time, so there is no additional pipeline to build or maintain. This extends upstream MongoDB Automated Embedding , which supports Voyage AI only.

Try it out using the [Install guide](https://docs.percona.com/percona-search-for-mongodb/install-mongot.html){:target="_blank"}. 

Learn more about this release in Percona Search for MongoDB 1.70.4-2 [release notes](https://docs.percona.com/percona-search-for-mongodb/release_notes/1.70.4-2.html){:target="_blank"}.

