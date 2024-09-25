from . import models
from . import schemas
from sqlalchemy.orm import Session

#create destination method
def create_category(db: Session, category: schemas.Category):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category;

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category_by_id(db: Session, id: int):
    return db.query(models.Category).filter(models.Category.id == id).first()