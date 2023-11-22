#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class for all amenities
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = Table('place_amenities', Base.metadata, Column(
        'place_id', String(60), ForeignKey('place.id'), primary_key=True),
        Column(
            'amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True))

    place = relationship(
            'Place', secondary=place_amenities, back_populates='amenities')
