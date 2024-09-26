from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str


class Category(BaseModel):
    title: str

class DestinationCreate(BaseModel):
    # add constructor
    title: str
    description: str
    votes: int
    category_id: int = None  # foreign key to Category table


class DestinationUpdate(BaseModel):
    votes: int

class Destination(BaseModel):
    id : int
    # title: str
    #title optional to avoid circular reference
    title: Optional[str] = None
    description:  Optional[str] = None
    votes: Optional[int] = None
    created_at: Optional[datetime] = None
    category: Optional[Category] = None
    