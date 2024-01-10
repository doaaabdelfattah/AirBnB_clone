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
        FileStorage.__objects[key] = obj
        
    def save(self):
        ''' serializes __objects to the JSON file '''        
        json_data = {}
        for key, value in FileStorage.__objects.items():
            json_data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_data, f)


    def reload(self):
       ''' deserializes the JSON file to __objects'''
       try:
           with open(FileStorage.__file_path, 'r') as f:
                dict = json.load(f)
            ####### Adjust function #####
       except FileNotFoundError:
            # If the file doesn’t exist, no exception should be raised)
           pass
