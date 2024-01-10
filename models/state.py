#!/usr/bin/python3
'''custome a State class that inhirets from BasModel'''
from models.base_model import BaseModel
class State(BaseModel):
    '''
    a State class inhirets from BaseModel
    
    Attrs:
    name: name of state
    '''
    name = ""