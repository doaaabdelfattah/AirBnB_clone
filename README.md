Welcome to the AirBnB clone project!



drafting >>>>
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
