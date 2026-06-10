from src.core.generic_repository import BaseRepository
from src.docs.models import DocumentModel


class DocumentRepository(BaseRepository):
    model = DocumentModel