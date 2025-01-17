#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import inspect
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
from datetime import datetime
import os

if models.storage_n == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    A base class for all hbnb models

    Attributes:
        id(str): A unique string, can't be null primary key
        created_at(datetime): Current datetime
        updated_at(datetime): The date the object was updated
    """
    if models.storage_n == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), default=datetime.utcnow())
        updated_at = Column(DateTime(), default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        storage.delete(self)
