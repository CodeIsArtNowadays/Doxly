from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserCredentialsSchema(UserBaseSchema):
    password: str
