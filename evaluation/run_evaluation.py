
import pandas as pd
from core.rag_engine import SHLEliteRAG

rag = SHLEliteRAG("data/Gen_AI Dataset.xlsx")
df = pd.read_excel("data/Gen_AI Dataset.xlsx")

correct = 0
total = len(df)

for _, row in df.iterrows():
    results = rag.search(row["Query"], k=1)
    if results and results[0]["assessment_url"] == row["Assessment_url"]:
        correct += 1

accuracy = correct / total
print("Top-1 Accuracy:", accuracy)
