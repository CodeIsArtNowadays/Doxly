from fastapi import APIRouter, Depends

from src.auth.schemas import UserCredentialsSchema, UserLoginResponseSchema
from src.auth.service import UserService
from src.auth.dependencies import get_user_service


auth_router = APIRouter()

@auth_router.post('/signup', response_model=UserLoginResponseSchema)
async def signup(
    user_data: UserCredentialsSchema,
    user_service: UserService = Depends(get_user_service)
):
    token = await user_service.create_user(user_data)
    return UserLoginResponseSchema(jwt_token=token)


@auth_router.post('/login', response_model=UserLoginResponseSchema)
async def login(
    user_data: UserCredentialsSchema,
    user_service: UserService = Depends(get_user_service)
):
    token = await user_service.login(user_data)
    return UserLoginResponseSchema(jwt_token=token)
