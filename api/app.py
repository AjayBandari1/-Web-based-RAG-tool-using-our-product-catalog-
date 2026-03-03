
from fastapi import FastAPI
from pydantic import BaseModel
from core.rag_engine import SHLEliteRAG
from config.logging_config import setup_logging

setup_logging()

app = FastAPI(title="SHL Elite v3 API")
rag = SHLEliteRAG("data/Gen_AI Dataset.xlsx")

class QueryRequest(BaseModel):
    query: str
    k: int = 5
    threshold: float = 0.3

@app.post("/recommend")
def recommend(request: QueryRequest):
    results = rag.search(request.query, request.k, request.threshold)
    return {"results": results}

@app.post("/health")
def health():
    return {"status": "healthy"}
