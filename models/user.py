#!/bin/usr/python3
"""
Model for User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Handles user information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
