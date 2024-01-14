#!/usr/bin/python3
''' Unit test for City class
    - test for instantiation
    - test for to_dict
'''

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.city import City
from models.engine.file_storage import FileStorage

# ============ test instantiation ===============


class TestCity_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        self.assertEqual(City, type(City()))

    # test for attributes
    def test_att_string(self):
        instant = City()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.state_id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_id_notequal(self):
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestCity_to_dict(unittest.TestCase):
    '''Unittest for User class'''

    def test_type(self):
        instant = City()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = City()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = City()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = City()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)
