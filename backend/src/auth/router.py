from fastapi import APIRouter, Depends

from src.core.dependencies import get_user
from src.auth.models import UserModel
from src.auth.service import UserService
from src.auth.exceptions import UserException
from src.auth.schemas import UserCredentialsSchema, UserLoginResponseSchema, UserBaseSchema
from src.auth.registration import RegistrationUseCase
from src.auth.dependencies import get_user_service


auth_router = APIRouter()

@auth_router.post('/signup', response_model=UserLoginResponseSchema)
async def signup(
    credentials: UserCredentialsSchema,
    registration: RegistrationUseCase = Depends(RegistrationUseCase),
    user_service: UserService = Depends(get_user_service)
):
    user = await registration(credentials)
    if not user: 
        raise UserException
    response = await user_service.login(credentials)
    return UserLoginResponseSchema(jwt_token=response['token'], username=response['user'].username)


@auth_router.post('/login', response_model=UserLoginResponseSchema)
async def login(
    user_data: UserCredentialsSchema,
    user_service: UserService = Depends(get_user_service)
):
    response = await user_service.login(user_data)
    return UserLoginResponseSchema(jwt_token=response['token'], username=response['user'].username)

@auth_router.get('/me', response_model=UserBaseSchema)
async def me(user: UserModel = Depends(get_user)):
    return user
