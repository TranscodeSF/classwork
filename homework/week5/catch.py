import sys # for sys.exit()

filename = raw_input("What file to open (hit enter for catch.txt)? ")
if not filename:
    filename = "catch.txt"

# Read a list of integers from a file
with open(filename, 'r') as f:
    text = f.read()
    # remove trailing whitespace
    # See: http://docs.python.org/library/stdtypes.html#str.rstrip
    text = text.rstrip()
    # split up string into an array, splitting on whitespace
    # See: http://docs.python.org/library/stdtypes.html#str.split
    stringvalues = text.split()

# Convert those strings from the file to integers
intvalues = []
for x in stringvalues:
    intvalues.append(int(x))

while True:
    command = raw_input("Input one letter: h(elp), a(verage), p(rint), e(x)it")
    if command == 'h':
        what_help = raw_input("Help on which command letter? ")
        # a dictionary of help text
        help_text = {
            'a': 'print the average of all values',
            'p': 'print all the values',
            'h': 'print help text',
            'x': 'quit',
        }
        print help_text[what_help]
    elif command == 'a':
        the_sum = 0
        for x in intvalues:
            the_sum += x
        average = the_sum / float(len(intvalues))
        print "The average is: %f" % average
    elif command == 'p':
        print intvalues
    elif command == 'x':
        # Forcibly exit.  We could also just use 'break' here.
        sys.exit()
    else:
        print "Invalid command: %s" % command
