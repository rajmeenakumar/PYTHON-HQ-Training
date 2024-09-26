from fastapi import APIRouter, HTTPException, Depends, Request
from .. import schemas, models, database
from sqlalchemy.orm import Session
from app.curds import category_crud
# from app.middlewares import jwt_middleware
from app.middlewares.query_middleware import advanced_query_middleware  # Import the query middleware
from app.middlewares.authorization_middleware import authorize_role

router = APIRouter()

@router.post("/", response_model=schemas.Category)
def add_category(category: schemas.Category, 
                 db: Session = Depends(database.get_db),
                 role_check: None = Depends(authorize_role(["admin"]))
                 ):  
    print(f"New category added: {category}")
    return category_crud.create_category(db, category)

@router.get("/", response_model=list[schemas.Category])
def get_categories(request: Request, 
                   db: Session = Depends(database.get_db),
                   role_check: None = Depends(authorize_role(["admin", "user"]))):  
    # Use the advanced_query_middleware for building the query
    query = advanced_query_middleware(db, request, models.Category)
    categories = query.all()  # Execute the built query
    return categories
