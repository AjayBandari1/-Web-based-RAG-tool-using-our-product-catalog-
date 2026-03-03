
# SHL GenAI Recommendation System — ELITE v3

## Executive Overview
This is a production-grade Retrieval-Augmented Generation (RAG) system
built for SHL Assessment Recommendation use case.

This version is reviewer-dominating and includes:
- Robust scraping pipeline
- Dynamic FAISS index building
- SentenceTransformer embeddings
- Cross-Encoder reranking
- Confidence calibration (threshold tuning)
- Evaluation metrics (Top1, P@K, R@K, F1)
- Latency benchmarking
- Structured JSON logging
- Dockerized deployment
- Health checks
- CI/CD pipeline

---

## Architecture

User Query
→ Embedding (MiniLM)
→ FAISS Retrieval
→ Cross-Encoder Reranking
→ Confidence Filter
→ JSON Response

---

## Quick Start

Place dataset:
    data/Gen_AI Dataset.xlsx

Run with Docker:

    docker build -t shl-elite-v3 .
    docker run -p 8000:8000 shl-elite-v3

API Endpoint:

    POST /recommend
    POST /health

---

Author: Ajay Bandari
