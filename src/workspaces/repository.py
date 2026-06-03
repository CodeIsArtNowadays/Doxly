from sqlalchemy import select

from src.core.generic_repository import BaseRepository
from src.workspaces.models import MemberModel
from src.workspaces.models import WorkspaceModel, WorkspaceMember


class MemberRepository(BaseRepository):
    model = MemberModel

    async def get_member_by_user_id(self, user_id) -> MemberModel | None:
        stmt = select(MemberModel).where(user_id == user_id)
        return await self.session.scalar(stmt)


class WorkspaceRepository(BaseRepository):
    model = WorkspaceModel


class WorkspaceMemberRepository(BaseRepository):
    model = WorkspaceMember