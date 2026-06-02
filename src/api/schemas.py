from pydantic import BaseModel


class MemberCreateSchema(BaseModel):
    user_id: int