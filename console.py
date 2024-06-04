#!/usr/bin/python3
"""
Cmd Module
"""
import cmd
import re
import ast
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


def split_curly_braces(incoming_extra_arg):
    """
    splits curly braces for update method
    """
    curly_braces = re.search(r"\{(.*?)\}",
                             incoming_extra_arg)

    if curly_braces:
        id_with_comma = shlex.split(
            incoming_extra_arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dict format **")
            return
        return (id, arg_dict)
    else:
        commands = incoming_extra_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return ("", "")
            try:
                attr_name = commands[1]
            except Exception:
                return (id, "")
            try:
                attr_value = commands[2]
            except Exception:
                return (id, attr_name)
            return (f"{id}", f"{attr_name} {attr_value}")


class HBNBCommand(cmd.Cmd):
    """
    CMD class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Does nothing when an empty line is entered
        """
        pass

    def do_quit(self, arg):
        """
        Quit program
        """
        return (True)

    def help_quit(self):
        """

        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Quits with Ctrl-D
        """
        print()
        return (True)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        Ex: create <class name>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            #  eval() changes the string into an py obj
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print string representation of an instance
        Ex: show <class name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()  # Fetch objs from storage

            key = "{}.{}".format(commands[0], commands[1])

            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()  # Save changes after del
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances.
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def default(self, arg):
        """
        Default behaviour for invalid syntax
        """
        arg_list = arg.split('.')
        #  eg: for Amenity.all(), output: ['Amenity', 'all()']
        #  arg_list[0] = 'Amenity'
        #  arg_list[1] = 'all()'
        incoming_class_name = arg_list[0]
        command = arg_list[1].split('(')
        incoming_method = command[0]

        incoming_extra_arg = command[1].split(')')[0]

        # all_args = incoming_extra_arg.split(',')

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }  # holds all methods we have

        if incoming_method in method_dict.keys():
            if incoming_method != "update":
                return (method_dict[incoming_method]
                        ("{} {}".format(incoming_class_name,
                                        incoming_extra_arg)))
            else:
                if not incoming_class_name:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_curly_braces(incoming_extra_arg)
                except Exception:
                    pass
                try:
                    return (method_dict[incoming_method]
                            ("{} {} {}".format(incoming_class_name,
                                               obj_id,
                                               arg_dict)))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False

    def do_count(self, arg):
        """
        Gets the number of times a class is used
        """
        objects = storage.all()
        commands = shlex.split(arg)

        incoming_class_name = commands[0]

        count = 0

        if commands:
            if incoming_class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Update an instance by adding an attribute
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{(.*?)\}", arg)

                if curly_braces:
                    str_data = curly_braces.group(1)

                    arg_dict = ast.literal_eval("{" + str_data + "}")

                    attribute_names = list(arg_dict.keys())
                    attribute_values = list(arg_dict.values())

                    attr_name1 = attribute_names[0]
                    attr_value1 = attribute_values[0]

                    attr_name2 = attribute_names[1]
                    attr_value2 = attribute_values[1]

                    setattr(obj, attr_name1, attr_value1)
                    setattr(obj, attr_name2, attr_value2)
                else:
                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(attr_value)
                        # convert values to their appropriate data types
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
