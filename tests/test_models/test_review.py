#!/usr/bin/python3
''' Unit test for Review class
    - test for instantiation
    - test for to_dict
'''

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.review import Review
from models.engine.file_storage import FileStorage

# ============ test instantiation ===============


class TestReview_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_instantiations(self):
        self.assertEqual(Review, type(Review()))

    # test for attributes
    def test_att_string(self):
        instant = Review()
        self.assertEqual(str, type(instant.place_id))
        self.assertEqual(str, type(instant.user_id))
        self.assertEqual(str, type(instant.text))
        self.assertEqual(str, type(instant.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_id_notequal(self):
        id1 = Review()
        id2 = Review()
        self.assertNotEqual(id1.id, id2.id)


# ============ test to_dict ===============
class TestReview_to_dict(unittest.TestCase):
    '''Unittest for class'''

    def test_type(self):
        instant = Review()
        self.assertTrue(dict, type(instant.to_dict))

    def test_keys(self):
        instant = Review()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_datetime_string(self):
        instant = Review()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = Review()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)
