

from fastapi import BackgroundTasks, Depends
from app.config.email import send_email
from app.models.user import User
from abc import ABC, abstractmethod
from app.config.security    import hash_password
from app.util.token_context import USER_VERIFY_ACCOUNT
from app.config.settings import Settings, get_settings;




class AbstractEmailService(ABC):
   
    @abstractmethod
    async def send_account_verification_email(self, user: User, background_tasks: BackgroundTasks) -> None:
        pass

class EmailService(AbstractEmailService):
    def __init__(self, settings: Settings = Depends(get_settings)) -> None:
        self.settings = settings

    async def send_account_verification_email(self, user: User, background_tasks: BackgroundTasks) -> None:
        string_context = user.get_context_string(context=USER_VERIFY_ACCOUNT)
        token = hash_password(string_context)
        activate_url = f"{self.settings.FRONTEND_HOST}/auth/account-verify?token={token}&email={user.email}"
        data = {
            'app_name': self.settings.APP_NAME,
            "name": user.name,
            'activate_url': activate_url
        }
        subject = f"Account Verification - {self.settings.APP_NAME}"
        await send_email(
            recipients=[user.email],
            subject=subject,
            template_name="user/account-verification.html",
            context=data,
            background_tasks=background_tasks
        )
    