from fastapi import APIRouter, HTTPException, status, Query
from app.database import get_database
from app.models.user import UserResponse, UserRole

router = APIRouter(prefix="/users", tags=["getAllUsers"])


@router.get(
    "/getAllUsers",
    response_model=list[UserResponse],
    summary="Get All Users (Admin Only)",
    description="Admins can list all users in the system"
)
async def getAllUsers(
    admin_id: str = Query(..., description="Admin user ID for authorization")
) -> list[UserResponse]:
    """
    getAllUsers API (Admin Only)

    Admin can list all users in the system.

    - Requires admin permission
    - Returns all users (excluding passwords)

    Parameters:
    - admin_id: Required - Admin user ID
    """
    db = get_database()


    admin = await db.users.find_one({"user_id": admin_id})

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found: {admin_id}"
        )

    if admin["role"] != UserRole.ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin permission required for this operation."
        )


    users = []
    cursor = db.users.find({}).sort("user_id", 1)

    async for user in cursor:
        users.append(
            UserResponse(
                user_id=user["user_id"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                department=user["department"],
                role=user["role"]
            )
        )

    return users
