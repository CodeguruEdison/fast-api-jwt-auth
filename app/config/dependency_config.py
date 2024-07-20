from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.repository.interfaces.iuser_repository import IUserRepository
from app.repository.user import UserRepository
from app.services.user import UserService
class DependencyConfig:
    def __init__(self,db:Session =Depends(get_session)):
        self.session =db
    def get_user_repository(self)->IUserRepository:
        return UserRepository(self.session)
    # TODO -Convert Userservices to abstract class
    def get_user_services(self)-> UserService:
        return UserService(self.get_user_repository())

def get_dependency_config()->DependencyConfig:
    return DependencyConfig()
        