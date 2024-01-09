#!/usr/bin/python3
"""
FileStorage class
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    
    def __init__(self):
        pass
    
    def all(self):
        ''' returns the dictionary __objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        ''' sets in __objects dictionary '''
        obj_class = obj.__class__.__name__
        obj_id = obj.id
        key = f"{obj_class}.{obj_id}"
        self.__objects[key] = obj
        
    def save(self):
        ''' serializes __objects to the JSON file '''
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
       ''' deserializes the JSON file to __objects'''
        with open(self.__file_path, 'r') as f:
            return (json.load(f))