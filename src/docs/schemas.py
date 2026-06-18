from pydantic import BaseModel


class DocumentCreateSchema(BaseModel):
    title: str
    workspace_id: int
    author_id: int
    url: str


class ChunkCreateSchema(BaseModel):
    document_id: int
    document_index: int
    embedding: list[float]
    text: str