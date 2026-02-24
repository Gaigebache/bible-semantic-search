# bible-semantic-search

Search the Bible by meaning, not just keywords. Built with vector embeddings, hybrid search(semantic + BM25), nad an LLM chat layer.

## Features
-Semantic search across multiple translations(KJV, NIV, ESV)
-Hybrid search combining vector similarity and keyword matching
-"What does the Bible say about X?" chat interface
-Filter by book, testament, and genre
-Related passages powered by vector similarity

## Tech Stack
-Frontend: Next.js
-Backend: FastAPI
-Vector DB: pgvector(PostgreSQL)

## Status
In active development

## Architecture
See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
