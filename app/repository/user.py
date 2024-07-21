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
    def is_user_exists_by_email(self,email:str)->bool:
      db_user = self.session.query(User).filter_by(email=email).all()
      is_user_exists = len(db_user)>0
      return is_user_exists
          