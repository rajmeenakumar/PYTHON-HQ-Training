from fastapi import APIRouter, HTTPException
from app.schemas.user import User, UserCreate
from app.database import user_collection
from bson import ObjectId
from app.utils.auth import hash_password

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["_id"] = str(ObjectId())
    await user_collection.insert_one(user_dict)
    return user_dict

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await user_collection.find_one({"_id": user_id})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
