from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.item import Item, ItemCreate
from app.database import item_collection
from bson import ObjectId
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate, user: dict = Depends(get_current_user)):
    new_item = item.dict()
    new_item["_id"] = str(ObjectId())
    new_item["owner_id"] = user["_id"]
    result = await item_collection.insert_one(new_item)
    return new_item

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: str):
    item = await item_collection.find_one({"_id": item_id})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")


# # get operation for items with item price greater than a given price
# @router.get("/price/{price}", response_model=List[Item])
#     items = await item_collection.find({"price": {"$gt": price}}).to_list(length=10)
#     return items


# @router.get("/search/{item_name}", response_model=List[Item])
# async def search_item(item_name: str):
#     items = await item_collection.find({"name": {"$regex": f"^{item_name}", "$options": "i"}}).to_list(length=10)
#     return items 

@router.get("/", response_model=List[Item])
async def list_items(skip: int = 0, limit: int = 10):
    items = await item_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return items


# create delete operation for items

@router.delete("/{item_id}", response_model=Item)
async def delete_item(item_id: str, user: dict = Depends(get_current_user)):
    item = await item_collection.find_one({"_id": item_id, "owner_id": user["_id"]})
    if item:
        await item_collection.delete_one({"_id": item_id})