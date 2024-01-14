#!/usr/bin/python3
"""
Unittest class
"""
import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    '''Unittest for Base_model'''
    def test_instantiations(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_notequal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    # def test_str_representation(self):
    #     date = datetime.today()
    #     dt_repr = repr(date)
    #     bm = BaseModel()
    #     bm.id = "000-111-222-333"
    #     bm.created_at = bm.updated_at = date
    #     instant_str = bm.__str__()
    #     self.assertIn("[BaseModel] (000-111-222-333)", instant_str)
    #     self.assertIn("'id': '000-111-222-333'", instant_str)
    #     self.assertIn("'created_at': " + dt_repr, instant_str)
    #     self.assertIn("'updated_at': " + dt_repr, instant_str)


class TestBaseModel_to_dict(unittest.TestCase):
    ''' unittest for to_dict method'''

    def test_type(self):
        instant = BaseModel
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = BaseModel()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = BaseModel()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))


class TestBaseModel_save(unittest.TestCase):
    ''' unittest for save method'''

    def test_save(self):
        instant = BaseModel()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
