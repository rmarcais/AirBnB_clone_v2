#!/usr/bin/python3
"""place.py
This module defines the class State.
"""

from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This class defines the attribut of the place"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """reviews attribute"""

            liste = []
            objs = models.storage.all(Review)

            for k, v in objs.items():
                if v.place_id == self.id:
                    liste.append(v)
            return liste

        @property
        def amenities(self):
            """getter attributes for amenity"""
            liste = []
            objs = models.storage.all(Amenity)

            for k, v in objs.items():
                if v.amenity_id == self.id:
                    liste.append(v)
            return liste

        @amenities.setter
        def amenities(self, obj):
            """setter attribut for amenities"""
            if (type(obj).__name__ == "Amenity"):
                self.amenity_ids.append(obj.id)
