
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.models.user import User


class IUserRepository(ABC):
    def __init__(self,session:Session):
        self.session:Session=session
    @abstractmethod    
    def add(self,user:User)->User:
        pass
    