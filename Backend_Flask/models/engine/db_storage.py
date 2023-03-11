#!/usr/bin/python3
"""File for database
"""
import models
from models.article import Base, Article
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    """interacts with the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object
        """
        self.__engine = create_engine('mysql+mysqldb://flask:flask_pwd@localhost/flaskDb')

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        objs = self.__session.query(Article).all()
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        count = len(models.storage.all(Article).values())
        return count
