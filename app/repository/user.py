from sqlalchemy.orm import Session
from app.models.user import User
from app.repository.interfaces.iuser_repository import IUserRepository

class UserRepository(IUserRepository):
    session:Session
    def __init__(self,session:Session):
        self.session =session
        super().__init__(session=session)
        
    def add(self,user:User):
        self.session.add(user)
        self.session.refresh(user)
