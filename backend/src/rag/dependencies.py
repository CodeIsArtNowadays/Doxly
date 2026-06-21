from fastapi import Depends

from src.docs.repository import ChunkRepository
from src.rag.rag_service import RagService
from src.docs.dependencies import get_chunk_repo


def get_rag_service(repo: ChunkRepository = Depends(get_chunk_repo)):
    return RagService(repo)