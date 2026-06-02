from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic


ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType]):

    model: type[ModelType]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data): 
        obj = self.model(**data.model_dump())
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        logger.info(f'Repository|{self.model}|Create')
        return obj

    async def get_by_id(self, id):
        
        return await self.session.get(self.model, id)
       
    async def update(self, id, upd_data):
        obj = await self.get_by_id(id)
        for k, v in upd_data.model_dump(exclude_unset=True).items():
           setattr(obj, k, v)

        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id):
        obj = await self.get_by_id(id)
        if obj:
            await self.session.delete(obj)


    