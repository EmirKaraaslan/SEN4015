from fastapi import APIRouter, HTTPException, status
from app.database import get_database
from app.models.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["createUser"])


@router.post(
    "/createUser",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create User",
    description="Creates a new user - for manual use via Postman or Terminal only, not used in UI"
)
async def createUser(user: UserCreate) -> UserResponse:
    """
    createUser API
    
    Creates a new user. Not used in UI, only for manual use via Postman or Terminal.
    
    User Model:
    - user_id: Unique user ID
    - first_name: User's first name
    - last_name: User's last name
    - email: Email address
    - department: Department
    - role: Role (user or admin)
    """
    db = get_database()
    
   
    existing_user = await db.users.find_one({"user_id": user.user_id})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"This user_id is already in use: {user.user_id}"
        )
    
    
    existing_email = await db.users.find_one({"email": user.email})
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"This email address is already registered: {user.email}"
        )
    
  
    user_dict = user.model_dump()
    
    
    result = await db.users.insert_one(user_dict)
    
    if not result.inserted_id:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the user."
        )
    
   
    return UserResponse(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        department=user.department,
        role=user.role
    )
