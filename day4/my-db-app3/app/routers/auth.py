
from passlib.hash import bcrypt
from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import UserCreate, UserLogin, UserResponse
from app.models import User
from sqlalchemy.orm import Session
from app.utils.jwt_handler import create_token

router = APIRouter()

@router.post('/register', response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)
    db_user = User(**user.dict(exclude={"password"}), password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user

@router.post('/login')
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user and bcrypt.verify(user.password, db_user.password):
        token = create_token(db_user.id);
        return {"token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect email or password")

