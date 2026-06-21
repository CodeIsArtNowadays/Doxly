from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserCredentialsSchema(UserBaseSchema):
    password: str


class UserLoginResponseSchema(BaseModel):
    username: str
    jwt_token: str
