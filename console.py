#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {"BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"}
    '''The preloop method 
    is called once before the command loop starts.
    '''
        
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
        """Quits command interpreter with ctrl+d
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
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
                models.storage.save()
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
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
            # print the value of the key
        print(objects[key])


    def do_all(self, arg):
        '''Usage: all <classname> or all '''
        args = arg.split()
        obj_list = []
        if args:
            if args[0] not in HBNBCommand.__classes:
                    print("** class doesn't exist **")
            else:
                for value in models.storage.all().values():
                    if args[0] == value.__class__.__name__:
                        obj_list.append(value.__str__())
        else:
            for value in models.storage.all().values():
                obj_list.append(value.__str__())
        print(obj_list)

    def do_destroy(self, arg):
        '''Usage: destroy <class name> <id>
            It Deletes an instance based on the class name and id 
            and save the change into the JSON file'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            if len(args) == 2:
                # Iterate over objects dictionary(__obj)
                for key, value in models.storage.all().items():
                    # if found the id in class
                    if class_name == value.__class__.__name__ and args[1] == value.id :
                        # delete object from obj dictionary
                        del models.storage.all()[key]
                        # Save the result to json file
                        models.storage.save()
                        return
                # if not found
                print("** no instance found **")
            else:
                print("** instance id missing **")
                
    def do_update(self, arg):
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
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        types_valid = type(getattr(all_objects[key], attribute_name))
        if hasattr(all_objects[key], attribute_name):
            try:
                attribute_value = types_valid(attribute_value)
                setattr(all_objects[key], attribute_name, attribute_value)
                all_objects[key].save()
            except ValueError:
                return
        else:
            print("** attribute doesn't exist **")
            return

                
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

    if not sys.stdin.isatty():
        # (onecmd) method is used to interpret a single line of input as a command.
        for line in sys.stdin:
            # Read command line by line
            # Stripe method to remove whitespace from beginning and the end
            HBNBCommand().onecmd(line.strip())
        else:
            HBNBCommand().cmdloop()