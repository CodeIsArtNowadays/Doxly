from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from src.workspaces.schemas import MemberCreateSchema


class MessageSchema(BaseModel):
    text: str
    author_id: int
    workspace_id: int
    is_ai: bool = Field(default=False)

class MessageResponseSchema(BaseModel):
    text: str
    author: MemberCreateSchema
    created_at: datetime | str

    model_config = ConfigDict(from_attributes=True)


class AiMessageSchema(MessageSchema):
    chunks: list[int]