# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .database import Base
from sqlalchemy.orm import relationship

# Base = declarative_base()

class Destination(Base):
    __tablename__ = "destinations"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(100), index=True)
    votes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)

    category_id = Column(Integer, ForeignKey('categories.id'))  # Foreign key to Category
    category = relationship("Category", back_populates="destinations")  # Relationship to Category


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    destinations = relationship("Destination", back_populates="category")  # Relationship to Destinations