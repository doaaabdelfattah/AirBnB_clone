#!/usr/bin/python3
'''custome a user class that inhirets from BasModel'''
from models.base_model import BaseModel
class User(BaseModel):
    """a User class

    Attrs:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    