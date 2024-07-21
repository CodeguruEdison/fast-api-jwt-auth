from fastapi import Request
from fastapi.responses import JSONResponse

from app.schemas.custom_exception import CustomException, UserAlreadyExistsException,PasswordNotStrongEnoughException

exception_responses:dict = {
    UserAlreadyExistsException: {"status_code": 400, "detail": "User with this email already exists."},
    PasswordNotStrongEnoughException: {"status_code": 400, "detail": "Password is not strong enough."},
}
def exception_handler(request:Request,exc:CustomException)->JSONResponse:
    #response = exception_responses.get(type(ex),{"status_code": 500, "detail": "An unexpected error occurred."})
    response = exception_responses.get(type(exc), {"status_code": 500, "detail": "An unexpected error occurred."})
    return JSONResponse(
        status_code=response["status_code"],
        content={"detail": response["detail"]}
    )
    
    