#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import sys

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