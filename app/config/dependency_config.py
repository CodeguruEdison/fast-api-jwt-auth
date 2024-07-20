from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.repository.interfaces.iuser_repository import IUserRepository
from app.repository.user import UserRepository
from app.services.user import AbstractUserService, UserService
class DependencyConfig:
    def __init__(self,session:Session =Depends(get_session)):
        self.session = session
        
    def get_user_repository(self)->IUserRepository:
        return UserRepository(self.session)
  
    def get_user_service(self)-> AbstractUserService:
        return UserService(self.get_user_repository())

def get_dependency_config(db: Session = Depends(get_session)) -> DependencyConfig:
    return DependencyConfig(db)
def get_user_service(config: DependencyConfig = Depends(get_dependency_config)) -> AbstractUserService:
    return config.get_user_service()        