#!/usr/bin/python3
"""
Custom BaseModel class for the AirBnb project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id (str): Unique user identity
        created_at: Time for the creation of the instance
        updated_at: Last Update of the instance.

    Methods:
        __str__: Returns string representation of the instance
        save(self): updates 'updated_at' with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    
    def __init__(self, *args, **kwargs):
        """initialize a public instance"""
        #convert id value to string
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        # Create dictionary from input arguments
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    # Convert datetime string into obj
                    # strptime is class method so we call it on datetime
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:        
                    # add items to dict
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def __str__(self):
        """return string representation of obj"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    def save(self):
        """update the updated_at to current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation"""
        data_copied = self.__dict__.copy()
        #to access name of class
        data_copied["__class__"] = self.__class__.__name__
        #Convert to ISO format
        data_copied["created_at"] = self.created_at.isoformat()
        data_copied["updated_at"] = self.updated_at.isoformat()
        #return the dictionary
        return data_copied
