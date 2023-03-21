#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, ForeignKey("places_id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    text = Column(String(1024), nullable=False)
