#!/usr/bin/python3
"""
Inherits from BaseModel superclass
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
