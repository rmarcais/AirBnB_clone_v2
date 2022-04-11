#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from tkinter import CASCADE
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        @property
        def cities(self):
            """getter attribute that returns the
            list of City instances with state_id equals to
            the current State.id"""
            l = []
            dico = models.storage.all(City)
            for key, value in dico.items():
                if value.state_id == self.id:
                    l.append(value)
            return l
