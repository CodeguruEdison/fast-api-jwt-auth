from fastapi import APIRouter,status,Depends

from app.config.dependency_config import DependencyConfig, get_dependency_config
from app.responses.user import UserReponse
from app.schemas.user import RegisterUserRequest


user_router =APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404:{"description":"Not found"}},
)

class UserController:
    def __init__(self,config:DependencyConfig=Depends(get_dependency_config)):
        self.user_service =config.get_user_services()

    # @user_router.post("",response_model=UserReponse,status_code=status.HTTP_201_CREATED)
    async def register_user(self,data:RegisterUserRequest):
        user = await self. user_service.create_user_account(data)
        return user
user_controller = UserController()
user_router.post("",response_model=UserReponse,status_code=status.HTTP_201_CREATED)
