#!/usr/bin/python3
""" State Module for HBNB project """
from dis import COMPILER_FLAG_NAMES
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """Amenity class to store amenity information"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')
