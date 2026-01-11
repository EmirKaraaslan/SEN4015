from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.ticket import (
    TicketCreate,
    TicketResponse,
    TicketStatus
)

router = APIRouter(prefix="/tickets", tags=["createTicket"])


async def generate_ticket_number() -> str:
    """Generates a unique ticket number (e.g., T-1001)."""
    db = get_database()
    
 
    last_ticket = await db.tickets.find_one(
        {},
        sort=[("ticket_number", -1)]
    )
    
    if last_ticket and "ticket_number" in last_ticket:

        try:
            last_number = int(last_ticket["ticket_number"].split("-")[1])
            new_number = last_number + 1
        except (IndexError, ValueError):
            new_number = 1001
    else:
        new_number = 1001
    
    return f"T-{new_number}"


@router.post(
    "/createTicket",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Ticket",
    description="Creates a new support ticket with Pending status"
)
async def createTicket(ticket: TicketCreate) -> TicketResponse:
    """
    createTicket API
    
    Creates a new support ticket.
    
    Ticket Model:
    - ticket_id: Unique ID (not shown to user)
    - ticket_number: Number shown on dashboard (T-1001, T-1002, ...)
    - title: Ticket title
    - description: User's description
    - category: Hardware or Software
    - priority: Low, Medium, High
    - status: Default is "Pending"
    """
    db = get_database()
    

    owner = await db.users.find_one({"user_id": ticket.owner_id})
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found: {ticket.owner_id}"
        )
    

    ticket_id = str(ObjectId())
    ticket_number = await generate_ticket_number()
    

    ticket_dict = {
        "ticket_id": ticket_id,
        "ticket_number": ticket_number,
        "title": ticket.title,
        "description": ticket.description,
        "category": ticket.category.value,
        "priority": ticket.priority.value,
        "status": TicketStatus.PENDING.value,
        "created_at": datetime.utcnow(),
        "owner_id": ticket.owner_id
    }
    

    result = await db.tickets.insert_one(ticket_dict)
    
    if not result.inserted_id:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the ticket."
        )
    
    return TicketResponse(
        ticket_id=ticket_id,
        ticket_number=ticket_number,
        title=ticket.title,
        description=ticket.description,
        category=ticket.category,
        priority=ticket.priority,
        status=TicketStatus.PENDING,
        created_at=ticket_dict["created_at"],
        owner_id=ticket.owner_id
    )
