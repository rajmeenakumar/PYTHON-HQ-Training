from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/hello")
def sayHello():
    return "hello"