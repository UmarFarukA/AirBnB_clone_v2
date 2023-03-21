#!/usr/bin/python3
"""Represent a relationship between place & amenity"""
from sqlalchemy import Table
from sqlalchemy import ForeignKey

place_amenity = Table("place_amenity", metadata=Base.metadata
                      Column("place_id", ForeignKey("places_id"),
                             primary_key=True)
                      Column("amenity_id", ForeignKey("amenities_id"),
                             primary_key=True)
                      )
