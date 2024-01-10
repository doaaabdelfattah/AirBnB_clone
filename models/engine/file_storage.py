#!/usr/bin/python3
"""
FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
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
       ''' deserializes the JSON file to __objects
       if the JSON file exists, otherwise pass
       '''
       try:
           with open(FileStorage.__file_path, 'r') as f:
                Current_dict = json.loads(f.read())
            ####### Adjust function #####
                for value in Current_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
       except FileNotFoundError:
            # If the file doesn’t exist, no exception should be raised)
           pass
