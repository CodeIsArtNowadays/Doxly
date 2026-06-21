from typing import Sequence
from sqlalchemy import select

from src.core.generic_repository import BaseRepository
from src.core.custom_types import StatusLiteral
from src.docs.models import DocumentModel, ChunkModel


class DocumentRepository(BaseRepository):
    model = DocumentModel

    async def get_active_documents_by_workspace_id(self, workspace_id: int) -> Sequence[DocumentModel]:
        stmt = select(DocumentModel).where(DocumentModel.workspace_id == workspace_id, DocumentModel.status == 'ready')
        res = await self.session.scalars(stmt)
        return res.all()

    async def set_status(self, document_id: int, status=StatusLiteral):
        document = await self.get_by_id(document_id)
        if not document:
            raise Exception # TODO: exc

        document.status = status
        await self.session.flush()

class ChunkRepository(BaseRepository):
    model = ChunkModel

    async def get_all_by_workspace_id(self, workspace_id: int) -> list[ChunkModel]:
        stmt = select(ChunkModel).join(DocumentModel, ChunkModel.document_id == DocumentModel.id).where(DocumentModel.workspace_id == workspace_id)
        return list(await self.session.scalars(stmt))