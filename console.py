#!/usr/bin/python3
"""
Cmd Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    CMD class
    """
    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
