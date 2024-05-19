#!/usr/bin/python3
"""
This is the base model of my program
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = created_at.utcnow()
        self.updated_at = updated_at.utcnow()

    def save(self):
        """
        Updates the updated_at object with new time.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        First piece of serialization, turning our object to a dictionary

        Return: Dictionary of an object/instance
        """
        obj_dict = self.__dict__.copy()
        # each instance has an in built dictionary and you need to copy it
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return (obj_dict)

    def __str__(self):
        """
        Should print in the format [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My Base Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON for my_model:")
    for key in my_model_json.keys():
        print("\t[{}] ({}) - {}".format(key,
                                        type(my_model_json[key]),
                                        my_model_json[key]))
