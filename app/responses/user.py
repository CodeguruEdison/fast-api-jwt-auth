from datetime import datetime
from typing import Union
from pydantic import EmailStr
from app.responses.base import BaseResponse


class UserReponse(BaseResponse):
    id:int
    name:str
    email:EmailStr
    isActive:bool
    created_at: Union[str,None,datetime] = None