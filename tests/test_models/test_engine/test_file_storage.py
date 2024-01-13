import unittest
import models
import json
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage_instantiation(unittest.TestCase):
    '''Unittest for FileStorage class'''
    
    def test_instantiations(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
    
    def test_obj_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_var(self):
        self.assertEqual(FileStorage, type(models.storage))
        


if __name__ == '__main__':
    unittest.main()