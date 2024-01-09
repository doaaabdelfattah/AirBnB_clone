#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    '''Define the quit command'''
def do_quit(self):
    """Quits the program."""
    print("quitting")
    return True

    '''Define the EOF command'''
def do_EOF(self, line):
    """Exits the program when EOF is received."""
    print()
    return self.do_quit()
def emptyline(self):
    """Do nothing when an empty line is entered."""
    pass
if __name__ == '__main__':
    my_cli = HBNBCommand()
    my_cli.cmdloop()