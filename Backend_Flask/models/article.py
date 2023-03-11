#!/usr/bin/python3
"""
"""
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import DeclarativeBase
import uuid

"""# declarative base class
class Base(DeclarativeBase):
    pass"""

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class Article(Base):
    """
    """
    __tablename__ = 'articles'
    id = Column(String(60), primary_key=True)
    title = Column(String(100))
    body = Column(Text())
    date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            
            if kwargs.get("date", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.date = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.title = title
            self. body = body
            date = datetime.utcnow()

    def save(self):
        """updates the attribute 'date' with the current datetime"""
        self.date = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
