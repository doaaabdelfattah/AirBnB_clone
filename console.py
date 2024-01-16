#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import re
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

    # def do_help(self, line):
    #     """overrides help method"""
    #     cmd.Cmd.do_help(self, line)

    # def help_quit(self):
    #     """ help guide for quit command """
    #     print('Quit command to exit the program')

    # def help_EOF(self):
    #     """ help guide for EOF command """
    #     print('EOF command to exit the program')

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    '''Aliasing (make exit the same as quit)'''
    do_exit = do_quit

    def emptyline(self):
        """ Eliminates empty lines
        """
        pass

    def do_count(self, arg):
        '''Usage: count <class name> or count'''
        args = arg.split()
        counts = 0
        for objcts in models.storage.all().values():
            if objcts.__class__.__name__ == args[0]:
                counts += 1
        print(counts)

    def do_create(self, arg):
        ''' Usage: create <class>
        Creates a class instance,saves it (to the JSON file)
        and prints its id '''
        '''Split the arguments to a list'''
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                '''create new object'''
                new_object = eval(args[0])()
                '''save new object to json file'''
                storage.save()
                '''print its id'''
                print(f"{new_object.id}")

    def do_show(self, arg):
        '''
        Prints the string representation of
    an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_names = args[0]
        if class_names not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id_isins = args[1]
        '''create the key for the dicti stored objects'''
        key = "{}.{}".format(class_names, id_isins)
        '''get the dictionary of stored objects'''
        objcts = storage.all()
        if key in objcts:
            print(objcts[key])
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        '''Usage: all <classname> or all '''
        args = arg.split()
        object_list = []
        if args:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                for value in storage.all().values():
                    if args[0] == value.__class__.__name__:
                        object_list.append(value.__str__())
        else:
            for value in storage.all().values():
                object_list.append(value.__str__())
        print(object_list)

    def do_destroy(self, arg):
        '''Usage: destroy <class name> <id>
            It Deletes an instance based on the class name and id
            and save the change into the JSON file'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return
            '''Iterate over objects dictionary(__obj)'''
        else:
            for key, value in storage.all().items():
                '''if found the id in class'''
                if args[0] == value.__class__.__name__ and args[1] == value.id:
                    '''delete object from obj dictionary'''
                    del storage.all()[key]
                    '''Save the result to json file'''
                    storage.save()
                    return
                '''if not found'''
            print("** no instance found **")

    def default(self, arg):
        '''Usage: <class name>.<command>(<parameters>)'''
        args = arg.split(".")
        if len(args) == 2:
            if args[0] in HBNBCommand.__classes:
                '''Use a dictionary to map commands to methods'''
                methods = {"all": self.do_all,
                           "count": self.do_count,
                           "show": self.do_show,
                           "destroy": self.do_destroy,
                           "update": self.do_update}
                '''Use a regular expression to match 
                    the command and the parameters'''
                matches = re.match(r'(\w+)\((.*)\)', args[1])
                if matches:
                    '''Get the command and 
                    the parameters from the match object'''
                    command, parameters = matches.groups()
                    ''' Use the dict.get() method
                    to get the method for the command, or None'''
                    method = methods.get(command)
                    if method:
                        ''' Use another regular expression to remove the
                         " charas from the parameters'''
                        parameters = re.sub(r'"', '', parameters)
                        '''Call the method with the class name
                        and the parameters as the argument'''
                        method(args[0] + " " + parameters)
                    elif args[1].startswith("update("):
                        args[1] = re.sub(r'update\(|\)|"', '', args[1])
                        if "," in args[1]:
                            args[1] = args[1].split(",")
                        if len(args[1]) == 4:
                            instance_id = args[1][0]
                            attribute_name = args[1][1]
                            attribute_value = args[1][2]
                            self.do_update(args[0], instance_id,
                                           attribute_name, attribute_value)
                        else:
                            '''The command is not valid'''
                            cmd.Cmd.default(self, arg)
                    else:
                        '''The command is not valid'''
                        cmd.Cmd.default(self, arg)
                else:
                    '''The command is not in the expected format'''
                    cmd.Cmd.default(self, arg)
            else:
                '''The class name is not valid'''
                cmd.Cmd.default(self, arg)
        else:
            '''The arg is not in the expected format'''
            cmd.Cmd.default(self, arg)

    def do_update(self, arg):
        '''Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")

            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) == 4:
            attribute_values = args[3]
        if attribute_values.startswith('"') and attribute_values.endswith('"'):
            attribute_values = attribute_values[1:-1]

        setattr(models.storage.all()[key], args[2], attribute_values)
        models.storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

    # if not sys.stdin.isatty():
    #     '''method is used to interpret the input as a comand'''
    #     for line in sys.stdin:
    #         '''Read command line by line'''

    #         HBNBCommand().onecmd(line.strip())
    #         '''method to remove whitespace from beg end'''
    # else:
    #     HBNBCommand().cmdloop()
