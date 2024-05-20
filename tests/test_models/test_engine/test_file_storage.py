import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Testing the instantiation of file storage
    """
    def test_FileStorage_instantiation_no_args(self):
        # FileStorage instance with no arguments
        self.assertEqual(type(FileStorage), FileStorage)



