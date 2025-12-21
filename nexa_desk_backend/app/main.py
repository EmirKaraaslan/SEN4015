from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import connect_to_mongo, close_mongo_connection

# Import modular API routers
from app.routers.loginSystem import router as loginSystem_router
from app.routers.createUser import router as createUser_router
from app.routers.createTicket import router as createTicket_router
from app.routers.getCustomTickets import router as getCustomTickets_router
from app.routers.getAllTickets import router as getAllTickets_router
from app.routers.closeTicket import router as closeTicket_router
from app.routers.getAllUsers import router as getAllUsers_router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events."""
    # Startup: Connect to MongoDB
    await connect_to_mongo()
    yield
    # Shutdown: Close MongoDB connection
    await close_mongo_connection()


# Create FastAPI application
app = FastAPI(
    title="Ticket Tracking System API",
    description="""
    🎫 **Ticket Tracking System** - A lightweight request management system similar to ServiceNow.
    
    ## 6 Modular APIs
    
    * **loginSystem** - User/Admin login operations
    * **createUser** - Create new user (Postman/Terminal)
    * **createTicket** - Create new ticket
    * **getCustomTickets** - Retrieve user's own tickets
    * **getAllTickets** - List all tickets (Admin)
    * **closeTicket** - Close ticket (Admin)
    
    ## User Roles
    
    * **admin** - Permission to view and close all tickets
    * **user** - Create and view own tickets
    """,
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration  , canlıya alırsan zaman burayı güncelle
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include modular API routers
app.include_router(loginSystem_router)      # POST /auth/loginSystem
app.include_router(createUser_router)       # POST /users/createUser
app.include_router(createTicket_router)     # POST /tickets/createTicket
app.include_router(getCustomTickets_router) # GET /tickets/getCustomTickets
app.include_router(getAllTickets_router)    # GET /tickets/getAllTickets
app.include_router(closeTicket_router)      # PUT /tickets/closeTicket/{ticket_id}
app.include_router(getAllUsers_router)      # GET /users/getAllUsers

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - API health check."""
    return {
        "message": "🎫 Ticket Tracking System API",
        "status": "active",
        "version": "1.0.0",
        "docs": "/docs",
        "apis": [
            "loginSystem",
            "createUser",
            "createTicket",
            "getCustomTickets",
            "getAllTickets",
            "closeTicket"
        ]
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "ticket-tracking-api"
    }
