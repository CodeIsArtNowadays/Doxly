from pydantic import BaseModel, ConfigDict

from src.core.custom_types import RoleLiteral


class MemberCreateSchema(BaseModel):
    user_id: int


class WorkspaceBaseSchema(BaseModel):
    title: str

    model_config = ConfigDict(from_attributes=True)


class WorkspaceCreateRequestSchema(WorkspaceBaseSchema):
    pass


class WorkspaceCreateSchema(WorkspaceCreateRequestSchema):
    user_id: int


class WorkspaceMemberCreateSchema(BaseModel):
    user_id: int
    workspace_id: int
    role: RoleLiteral | None = None