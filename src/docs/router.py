from fastapi import APIRouter, Depends, UploadFile, File

from src.docs.dependencies import get_docs_service
from src.docs.service import DocumentService
from src.workspaces.models import MemberModel
from src.workspaces.dependencies import Permission


docs_router = APIRouter(prefix='/{workspace_id}')


@docs_router.post('upload')
async def upload_document(
    workspace_id: int, 
    file: UploadFile = File(...),
    member: MemberModel = Depends(Permission(['owner', 'admin', 'member'])),
    docs_service: DocumentService = Depends(get_docs_service)
):
    allowed_extensions = {'pdf', 'docx', 'txt'}
    
    file_extension = file.filename.split('.')[-1].lower() if file.filename else ''

    if file_extension not in allowed_extensions:
        raise Exception # TODO: exc
        
    # docs_service.proccess_in_background