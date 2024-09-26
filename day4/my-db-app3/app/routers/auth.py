
from app.database import get_db
from fastapi import APIRouter, Depends
from app.schemas import UserCreate, UserResponse
from app.models import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/register', response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

