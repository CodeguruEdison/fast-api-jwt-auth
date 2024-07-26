
from abc import ABC, abstractmethod
from app.config.security import hash_password, is_password_strong_enough
from app.models.user import User
from app.repository.interfaces.iuser_repository import IUserRepository
from app.responses.user import UserResponse
from app.schemas.user import RegisterUserRequest
from app.mappers.user_mapper import user_to_user_response
from app.schemas.custom_exception import  PasswordNotStrongEnoughException, UserAlreadyExistsException

class AbstractUserService(ABC):
  def __init__(self,user_repository:IUserRepository):
    self.user_repository:IUserRepository=user_repository
  
  @abstractmethod
  async def create_user_account(self, data: RegisterUserRequest) -> User|None:
        pass


class UserService(AbstractUserService):
  def __init__(self,user_repository:IUserRepository):
      super().__init__(user_repository)
 
  async def create_user_account(self,data:RegisterUserRequest)->UserResponse|None:
    if self.user_repository.is_user_exists_by_email(data.email):
     raise UserAlreadyExistsException()
    if not is_password_strong_enough(data.password):
      raise PasswordNotStrongEnoughException()
    else:
     user = User(name=data.name,
                 email =data.email,
                 password=hash_password(data.password),
                 is_active=False)
     db_user = self.user_repository.add(user) 
     #Account verification
     
     return user_to_user_response(db_user)    
      
