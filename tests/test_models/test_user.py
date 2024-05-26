import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        # Create temp test file
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        # Remove temp test file after test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        # Create a new user instance
        test_user = User()
        # check if default email is empty
        self.assertEqual(test_user.email, "")
        # check if default password is empty
        self.assertEqual(test_user.password, "")
        # check if default first name is empty
        self.assertEqual(test_user.first_name, "")
        # check if default last name is empty
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_base_model(self):
        # create a User instance
        test_user = User()
        # check if User is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        # create new user
        test_user = User()
        # Set attributes of the user instance
        test_user.email = "iamkofiantwi@outlook.com"
        test_user.password = "hydra@thepantheon"
        test_user.first_name = "Bismark"
        test_user.last_name = "Agyei"
        # get str rep. of user instance
        usr_str = str(test_user)
        # check if user is present in str rep.
        self.assertIn("User", usr_str)
        # check if email is present in str rep.
        self.assertIn("iamkofiantwi@outlook.com", usr_str)
        # check if first name is present in str rep.
        self.assertIn("Bismark", usr_str)
        # check if last name is present in str rep.
        self.assertIn("Agyei", usr_str)

    def test_user_to_dict(self):
        # create User instance
        test_user = User()
        # Set attributes for user instance
        test_user.email = "iamkofiantwi@outlook.com"
        test_user.first_name = "Bismark"
        test_user.last_name = "Agyei"
        test_user.save()
        # Get dict rep. of user instance
        user_dict = test_user.to_dict()
        # Check if 'email' key in dict matches set value
        self.assertEqual(user_dict['email'], "iamkofiantwi@outlook.com")
        # Check if 'first_name' key in dict matches set value
        self.assertEqual(user_dict['first_name'], "Bismark")
        # Check if 'last_name' key in dict matches set value
        self.assertEqual(user_dict['last_name'], "Agyei")

    def test_user_instance_creation(self):
        # create new instance with arguments
        test_user = User(email="iamkofiantwi@outlook.com",
                         password="hydra@pantheon",
                         first_name="Bismark", last_name="Agyei")
        # check if email attribute is set correctly
        self.assertEqual(test_user.email, "iamkofiantwi@outlook.com")
        # check if password attribute is set correctly
        self.assertEqual(test_user.password, "hydra@pantheon")
        # check if first_name attribute is set correctly
        self.assertEqual(test_user.first_name, "Bismark")
        # check if last_name attribute is set correctly
        self.assertEqual(test_user.last_name, "Agyei")

    def test_user_instance_to_dict(self):
        # create user instance with attributes
        test_user = User(email="iamkofiantwi@outlook.com",
                         password="hydra@pantheon",
                         first_name="Bismark", last_name="Agyei")
        # Get dict rep. of user instance
        user_dict = test_user.to_dict()
        # Check if 'email' key in dict matches set value
        self.assertEqual(user_dict['email'], "iamkofiantwi@outlook.com")
        # Check if 'password' key in dict matches set value
        self.assertEqual(user_dict['password'], "hydra@pantheon")
        # Check if 'first_name' key in dict matches set value
        self.assertEqual(user_dict['first_name'], "Bismark")
        # Check if 'last_name' key in dict matches set value
        self.assertEqual(user_dict['last_name'], "Agyei")

    def test_user_id_generation(self):
        # create two user instances
        test_user = User()
        user2 = User()
        # See if id of each user is unique
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == "__main__":
    unittest.main()
