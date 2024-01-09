#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
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
    def do_empty_line(self, line):
        """
        Eliminates empty lines
        """
        pass




if __name__ == '__main__':
    my_cli = HBNBCommand()
    my_cli.cmdloop()