from pydantic import BaseModel
from datetime import datetime

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

    #add constructor
    def __init__(self, title, description, votes):
        self.id = None  # auto-generated id for each destination
        self.title = title
        self.description = description
        self.votes = votes
        self.created_at = datetime.now()

    id : int
    title: str
    description: str
    votes: int
    created_at: datetime
    # category: Category