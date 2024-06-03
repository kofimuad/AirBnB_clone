#!/usr/bin/python3
"""
Cmd Module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    CMD class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User"]

    def empty_line(self):
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
