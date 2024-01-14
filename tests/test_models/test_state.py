#!/usr/bin/python3
''' Unit test for State class
    - test for instantiation
    - test for to_dict
'''

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.state import State
from models.engine.file_storage import FileStorage

# ============ test instantiation ===============


class TestState_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        self.assertEqual(State, type(State()))

    # test for attributes
    def test_att_string(self):
        instant = State()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))


def test_id_notequal(self):
    id1 = BaseModel()
    id2 = BaseModel()
    self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestState_to_dict(unittest.TestCase):
    '''Unittest for class'''

    def test_type(self):
        instant = State()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = State()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = State()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = State()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)
