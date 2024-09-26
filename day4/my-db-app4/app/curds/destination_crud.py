from .. import models
from .. import schemas
from sqlalchemy.orm import Session

#create destination method
def create_destination(db: Session, destination: schemas.DestinationCreate):
    db_destination = models.Destination(**destination.dict())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination



#get all destinations method
def get_destinations(db: Session, skip, limit):
    return db.query(models.Destination).offset(skip).limit(limit).all()



#get destination by id method
def get_destination_by_id(db: Session, destination_id: int):
    return db.query(models.Destination).filter(models.Destination.id == destination_id).first()