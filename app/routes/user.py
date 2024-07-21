from fastapi import APIRouter,Depends, HTTPException,status

from app.config.dependency_config import get_user_service
from app.responses.user import UserResponse
from app.schemas.user import RegisterUserRequest
from app.schemas.user_custom_exception import UserAlreadyExistsException
from app.services.user import AbstractUserService


user_router =APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404:{"description":"Not found"}},
)
@user_router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(data:RegisterUserRequest,user_service:AbstractUserService = Depends(get_user_service)):
    try:
        user = await user_service.create_user_account(data)
        return user
    except UserAlreadyExistsException as e:
        raise HTTPException(status_code=400,detail=str(e))
        
    
