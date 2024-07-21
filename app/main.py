from fastapi import FastAPI
from app.handlers.exception_handlers import exception_handler
from app.routes import user
from app.schemas.custom_exception import CustomException

def create_application():
    application = FastAPI()
    application.add_exception_handler(CustomException,exception_handler)
    application.include_router(user.user_router)
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, I am Describly. Awesome - Your setrup is done & working."}