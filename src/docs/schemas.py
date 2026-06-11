from pydantic import BaseModel


class DocumentCreateSchema(BaseModel):
    title: str
    workspace_id: int
    author_id: int
    url: str