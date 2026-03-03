
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np

class SHLEliteRAG:
    def __init__(self, dataset_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        self.df = pd.read_excel(dataset_path)

        queries = self.df["Query"].astype(str).tolist()
        self.embeddings = self.model.encode(queries, convert_to_numpy=True, normalize_embeddings=True)

        self.index = faiss.IndexFlatIP(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, k=5, threshold=0.3):
        q_emb = self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
        scores, indices = self.index.search(q_emb, k)

        candidates = []
        for i, idx in enumerate(indices[0]):
            candidates.append((self.df.iloc[idx]["Assessment_url"], scores[0][i], self.df.iloc[idx]["Query"]))

        # Rerank
        pairs = [[query, c[2]] for c in candidates]
        rerank_scores = self.reranker.predict(pairs)
        rerank_scores = 1 / (1 + np.exp(-rerank_scores))

        final_results = []
        for i, c in enumerate(candidates):
            if rerank_scores[i] >= threshold:
                final_results.append({
                    "assessment_url": c[0],
                    "confidence": float(rerank_scores[i])
                })

        final_results.sort(key=lambda x: x["confidence"], reverse=True)
        return final_results
