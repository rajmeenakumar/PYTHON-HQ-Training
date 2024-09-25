# import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Destinations(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, index=True)
    description = Column(String(100))
    votes = Column(Integer, default=0)
    # created_at = Column(DateTime, default=datetime.now)