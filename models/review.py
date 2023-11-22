#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os


class Review(BaseModel, Base):
    """
    Review classto store review information
    Attributes:
        __tablename__(str): Table name
        text(str): User's email cant be null
        place_id(str): place id, cant be null
        user_id(str): User's id, not null
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
