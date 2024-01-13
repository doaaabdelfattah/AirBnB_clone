#!/usr/bin/python3
''' Unit test for User class
    - test for instantiation
    - test for filStorage
'''

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.user import User
from models.engine.file_storage import FileStorage

# ============ test instantiation ===============
class TestUser_instantiation(unittest.TestCase):
    '''Unittest for User class'''
    
    def test_instantiations(self):
        self.assertEqual(User, type(User()))
        
    # test for attributes
    def test_att_string(self):
        instant = User()
        self.assertEqual(str, type(instant.email))
        self.assertEqual(str, type(instant.password))
        self.assertEqual(str, type(instant.first_name))
        self.assertEqual(str, type(instant.last_name))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_id_notequal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)
        

# ============ test to_dict ===============
class TestBaseModel_to_dict(unittest.TestCase):
    
    def test_type(self):
        instant = User()
        self.assertTrue(dict, type(instant.to_dict))
        
    def test_keys(self):
        instant = User()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())
    
    def test_datetime_string(self):
        instant = User()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))
    
    def test_save(self):
        instant = User()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)

 # ============ test FileStorage handling ===============
# class TestFileStorage_methods(unittest.TestCase):   
#     '''Unit test for FileStorage with User class'''
 
#    # Unittest for new()
#     def test_new_method(self):
#         instant = User()
#         models.storage.new(instant)
#         self.assertIn("User." + instant.id, models.storage.all().keys())
    

#     # Unittest for save()
#     def test_save_method(self):
#         instant = User()
#         models.storage.new(instant)
#         models.storage.save()
#         with open("file.json", "r") as f:
#             self.assertIn("User." + instant.id, f.read())
    
#     # Unittest for reload()
#     def test_save_method(self):
#         instant = User()
#         models.storage.new(instant)
#         models.storage.save()
#         models.storage.reload()
#         self.assertIn("User." + instant.id, FileStorage._FileStorage__objects)
   
        
        

        
        

if __name__ == '__main__':
    unittest.main()