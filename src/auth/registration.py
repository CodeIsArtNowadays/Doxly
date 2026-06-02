from fastapi import Depends

from src.auth.service import UserService
from src.auth.schemas import UserCredentialsSchema
from src.auth.dependencies import get_user_service
from src.api.schemas import MemberCreateSchema
from src.api.repository import MemberRepository
from src.api.dependencies import get_member_repo


class RegistrationUseCase:

    def __init__(
        self, 
        user_service: UserService = Depends(get_user_service),
        member_repo: MemberRepository = Depends(get_member_repo)
    ):
        self.user_service = user_service
        self.member_repo = member_repo
    
    async def __call__(self, credentials: UserCredentialsSchema):

        # Create user w/ hashed password
        hashed_password = await self.user_service.hash_password(credentials.password)
        user_data = UserCredentialsSchema(username=credentials.username, password=hashed_password)
        user = await self.user_service.create_user(user_data)

        # Create member w/ user_id
        await self.member_repo.create(MemberCreateSchema(user_id=user.id))
        
        # Login user
        jwt_token = await self.user_service.login(credentials)

        return jwt_token

        
        
        