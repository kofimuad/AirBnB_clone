#!/usr/bin/python3
"""
Inherits from superclass BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity inherits from BaseModel"""
    name: str = ""
