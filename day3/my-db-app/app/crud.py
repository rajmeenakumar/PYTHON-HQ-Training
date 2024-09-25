from sqlalchemy.orm import Session
from . import models, schema

def get_destinations(db: Session):
    return db.query(models.Destinations).all()

def create_destination(db: Session, destination: schema.DestinationCreate):
    db_destination = models.Destinations(**destination.dict())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination
    