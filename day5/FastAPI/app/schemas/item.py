from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    tax: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    _id: str
    owner_id: str