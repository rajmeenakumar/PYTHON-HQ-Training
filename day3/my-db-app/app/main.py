from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schema, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/hello")
def sayHello():
    return "hello"

# get for destinations 
@app.get("/destinations", response_model=list[schema.Destination])
def get_destinations(db: Session = Depends(get_db)):
    destinations = crud.get_destinations(db)
    return destinations

@app.post("/destinations", response_model=schema.Destination)
def create_destination(destination : schema.DestinationCreate, db: Session = Depends(get_db)):
    destination = crud.create_destination(db, destination )
    return destination
