from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import user_collection
from app.utils.auth import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await user_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["_id"]})
    return {"access_token": token, "token_type": "bearer"}
