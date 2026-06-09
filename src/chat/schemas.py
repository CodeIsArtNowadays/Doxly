from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.workspaces.schemas import MemberCreateSchema


class ChannelSchema(BaseModel):
    workspace_id: int

class MessageSchema(BaseModel):
    text: str
    author_id: int
    channel_id: int

class MessageResponseSchema(BaseModel):
    text: str
    author: MemberCreateSchema
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)