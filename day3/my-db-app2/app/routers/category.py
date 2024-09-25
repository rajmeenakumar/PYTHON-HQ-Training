from fastapi import APIRouter, HTTPException, Depends
from .. import schemas, models, database
from sqlalchemy.orm import Session
from .. import  destination_crud, category_crud

router = APIRouter()

@router.post("/", response_model= schemas.Category)
def add_category(category: schemas.Category, db: Session = Depends(database.get_db)):
    print(f"New category added: {category}")
    return category_crud.create_category(db, category)


@router.get("/", response_model=list[schemas.Category])
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    categories = category_crud.get_categories(db, skip, limit)
    return categories;

# @router.get("/{id}", response_model=schemas.Destination)
# def get_destination(id: int, db: Session = Depends(database.get_db)):
#     destination = destination_crud.get_destination_by_id(db, id)
#     if not destination:
#         raise HTTPException(status_code=404, detail="Destination not found")
#     return destination;


# @router.delete("/{id}", response_model=schemas.Destination)
# def delete_destination(id: int, db: Session = Depends(database.get_db)):
#     destination = destination.get_destination_by_id(db, id)
#     if not destination:
#         raise HTTPException(status_code=404, detail="Destination not found")
#     db.delete(destination)
#     db.commit()
#     return destination;


# @router.patch("/destinations/{id}", response_model=schemas.Destination)
# def update_destination(id: int, updated_destination: schemas.DestinationUpdate, db: Session = Depends(database.get_db)):
#     destination = destination.get_destination_by_id(db, id)
#     if not destination:
#         raise HTTPException(status_code=404, detail="Destination not found")
#     destination.votes = updated_destination.votes
#     db.commit()
#     db.refresh(destination)
#     return destination;