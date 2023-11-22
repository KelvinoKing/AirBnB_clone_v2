#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Table, Integer, Float, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata, Column(
    'place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review', backref='place', cascade='all, delete-orphan')
        amenities = relationship(
                'Amenity', secondary=place_amenity, viewonly=False)

    @property
    def review(self):
        from models import storage
        return [review for review in storage.all(
            "Review").values() if review.place_id == self.id]

    @property
    def amenities(self):
        from models import storage
        return [storage.get('Amenity', amenity_id) for amenity_id in getattr(
            self, 'amenity_ids', [])]

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            amenity_ids = getattr(self, 'amenity_ids', [])
            if amenity_id not in amenity_ids:
                amenity_ids.append(amenity_id)
                self.amenity_ids = amenity_ids
                self.save()
