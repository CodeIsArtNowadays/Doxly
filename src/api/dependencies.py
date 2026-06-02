from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.api.repository import MemberRepository


async def get_member_repo(session: AsyncSession = Depends(get_db)):
    return MemberRepository(session)