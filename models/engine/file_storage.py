#!/usr/bin/python3
"""
FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
class FileStorage:
    __file_path = 'file.json'
    # __objects: (dict key is clsname,id and the value is a dict of object)
    __objects = {}
    
    def __init__(self):
        pass
    
    def all(self):
        ''' returns the dictionary __objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        ''' adding objects to the __objects dictionary '''
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
                Current_dict = json.load(f)
            # loop through all objects in Current_dict
                for value in Current_dict.values():
                    # extract the class name from object keys as string
                    cls_name = value["__class__"]
                    # Remove the "__class__" key from the dictionary as it'not necessary 
                    del value["__class__"]
                    # (eval) evaluate cls_name and save its class object from this class
                    obj_class = eval(cls_name)
                    # create new instance using (**value): unpacking dict value as kwargs
                    # Then pass them to cls constructor
                    new_instance = obj_class(**value)
                    # The new method is called with the newly created object as an argument to add it to the __objects dictionary.
                    self.new(new_instance)
       except FileNotFoundError:
            # If the file doesn’t exist, no exception should be raised)
           return
