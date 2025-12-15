from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    """User role enum definition."""
    ADMIN = "admin"
    USER = "user"


# ============== Request Models (Create) ==============

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    user_id: str = Field(..., description="Unique user identifier")
    first_name: str = Field(..., min_length=1, max_length=50, description="User's first name")
    last_name: str = Field(..., min_length=1, max_length=50, description="User's last name")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=1, description="User's password (stored as plain text)")
    department: str = Field(..., min_length=1, max_length=100, description="User's department")
    role: UserRole = Field(default=UserRole.USER, description="User's role (admin or user)")


class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password")


# ============== Response Models (Read) ==============

class UserResponse(BaseModel):
    """Schema for user response (excluding password)."""
    user_id: str
    first_name: str
    last_name: str
    email: EmailStr
    department: str
    role: UserRole


class LoginResponse(BaseModel):
    """Schema for login response."""
    success: bool
    message: str
    user: Optional[UserResponse] = None


# ============== Database Model ==============

class UserInDB(BaseModel):
    """Schema for user stored in database (including password)."""
    user_id: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str  # Plain text password
    department: str
    role: UserRole
