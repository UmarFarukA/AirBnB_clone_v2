#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """Represents the Amenity class
    __tablename__: defines the table name
    name (sqlalchemy colum): define column name
    """
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity"
                                   viewonly=False)
