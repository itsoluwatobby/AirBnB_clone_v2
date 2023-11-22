#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Amenity class
     Attributes:
        __tablename__(str): Table name
        name(str): User's email cant be null
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        place_amenities = relationship("Place", secondary='place_amenity',
                                       back_populates="amenities")
