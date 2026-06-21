import numpy as np

from sentence_transformers import SentenceTransformer

from src.docs.models import ChunkModel
from src.rag.calculations import bm25, cos_sim, min_max_norm


semantic_model = SentenceTransformer("all-MiniLM-L6-v2")

# @ai -> message -> ... -> hybrid (message, chunks) -> llm (message, top3 chunk)
#           get_all_workspace_chunks

# -> chunks = [+'score': 0.5]


def rate_chunks(message: str, chunks: list[ChunkModel], k: int=5):
    message_vector = semantic_model.encode(message)

    chunks_texts = [chunk.text for chunk in chunks]
    chunks_vectors = [chunk.embedding for chunk in chunks]

    bm25_scores = np.array(bm25(message, chunks_texts))
    cos_sim_scores = np.array([cos_sim(message_vector, vector) for vector in chunks_vectors])

    bm25_scores = min_max_norm(bm25_scores)

    for chunk, bm25_score, cossim_score in zip(chunks, bm25_scores, cos_sim_scores):
        chunk.score = bm25_score * 0.5 + cossim_score * 0.5

    return sorted(chunks, key=lambda x: x.score, reverse=True)[:k]
