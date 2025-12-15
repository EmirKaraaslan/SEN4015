from fastapi import APIRouter, HTTPException, status
from app.database import get_database
from app.models.ticket import TicketClose, TicketResponse, TicketStatus
from app.models.user import UserRole

router = APIRouter(prefix="/tickets", tags=["closeTicket"])


@router.put(
    "/closeTicket/{ticket_id}",
    response_model=TicketResponse,
    summary="Close Ticket (Admin Only)",
    description="Admins can change ticket status from Pending to Closed"
)
async def closeTicket(
    ticket_id: str,
    close_data: TicketClose
) -> TicketResponse:
    """
    closeTicket API (Admin Only)
    
    When admin clicks "close ticket" button, changes the ticket status
    from Pending to Closed.
    
    - Managed only via ticket_id parameter
    - Requires admin permission
    
    Parameters:
    - ticket_id: In URL - ID of the ticket to close
    - admin_id: In body - ID of the admin performing the operation
    """
    db = get_database()
    
    # Verify admin exists and has admin role
    admin = await db.users.find_one({"user_id": close_data.admin_id})
    
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin user not found: {close_data.admin_id}"
        )
    
    if admin["role"] != UserRole.ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin permission required for this operation."
        )
    
    # Find the ticket
    ticket = await db.tickets.find_one({"ticket_id": ticket_id})
    
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket not found: {ticket_id}"
        )
    
    # Check if already closed
    if ticket["status"] == TicketStatus.CLOSED.value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This ticket is already closed."
        )
    
    # Update ticket status
    result = await db.tickets.update_one(
        {"ticket_id": ticket_id},
        {"$set": {"status": TicketStatus.CLOSED.value}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while closing the ticket."
        )
    
    # Return updated ticket
    return TicketResponse(
        ticket_id=ticket["ticket_id"],
        ticket_number=ticket["ticket_number"],
        title=ticket["title"],
        description=ticket["description"],
        category=ticket["category"],
        priority=ticket["priority"],
        status=TicketStatus.CLOSED,
        created_at=ticket["created_at"],
        owner_id=ticket["owner_id"]
    )
