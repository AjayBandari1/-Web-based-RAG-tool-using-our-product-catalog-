from fastapi import FastAPI
from pydantic import BaseModel
from core.rag_engine import SHLEliteRAG
from config.logging_config import setup_logging
import os

setup_logging()

app = FastAPI(title="SHL Elite v3 API")

rag = None

@app.on_event("startup")
def load_model():
    global rag
    DATA_PATH = "data/Gen_AI Dataset.xlsx"
    rag = SHLEliteRAG(DATA_PATH)

class QueryRequest(BaseModel):
    query: str
    k: int = 5
    threshold: float = 0.3

@app.post("/recommend")
def recommend(request: QueryRequest):
    results = rag.search(request.query, request.k, request.threshold)
    return {"results": results}

@app.get("/health")
def health():
    return {"status": "ok"}
