#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}
    '''The preloop method 
    is called once before the command loop starts.
    '''
    def preloop(self) -> None:
        print("Documented commands (type help <topic>):")
        print("========================================")
    
    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d
         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True
    def do_quit(self, line):
        """Quit command to exit the program
         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True
    
    # Aliasing (make exit the same as quit)
    do_exit = do_quit
    
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
            print(" class name missing ")
        else:
            if args[0] not in HBNBCommand.__classes:
                print(" class doesn't exist ")
            else:
                # create new object
                new_obj = eval(args[0])()
                # save new object to json file
                new_obj.save()
                # print its id
                print(f"{new_obj.id}")
                
    def do_show(self, arg):
        '''
        Prints the string representation of
    an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id_isinstance = args[1]
        # create the key for the dictionary of stored objects
        key = "{}.{}".format(class_name, id_isinstance)
        # get the dictionary of stored objects
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
            # print the value of the key
        print(objects[key])
                
    
        
        
        
        

        

''' to handel multiable command
sys.argv list, which contains 
all the command-line arguments.
You can loop through sys.argv[1:] 
(excluding the first element, which is the script's name)
and execute the commands
if name == 'main':
     my_cmd = HBNBCommand().cmdloop()
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        my_cmd.onecmd(arg)
        --------------------- OR----------------
        if name == "main":
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
