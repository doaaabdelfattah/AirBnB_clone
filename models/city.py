#!/usr/bin/python3
'''custome a city class that inhirets from BasModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    a cityclass inhirets from BaseModel
    Attrs:
    state_id: id of namestate
    name: name of state
    '''
    state_id = ""
    name = ""
