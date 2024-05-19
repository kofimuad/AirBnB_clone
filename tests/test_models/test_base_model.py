#!/usr/bin/python3
"""
To test the base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_base = BaseModel()

        self.assertIsNotNone(my_base.id)
        self.assertIsNotNone(my_base.created_at)
        self.assertIsNotNone(my_base.updated_at)

    def test_save(self):
        my_base = BaseModel()

        initial_update = my_base.updated_at
        current_update = my_base.save()
        self.assertNotEqual(initial_update, current_update)

    def test_to_dict(self):
        my_base = BaseModel()

        my_base_dict = my_base.to_dict()
        # check if my_base is indeed a dict
        self.assertIsInstance(my_base_dict, dict)

        # Check the key value pairing of the dict
        self.assertEqual(my_base_dict["__class__"], 'BaseModel')
        self.assertEqual(my_base_dict["id"], my_base.id)
        self.assertEqual(my_base_dict["created_at"],
                         my_base.created_at.isoformat())
        self.assertEqual(my_base_dict["updated_at"],
                         my_base.updated_at.isoformat())

    def test_str(self):
        my_base = BaseModel()
        # Check if it starts with BaseModel
        self.assertTrue(str(my_base).startswith('[BaseModel]'))
        # Check if id is present in string
        self.assertIn(my_base.id, str(my_model))
        # Check if there is dict rep. of model in string
        self.assertIn(str(my_base.__dict__), str(my_base))


if __name__ == "__main__":
    unittest.main()
