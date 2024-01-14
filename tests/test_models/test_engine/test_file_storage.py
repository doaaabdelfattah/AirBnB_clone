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
        '''Unittest for FileStorage class'''
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path(self):
        '''Unittest for FileStorage class'''
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_obj_dict(self):
        '''Unittest for FileStorage class'''
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_var(self):
        '''Unittest for FileStorage class'''
        self.assertEqual(FileStorage, type(models.storage))


class TestFileStorage_methods(unittest.TestCase):
    '''unittest for FileStorage methods'''

    def test_dict_type(self):
        '''Unittest for all()'''
        instant = FileStorage
        self.assertEqual(dict, type(models.storage.all()))

    def test_new_method(self):
        '''Unittest for new()'''
        instant = BaseModel()
        models.storage.new(instant)
        self.assertIn("BaseModel." + instant.id, models.storage.all().keys())

    def test_save_method(self):
        '''Unittest for save()'''
        instant = BaseModel()
        models.storage.new(instant)
        models.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + instant.id, f.read())

    def test_save_method(self):
        '''Unittest for reload()'''
        instant = BaseModel()
        models.storage.new(instant)
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel." + instant.id,
                      FileStorage._FileStorage__objects)

    def test_reload_no_file(self):
        ''' test reload - nofile'''
        self.assertTrue(FileNotFoundError, models.storage.reload)

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(None, models.storage.reload())

if __name__ == '__main__':
    unittest.main()
