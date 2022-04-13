#!/usr/bin/python3
"""amenity.py
This module defines the class Amenity.
"""


from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This class defines the name of the amenity"""
    if getenv("HBNB_STORAGE_TYPE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    name = ""
