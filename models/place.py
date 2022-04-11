#!/usr/bin/python3
""" Place Module for HBNB project """
from ctypes import FormatError
import string

from colorama import Fore
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models
from sqlalchemy import *

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey='places.id', nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey='amenities.id', nullable=False))


class Place(BaseModel):
    """ A place to stay """
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

    if getenv("HBTN_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref="Place",
                               cascade="all, delete_orphan")
        amenities = relationship('Amenity', backref="Place",
                                 secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attributes for reviews"""
            for review in models.storage.all(Review):
                if review.place_id == self.id:
                    return review.place_id

        @property
        def amenities(self):
            """getter attributes for amenity"""
            for amenit in models.storage.all(Amenity):
                if amenit.id in self.amenity_ids:
                    return amenit.id

        @amenities.setter
        def amenities(self, obj):
            """setter attribute for amenities"""
            if (type(obj) == Amenity):
                self.amenity_ids.append(obj.id)
