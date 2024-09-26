from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
 
# class Category(BaseModel):
#     title: str

# class DestinationCreate(BaseModel):
#     # add constructor
#     title: str
#     description: str
#     votes: int
#     category_id: int = None  # foreign key to Category table


# class DestinationUpdate(BaseModel):
#     votes: int

# class Destination(BaseModel):

#     #add constructor
#     def __init__(self, title, description, votes):
#         self.id = None  # auto-generated id for each destination
#         self.title = title
#         self.description = description
#         self.votes = votes
#         self.created_at = datetime.now()

#     id : int
#     title: str
#     description: str
#     votes: int
#     created_at: datetime
#     category: Category




class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    class Config:
        orm_mode = True

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class DestinationBase(BaseModel):
    title: str
    description: str
    votes: int


class DestinationCreate(DestinationBase):
    category_id: Optional[int] = None  # Foreign key to Category


class DestinationUpdate(BaseModel):
    votes: int


class Destination(DestinationBase):
    id: int
    created_at: datetime
    category: Optional[Category] = None  # Add the relationship with Category

    class Config:
        orm_mode = True


