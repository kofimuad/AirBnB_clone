#!/usr/bin/python3
"""
Inherits from superclass BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class inherits from BaseModel"""
    name: str = ""
