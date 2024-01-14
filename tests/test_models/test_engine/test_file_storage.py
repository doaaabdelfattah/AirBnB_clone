#!/usr/bin/python3
"""
FileStorage class
"""
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


class TestFileStorage_methods(unittest.TestCase):
    '''unittest for FileStorage methods'''

    '''Unittest for all()'''
    def test_dict_type(self):
        instant = FileStorage
        self.assertEqual(dict, type(models.storage.all()))

    '''Unittest for new()'''
    def test_new_method(self):
        instant = BaseModel()
        models.storage.new(instant)
        self.assertIn("BaseModel." + instant.id, models.storage.all().keys())

    '''Unittest for save()'''
    def test_save_method(self):
        instant = BaseModel()
        models.storage.new(instant)
        models.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + instant.id, f.read())

    '''Unittest for reload()'''
    def test_save_method(self):
        instant = BaseModel()
        models.storage.new(instant)
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel." + instant.id,
                      FileStorage._FileStorage__objects)

    '''unittest for no file'''
    def test_reload_no_file(self):
        self.assertTrue(FileNotFoundError, models.storage.reload)
        

if __name__ == '__main__':
    unittest.main()
