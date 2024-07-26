import os
from pathlib import Path
from fastapi import BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from app.config.settings import get_settings


settings =get_settings()
def str_to_bool(value):
    return value.lower() in ('true', '1', 'yes')

conf = ConnectionConfig(
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME", ""),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD", ""),
    MAIL_FROM="test@email.com",
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 1025)),
    MAIL_SERVER=os.environ.get("MAIL_SERVER", ""),
    MAIL_FROM_NAME=os.environ.get("MAIL_FROM_NAME", "no-reply@test.com"),
    MAIL_STARTTLS=str_to_bool(os.environ.get("MAIL_STARTTLS", "False")),
    MAIL_SSL_TLS=str_to_bool(os.environ.get("MAIL_SSL_TLS", "False")),
    USE_CREDENTIALS= str_to_bool(os.environ.get("USE_CREDENTIALS",True)),
    VALIDATE_CERTS=True,
    MAIL_DEBUG=True,
    SUPPRESS_SEND=str_to_bool(os.environ.get("SUPPRESS_SEND", "False")),
    TEMPLATE_FOLDER=Path(__file__).parent/"templates"
    
)
fm = FastMail(config=conf)

async def send_email(recipients:list,subject:str,context:dict,template_name:str,background_tasks:BackgroundTasks):
    message = MessageSchema(
            subject=subject,
            recipients= recipients,
            template_body=context,
            subtype=MessageType.html)
    background_tasks.add_task(fm.send_message,message,template_name=template_name)
    