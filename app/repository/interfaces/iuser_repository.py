
from abc import ABC
from sqlalchemy.orm import Session

from app.models.user import User

class IUserRepository(ABC):
    def __init__(self,session:Session):
        self.session=session
    async def add(self,user:User):
        pass
    