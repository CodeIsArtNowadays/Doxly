from src.workspaces.schemas import WorkspaceCreateRequestSchema, WorkspaceCreateSchema, WorkspaceMemberCreateSchema
from src.workspaces.repository import WorkspaceRepository, MemberRepository, WorkspaceMemberRepository


class WorkspaceService:

    def __init__(
        self, 
        workspace_repo: WorkspaceRepository,
        workspace_member_repo: WorkspaceMemberRepository
    ):
        self.workspace_repo = workspace_repo
        self.workspace_member_repo = workspace_member_repo

    async def create_workspace(self, workspace_request_data: WorkspaceCreateRequestSchema, user_id: int):
        workspace = await self.workspace_repo.create(workspace_request_data)
        workspace_member_data = WorkspaceMemberCreateSchema(workspace_id=workspace.id, user_id=user_id, role='owner')
        await self.workspace_member_repo.create(workspace_member_data)
        return workspace

    