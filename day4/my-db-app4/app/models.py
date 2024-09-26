from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    role = Column(String(20), default='user')  # Role: 'admin' or 'user'
    created_at = Column(DateTime, default=datetime.now)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    destinations = relationship("Destination", back_populates="category")  # Relationship to Destinations

class Destination(Base):
    __tablename__ = "destinations"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(100), index=True)
    votes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="destinations")  # Relationship to Category
