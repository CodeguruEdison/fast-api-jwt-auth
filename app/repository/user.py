from sqlalchemy.orm import Session
from app.models.user import User
from app.repository.interfaces.iuser_repository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self,session:Session):
        super().__init__(session=session)
        
    def add(self,user:User)-> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
