
from app.models.user import User
from app.repository.interfaces.iuser_repository import IUserRepository
from app.schemas.user import RegisterUserRequest



class UserService:
  def __init__(self,user_repository:IUserRepository):
      self.user_repository:IUserRepository = user_repository
 
  async def create_user_account(self,data:RegisterUserRequest):
     user = User(name=data.name,email =data.email,pasword=data.password,is_active=data.password)
     return await self.user_repository.add(user)     
      
