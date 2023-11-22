#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    A place to stay
    
    Attributes:
        __tablename__(str): Table name
        name(str): name of place, cant be null
        city_id(str): city id, cant be null
        user_id(str): User's id, not null
        description(str): description of place
        number_rooms(int): number of rooms, cant be null
        number_bathrooms(int): number of bathrooms, cant be null
        max_guest(int): number of guest, not null
        price_by_night(int): price of place at night, cant be null
        latitude(float): latitude of place
        longitude(float): longitude of place
        amenity_id(list): list of amenities id
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float())
    longitude = Column(Float())
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, back_populates='place_amenities')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            '''method for retrieving reviews from file storage'''
            reviews = models.storage.all(Review).values()
            _list = [rev for rev in reviews if self.id == rev.place_id]
            return _list

        @property
        def amenities(self):
            '''
            returns a list of Amenity instances based on amenity_ids
            linked to a Place
            '''
            amens = models.storage.all(Amenity).values()
            _list = [ameni for ameni in amens if amen.id in self.amenity_ids]
            return _list

        @amenities.setter
        def amenities(self, obj):
            '''
            handles append method for adding an Amenity.id to the attribute
            amenity_ids.
            '''
            if obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
