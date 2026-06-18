from src.docs.repository import ChunkRepository
from src.rag.retriever import rate_chunks
from src.rag.llm_service import llm_service


class RagService:

    def __init__(self, chunk_repo: ChunkRepository):
        self.chunk_repo = chunk_repo

    async def process(self, message: str, workspace_id):
        chunks = await self.chunk_repo.get_all_by_workspace_id(workspace_id)
        top_related_chunks = rate_chunks(message, chunks)
        response = llm_service.ask_llm('Provided context: \n' + '\n'.join([chunk.text for chunk in top_related_chunks]))
        # response = {'type': 'llm', 'content': {'message': response}}
        return response
