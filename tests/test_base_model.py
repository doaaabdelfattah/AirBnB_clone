import unittest
import models
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Unittest for Base_model'''
    def test_instantiations(self):
        self.assertEqual(BaseModel, type(BaseModel()))
    
    def test_id_notequal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)
        
    # def test_str(self):
    #     instant = BaseModel()
    #     self.assertEqual("")


if __name__ == '__main__':
    unittest.main()