from fastapi import APIRouter, HTTPException, status
from app.database import get_database
from app.models.user import UserLogin, LoginResponse, UserResponse, UserRole

router = APIRouter(prefix="/auth", tags=["loginSystem"])


@router.post(
    "/loginSystem",
    response_model=LoginResponse,
    summary="System Login",
    description="Logs users into the system, distinguishes between user and admin roles"
)
async def loginSystem(login_data: UserLogin) -> LoginResponse:
    """
    loginSystem API
    
    Logs users into the system. Distinguishes between User and Admin roles.
    
    - Authenticates with email and password
    - Password is compared as plain text (no hashing)
    """
    db = get_database()
    
    # Find user by email
    user = await db.users.find_one({"email": login_data.email})
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found. Please check your email address."
        )
    
    # Plain text password comparison (per requirements)
    if user["password"] != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password. Please try again."
        )
    
    # Create user response (excluding password)
    user_response = UserResponse(
        user_id=user["user_id"],
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"],
        department=user["department"],
        role=user["role"]
    )
    
    return LoginResponse(
        success=True,
        message="Login successful!",
        user=user_response
    )
