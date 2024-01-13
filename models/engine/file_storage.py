#!/usr/bin/python3
"""
FileStorage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
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
       try:
           with open(FileStorage.__file_path, 'r') as f:
            if os.path.getsize(self.__file_path) > 0:
                Current_dict = json.load(f)
                '''loop through all objects in Current_dict'''
                for value in Current_dict.values():
                    '''extract the class name from object keys as string'''
                    cls_name = value["__class__"]
                    '''Remove the "__class__"
                        key from the dictionary as it'not necessary'''
                    del value["__class__"]
                    '''(eval) evaluate cls_name
                        and save its class object from this class'''
                    obj_class = eval(cls_name)
                    '''create new instance using
                        (**value): unpacking dict value as kwargs'''
                    '''Then pass them to cls constructor'''
                    new_instance = obj_class(**value)
                    '''The new method is called with
                            the newly created object as an argument to
                            add it to the __objects dictionary.'''
                    self.new(new_instance)
       except FileNotFoundError:
        return
