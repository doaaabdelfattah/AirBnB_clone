#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import shlex
import sys
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }
    '''The preloop method 
    is called once before the command loop starts.
    '''
    def preloop(self) -> None:
        print("Documented commands (type help <topic>):")
        print("========================================")
        
        def do_help(self, line):
            """overrides help method"""
        cmd.Cmd.do_help(self, line)
        
    def help_quit(self):
        """ help guide for quit command """
        print('Quit command to exit the program')

    def help_EOF(self):
        """ help guide for EOF command """
        print('EOF command to exit the program')

    
    def do_EOF(self, line):
        """ function to exit the cmd """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True
    
    # Aliasing (make exit the same as quit)
    #do_exit = do_quit
    
    def do_empty_line(self, line):
        """ Eliminates empty lines
        """
        pass
    
    def do_create(self, arg):
        ''' Usage: create <class>
        Creates a class instance,saves it (to the JSON file) 
        and prints its id '''
        # Split the arguments to a list
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                # create new object
                new_obj = eval(args[0])()
                # save new object to json file
                models.storage.save()
                # print its id
                print(f"{new_obj.id}")
                

''' to handel multiable command
sys.argv list, which contains 
all the command-line arguments.
You can loop through sys.argv[1:] 
(excluding the first element, which is the script's name)
and execute the commands
if __name__ == '__main__':
     my_cmd = HBNBCommand().cmdloop()
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        my_cmd.onecmd(arg)
        --------------------- OR----------------
        if __name__ == "__main__":
    # not Running in Terminal (non-interactive)
    if not sys.stdin.isatty():
        # (onecmd) method is used to interpret a single line of input as a command.
        for line in sys.stdin:
            # Read command line by line
            # Stripe method to remove whitespace from beginning and the end
            line = line.strip()
            # Check if the line contains semicolons
            if ";" in line:
                # Call the default method
                HBNBCommand().default(line)
            else:
                # Call the onecmd method
                HBNBCommand().onecmd(line)
    else:
        HBNBCommand().cmdloop()

'''
    
# Make the interpreter works in a loop
if __name__ == "__main__":
    # not Running in Terminal (non-interactive)
    if not sys.stdin.isatty():
        # (onecmd) method is used to interpret a single line of input as a command.
        for line in sys.stdin:
            # Read command line by line
            # Stripe method to remove whitespace from beginning and the end
            HBNBCommand().onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()
