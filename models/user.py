#!/usr/bin/python3
"""This module defines a class User"""
import models
import hashlib
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
    if models.storage_n == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, __name: str, __value) -> None:
        '''Sets an attribute of this class to a given value.'''
        if __name == 'password':
            if type(__value) is str:
                m = hashlib.md5(bytes(__value, 'utf-8'))
                super().__setattr__(__name, m.hexdigest())
        else:
            super().__setattr__(__name, __value)
