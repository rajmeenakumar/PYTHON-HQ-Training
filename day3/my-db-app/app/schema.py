from datetime import datetime
from pydantic import BaseModel

class Destination(BaseModel):
    id: int
    title: str
    description: str
    votes: int
    # created_at: datetime

class DestinationCreate(BaseModel):
    title: str
    description: str
    votes: int
    
    

