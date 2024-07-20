from datetime import datetime
from typing import Union
from pydantic import EmailStr
from app.responses.base import BaseResponse


class UserResponse(BaseResponse):
    id:int
    name:str
    email:EmailStr
    is_active :bool
    created_at: Union[str,None,datetime] = None
    class Config:
        from_attributes = True