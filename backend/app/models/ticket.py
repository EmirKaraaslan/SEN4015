from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime


class TicketCategory(str, Enum):
    """Ticket category enum definition."""
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    NETWORK = "Network"


class TicketPriority(str, Enum):
    """Ticket priority enum definition."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class TicketStatus(str, Enum):
    """Ticket status enum definition."""
    PENDING = "Pending"
    CLOSED = "Closed"


# ============== Request Models (Create) ==============

class TicketCreate(BaseModel):
    """Schema for creating a new ticket."""
    title: str = Field(..., min_length=1, max_length=200, description="Ticket title")
    description: str = Field(..., min_length=1, description="Ticket description")
    category: TicketCategory = Field(..., description="Ticket category (Hardware or Software)")
    priority: TicketPriority = Field(default=TicketPriority.MEDIUM, description="Ticket priority")
    owner_id: str = Field(..., description="User ID of the ticket owner")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Laptop screen not working",
                "description": "Dell Latitude 5520 laptop screen won't turn on. Power light is on but screen is black.",
                "category": "Hardware",
                "priority": "High",
                "owner_id": "U001"
            }
        }


class TicketClose(BaseModel):
    """Schema for closing a ticket (admin only)."""
    admin_id: str = Field(..., description="Admin user ID performing the operation")
    
    class Config:
        json_schema_extra = {
            "example": {
                "admin_id": "A001"
            }
        }


# ============== Response Models (Read) ==============

class TicketResponse(BaseModel):
    """Schema for ticket response."""
    ticket_id: str
    ticket_number: str
    title: str
    description: str
    category: TicketCategory
    priority: TicketPriority
    status: TicketStatus
    created_at: datetime
    owner_id: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "ticket_id": "65f1a2b3c4d5e6f7g8h9i0j1",
                "ticket_number": "T-1001",
                "title": "Laptop screen not working",
                "description": "Dell Latitude 5520 laptop screen won't turn on.",
                "category": "Hardware",
                "priority": "High",
                "status": "Pending",
                "created_at": "2024-01-15T10:30:00",
                "owner_id": "U001"
            }
        }


# ============== Database Model ==============

class TicketInDB(BaseModel):
    """Schema for ticket stored in database."""
    ticket_id: str
    ticket_number: str
    title: str
    description: str
    category: TicketCategory
    priority: TicketPriority
    status: TicketStatus = TicketStatus.PENDING
    created_at: datetime
    owner_id: str
