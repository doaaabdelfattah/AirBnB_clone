import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser_instantiation(unittest.TestCase):
    '''Unittest for User class'''
    
    # test for instantiation
    def test_instantiations(self):
        self.assertEqual(User, type(User()))
        
    # test for attributes
    def test_att_string(self):
        instant = User()
        self.assertTrue(str, type(instant.email))
        self.assertTrue(str, type(instant.password))
        self.assertTrue(str, type(instant.first_name))
        self.assertTrue(str, type(instant.last_name))

    
    
    
    # test to_dict
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
    
    
    # test for save   
class TestBaseModel_save(unittest.TestCase):
    ''' unittest for save method''' 
    def test_save(self):
        instant = User()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)
        
   
class TestFileStorage_methods(unittest.TestCase):   
    '''Unit test for FileStorage with User class'''
 
   # Unittest for new()
    def test_new_method(self):
        instant = User()
        models.storage.new(instant)
        self.assertIn("User." + instant.id, models.storage.all().keys())
    

    # Unittest for save()
    def test_save_method(self):
        instant = User()
        models.storage.new(instant)
        models.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("User." + instant.id, f.read())
    
    # Unittest for reload()
    def test_save_method(self):
        instant = User()
        models.storage.new(instant)
        models.storage.save()
        models.storage.reload()
        self.assertIn("User." + instant.id, FileStorage._FileStorage__objects)
   
        
        

        
        

if __name__ == '__main__':
    unittest.main()