## Reading:

* [Chapter 6: Fruitful Functions](http://www.greenteapress.com/thinkpython/html/thinkpython007.html):

* [Exceptions Tutorial](http://docs.python.org/tutorial/errors.html)

* [Reading and Writing files](http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files)

* [Methods on file objects](http://docs.python.org/tutorial/inputoutput.html#methods-of-file-objects)


## Anagrams:

Last week we talked about testing and recursion.  For this question,
you'll be looking at a recursive function, and testing it.

Our recursive function lives in anagram.py.  Take a good look at that
whole file, both the code and the spec.

Your task: write unit tests for the following functions:

 - `normalize`
 - `remove_letters`
 - `anagrams`

Put your tests in `anagram_test.py`

Some of the functions have bugs.  Describe the bugs you find:

Answer here...


Optional: See if you can fix the bugs you found.  Use the `anagrams()` function in
the python interpereter to find anagrams of your name.  What's your
favorite anagram of your name:

Answer here...


## Exception warmup:

In the file `classifier.py`, write a program that prompts a user for input.
Then, print out whether that number is an int, a float, or neither.

Fill in the two helper functions `call is_string_int(s)` and `is_string_float(s)`
and use those helper functions.  In those helper functions, use a try/except
block to try converting user input to the given type.  Then, call those helper
functions in the main program.

The program's output should look something like this:

    What string do you want to know about? 5
    5 is an int.

    What string do you want to know about? 3.2
    3.2 is a float.

    What string do you want to know about? 5x
    5x doesn't look like an int or a float.


## Catching exceptions:

This exercise is to give you practice about reading code that you haven't
written and then improving it by adding exception handling.  This will also
hone your ability to think of good test cases.

First, try running `catch.py` and using the default `catch.txt` file.  This program
loads a file consisting of a series of integers, then lets you average or print
them.  Try to think of several different ways this program could break and
throw an exception.

Your job is to add exception handling to this file.  Make the exceptions as
specific as possible.  For instance, don't `catch Exception`, you should `catch
ValueError` instead.  In the catch block, print out an error message.  If you
also feel like the program can't continue at that point (maybe it had trouble
loading a file), then use `sys.exit()` to quit the program entirely.

There are at least four different lines of code that can throw different kinds
of exceptions.  If you are having trouble coming up with all four, try thinking
about different file contents that you could load that might cause problems.


## Score keeping:

Sometimes when playing games with friends, it's really tedious to have to keep
track of scores round after round.  Your job is to write a program that will
keep track of scores and store them in a file.  The idea is that after each
round, you would run this program and enter everybody's scores for the round
in, and then it would give you current score totals.

First, take a look at `scores.txt`.  It's a pretty simple format.  There's one
line with a person's name, and then multiple lines with integer scores for each
round.  Assume each person has the same amount of rounds.  In this case, every
player has played three rounds.

Your job is to write a program in `scorekeeper.py` that does this score tracking.
This program should do the following things:

First, the program should open the `scores.txt` file and read in the data.  You
can't assume anything about the player's names, the number of players, or the
number or rounds that have been played.  You should figure out what those are
from the file itself!  Read the file line by line and either add a new player
or add a score to an existing player's list of scores.

Remember to use a try/except block around the file IO.  If opening or reading
the file fails, then print out an error message and quit the program.

Second, the program should print out the current totals.  For the given
scores.txt file, it should look like this:

    Total points per player:
        amber: 4
        naomi: 17
        aiiaiea: 10

Third, the program should prompt for scores for the current round.  The user
should be able to enter a single score per player.  For example:

    How many points did enne score? 5
    How many points did naomi score? -3
    How many points did aiiaiea score 20

If a user enters in a non-integer, the program should print out an error
message and ask for the score again.  You should use a try/except block for
this.

Fourth, the program should print out the new score totals again.  Remember to
not repeat yourself!  Try to reuse the print function from above.

    Total points per player:
        enne: 9
        naomi: 14
        aiiaiea: 30

Finally, the program should open up scores.txt and write out all of the player
names and all the new round scores.

You should be able to run this program again and have it read in the new scores
correctly.

### Helpful Hints:

* When reading the score file, I would suggest using a dictionary to store
this information, with the key of the dictionary being the player's name and
the value of the dictionary being a list of integers.  Remember that you can do
a "for key in dict:" to loop over all the keys in the dictionary.

* Remember the classifier exercise above if you want to figure out if a line
in a file is an integer or a string.  You could reuse that is_string_int
function.

* The rstrip function (look at catch.py for an example) will remove '\n' from
the end of a line after reading it from a file.

* Once you think your program is working, add a fourth and a fifth player to
scores.txt and verify that your program behaves correctly.

* As you are working on your program, you may write something incorrect to
scores.txt, which would cause the program to not be able to read anything else
in.  A copy of the original version of scores.txt is in scores_original.txt if
you need it!

* Remember when writing things to a file that you need to write the special
character '\n' to write a new line.

### Bonus Questions:

If you get this done and want to show off your expert Python knowledge, here
are some creative ways you could make this program better:

* Print an error if not every person has the same number of rounds (easy).
* Print out every player's average score as a float (a little tricky).
* Print out the name of the currently winning player (somewhat tricky).
* Print out all players and scores in sorted order of score (super tricky).


## Survey

How long did this assignment take you?

What did you enjoy about it?

What did you have a hard time with?

What should we go over more in class?

