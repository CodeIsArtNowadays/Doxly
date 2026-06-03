from fastapi import APIRouter, Depends

from src.workspaces.models import MemberModel
from src.workspaces.service import WorkspaceService
from src.workspaces.schemas import WorkspaceCreateRequestSchema
from src.workspaces.dependencies import get_member, get_workspace_service


workspaces_router = APIRouter()


@workspaces_router.get('/index')
async def index():
    return {'me': 'KING'}


@workspaces_router.post('/')
async def create_workspace(
    workspace_data: WorkspaceCreateRequestSchema,
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    member: MemberModel = Depends(get_member)
):
    '''Title, user'''
    return await workspace_service.create_workspace(workspace_data, member.user_id)
    

@workspaces_router.get('/{id}')
async def get_workspace(id: int):
    # workspace + it's members 
    pass 
    