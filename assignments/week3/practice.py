def conjoin(first, second):
    """
    Return the two arguments conjoined with the word "and"

    Parameters:
    first - A string representing an English noun
    second - Another string representing an english noun

    Returns as a string an english phrase formed by putting the word "and"
    between its two arguments.  For example, if there was some other code
    that called conjoin("cat", "mouse"), then this function should return
    the string "cat and mouse".  See the bottom of this file for writing
    calling code.  It may help to think about writing the calling code
    first before writing each function implementation!
    """
    pass

def print_lots(phrase, times):
    """
    Print a phrase multiple times

    Parameters:
    phrase - a string to print
    times - the number of times to print the phrase

    At the end of execution, the phrase should be printed the
    specified number of times.

    Has no defined return value (i.e. you do not need a return statement).
    """
    pass

def joyful_phrase():
    """
    Randomly returns one of at least five different joyful phrases.

    The selection of joyful phrases is up to the implementor (the
    student, that is you). Remember the use of random from the
    guess my number exercise from pset2!

    Has no defined return value.
    """
    pass


def add_last_two(lst):
    """
    Computes the sum of the last two elements in the given list.

    Parameters:
    lst - the list to compute the last two elements of.  Must be a list of
    numbers, e.g. [1, 3, 4, -2, 5]

    For lists of two or more items, returns the sum of the last two elements.
    For lists of one item (e.g. [5]), returns that item.
    For empty lists (e.g. []), returns 0
    """
    pass

def extend_fibonacci(lst):
    """
    Append the sum of the last two elements

    Parameters:
    lst - A list of numbers with at least two elements in it, e.g. [4, 5]

    After this function executes, lst should have an additional
    element at the end.  This additional element should be the sum of
    the previous last two numbers.  For example:

         x = [1, 1, 2, 3]
         extend_fibonacci(x)
         print x

    ...after the function call, x should be [1, 1, 2, 3, 5] because 5 is the
    sum of the last two elements in the list.

    Remember that lists are a mutable type, so if they are modified (even when
    passed to a function as a parameter), then the list that x is pointing to
    in the example above is also modified!

    This function should not return anything, but should modify lst directly.
    """
    pass

#Read the code, try out the function in the interpreter, and write
#the specification for the following function:

def count_v(word):
    """ FILL IN THE SPECIFICATION HERE """
    result = 0
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            result += 1
    return result


# Finally, now that you have written all these functions above, write some code
# below this comment to call each of those functions with appropriate parameter
# values.
#
# This is also a good way to test out your functions.  If you run practice.py
# in idle, and you have put this code at the bottom, then you can make sure
# your functions work the way you expect them to!
#
# For each function above, write some code that calls that function at least
# twice.  It can be any code.  Be as straightforward or creative as you'd like.
# I'll do "conjoin" as the first example for you.  Please fill in the rest.

# call conjoin

print conjoin("foo", "bar")
print conjoin("french toast", "maple syrup")
print conjoin(raw_input("Pick word 1: "), raw_input("Pick word 2: "))
print conjoin(conjoin("a", "b"), "c")

# call print_lots

# call joyful_phrase

# call add_last_two

# call extend_fibonacci

# call count_v

