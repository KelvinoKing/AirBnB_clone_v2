#!/usr/bin/python3
"""This module defines the DBStorage class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """THis class manages storage of hbnb models in a MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and the current database session
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        """
        classes = [User, State, City, Amenity, Place, Review]
        result_dict = {}

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result_dict[key] = obj

        else:
            for class_item in classes:
                query_result = self.__session.query(class_item).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result_dict[key] = obj

        return result_dict

    def new(self, obj):
        """Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current
        database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
