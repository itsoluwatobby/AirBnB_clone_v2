#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Attributes:
        __tablename__(str): Table name
        email(str): User's email cant be null
        password(str): The user password, cant be null
        first_name(str): User's first name
        last_name(str): User's last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
