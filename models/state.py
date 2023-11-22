#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City', backref='state', cascade='all, delete-orphan')
    else:
        # For FileStorage
        @property
        def cities(self):
            """Getter attr that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            city_list = []
            city_instances = storage.all('City')
            for city in city_instances.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
