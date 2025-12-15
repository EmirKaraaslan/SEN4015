from fastapi import APIRouter, HTTPException, status, Query
from app.database import get_database
from app.models.ticket import TicketResponse
from app.models.user import UserRole

router = APIRouter(prefix="/tickets", tags=["getAllTickets"])


@router.get(
    "/getAllTickets",
    response_model=list[TicketResponse],
    summary="Get All Tickets (Admin Only)",
    description="Admins can list all tickets in the system"
)
async def getAllTickets(
    admin_id: str = Query(..., description="Admin user ID for authorization")
) -> list[TicketResponse]:
    """
    getAllTickets API (Admin Only)
    
    Admin can list all tickets.
    
    - Requires admin permission
    - Returns all tickets in the system
    
    Parameters:
    - admin_id: Required - Admin user ID for authorization
    """
    db = get_database()
    
    # Verify admin exists and has admin role
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
    
    # Retrieve all tickets
    tickets = []
    cursor = db.tickets.find({}).sort("created_at", -1)
    
    async for ticket in cursor:
        tickets.append(TicketResponse(
            ticket_id=ticket["ticket_id"],
            ticket_number=ticket["ticket_number"],
            title=ticket["title"],
            description=ticket["description"],
            category=ticket["category"],
            priority=ticket["priority"],
            status=ticket["status"],
            created_at=ticket["created_at"],
            owner_id=ticket["owner_id"]
        ))
    
    return tickets
