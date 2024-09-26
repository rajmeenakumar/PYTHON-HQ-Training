from fastapi import APIRouter, HTTPException, Depends, Request
from .. import schemas, models, database
from sqlalchemy.orm import Session
from app.curds import destination_crud
from app.middlewares.query_middleware import advanced_query_middleware  # Import the query middleware
from app.middlewares.authorization_middleware import authorize_role

router = APIRouter()

@router.post("/", response_model=schemas.Destination)
def add_destination(destination: schemas.DestinationCreate, 
                    db: Session = Depends(database.get_db),
                    role_check: None = Depends(authorize_role(["admin"]))): 
    print(f"New destination added: {destination}")
    return destination_crud.create_destination(db, destination)

@router.get("/", response_model=list[schemas.Destination])
def get_destinations(request: Request, 
                     db: Session = Depends(database.get_db),
                     role_check: None = Depends(authorize_role(["admin", "user"]))):  
    # Use the advanced_query_middleware for building the query
    query = advanced_query_middleware(db, request, models.Destination)
    destinations = query.all()  # Execute the built query
    return destinations

@router.get("/{id}", response_model=schemas.Destination)
def get_destination(id: int, 
                    db: Session = Depends(database.get_db),
                    role_check: None = Depends(authorize_role(["admin", "user"]))):  
    destination = destination_crud.get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

@router.delete("/{id}", response_model=schemas.Destination)
def delete_destination(id: int, 
                       db: Session = Depends(database.get_db),
                       role_check: None = Depends(authorize_role(["admin"]))):  
    destination = destination_crud.get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    db.delete(destination)
    db.commit()
    return destination

@router.patch("/destinations/{id}", response_model=schemas.Destination)
def update_destination(id: int, 
                       updated_destination: schemas.DestinationUpdate, 
                       db: Session = Depends(database.get_db),
                       role_check: None = Depends(authorize_role(["admin"]))): 
    destination = destination_crud.get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    destination.votes = updated_destination.votes
    db.commit()
    db.refresh(destination)
    return destination
