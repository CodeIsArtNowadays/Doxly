from fastapi import APIRouter, Depends

from src.auth.service import UserService
from src.auth.schemas import UserCredentialsSchema, UserLoginResponseSchema
from src.auth.registration import RegistrationUseCase
from src.auth.dependencies import get_user_service


auth_router = APIRouter()

@auth_router.post('/signup', response_model=UserLoginResponseSchema)
async def signup(
    credentials: UserCredentialsSchema,
    registration: RegistrationUseCase = Depends(RegistrationUseCase)
):
    token = await registration(credentials)
    return UserLoginResponseSchema(jwt_token=token)


@auth_router.post('/login', response_model=UserLoginResponseSchema)
async def login(
    user_data: UserCredentialsSchema,
    user_service: UserService = Depends(get_user_service)
):
    token = await user_service.login(user_data)
    return UserLoginResponseSchema(jwt_token=token)
