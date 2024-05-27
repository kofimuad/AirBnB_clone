#!/usr/bin/python3
"""
Inherits from BaseModel superclass
"""

from models.base_model import BaseModel


class City(BaseModel):
    state_d: str = ""
    name: str = ""
