from app.models.user import User
from app.responses.user import UserResponse

def user_to_user_response(user: User) -> UserResponse:
    try:
        # Manually map attributes from User to UserResponse
        return UserResponse(
            id=user.id, 
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at
        )
    except Exception as e:
        print(f"Error mapping User to UserResponse: {e}")
        raise