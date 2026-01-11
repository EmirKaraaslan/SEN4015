from fastapi import APIRouter, HTTPException, status, Query
from typing import Optional
from app.database import get_database
from app.models.ticket import TicketResponse, TicketCategory

router = APIRouter(prefix="/tickets", tags=["getCustomTickets"])


@router.get(
    "/getCustomTickets",
    response_model=list[TicketResponse],
    summary="Get User Tickets",
    description="Each user can view their own tickets. Filter by category using the category parameter for hardware/software filtering"
)
async def getCustomTickets(
    user_id: str = Query(..., description="User ID to filter tickets"),
    category: Optional[TicketCategory] = Query(None, description="Filter by category (Hardware/Software/Network)")
) -> list[TicketResponse]:
    """
    getCustomTickets API
    
    Each user can view their own tickets.
    
    - When user clicks on hardware tickets, only hardware tickets are returned
    - When user clicks on software tickets, only software tickets are returned
    - Managed via category parameter
    
    Parameters:
    - user_id: Required - User ID
    - category: Optional - Hardware/Software/Network filter
    """
    db = get_database()
    

    user = await db.users.find_one({"user_id": user_id})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found: {user_id}"
        )
    

    query = {"owner_id": user_id}
    
    if category:
        query["category"] = category.value
    

    tickets = []
    cursor = db.tickets.find(query).sort("created_at", -1)
    
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
