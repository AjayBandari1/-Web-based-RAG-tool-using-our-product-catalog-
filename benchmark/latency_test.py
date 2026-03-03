
import time
from core.rag_engine import SHLEliteRAG

rag = SHLEliteRAG("data/Gen_AI Dataset.xlsx")

start = time.time()
rag.search("Java developer assessment", k=5)
end = time.time()

print("Latency (seconds):", end - start)
