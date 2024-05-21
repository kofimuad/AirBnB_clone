import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    File Storage Class
    """
    __file_path = "file.json"
    __objects = {}  # empty dict

    def new(self, obj):
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns all data in __objects dict
        """
        return (FileStorage.__objects)

    def save(self):
        """
        This does the serialization
        Saves the obj dict to JSON format
        """
        all_objs = FileStorage.__objects
        obj_dict = {} #  An empty dict to store objects

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialization
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        # use eval() to transform it ito a class
                        cls = eval(class_name)
                        instance = cls(**values)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
