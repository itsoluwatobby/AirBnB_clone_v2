#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """
    State class
    Attributes:
        __tablename__(str): table name
        name(str): The name of the State
        cities: Relationship between city and state
    """
    if models.storage_n == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_n == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            '''method for cities from storage'''
            cities = models.storage.all(City).values()
            cities_list = [city for city in cities if self.id == city.state_id]
            return cities_list
