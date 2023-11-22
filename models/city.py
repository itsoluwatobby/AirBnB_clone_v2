#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    Attributes:
        __tablename__(str): table name
        name(str): Name of the city. String 128 chars and can't be null
        state_id(str): The id of state city is in can't be nul 60 chars
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship("Place", backref="cities", cascade="all, delete")
