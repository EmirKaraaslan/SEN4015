from app.routers.loginSystem import router as loginSystem_router
from app.routers.createUser import router as createUser_router
from app.routers.createTicket import router as createTicket_router
from app.routers.getCustomTickets import router as getCustomTickets_router
from app.routers.getAllTickets import router as getAllTickets_router
from app.routers.closeTicket import router as closeTicket_router

__all__ = [
    "loginSystem_router",
    "createUser_router", 
    "createTicket_router",
    "getCustomTickets_router",
    "getAllTickets_router",
    "closeTicket_router"
]
