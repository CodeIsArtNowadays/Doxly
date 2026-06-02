from sqlalchemy import select

from src.core.generic_repository import BaseRepository

from src.auth.models import UserModel


class UserRepository(BaseRepository):
    model = UserModel

    async def get_by_username(self, username: str):
        stmt = select(self.model).where(self.model.username == username)
        return await self.session.scalar(stmt)
        