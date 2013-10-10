#Functions

Week 3-4's homework is all about learning to do functions.  You have two weeks to
finish the assignment. For the first week, finish the reading, Rock Paper
Scissors, and Function Practice.  For the second week, finish the Markov Chain
problem.  Please do not wait until the last day to do either of these.  If you
have questions about how functions or Python or anything works, please feel free
to email the discuss list!

## Reading

Read [chapter 3](http://www.greenteapress.com/thinkpython/html/thinkpython004.html) from the
Think Python book

## Rock Paper Scissors

In the file rockpaperscissors.py, fill in the function is_better_than based on
the specification given in that file. If you remember how we did the
rock-paper-scissors game in the class, this would be turning the heart of that
game into a function in the file, that you can then test separately.

Already provided is a rockpaperscissors_test.py file. This Python code will
test the function you have written to make sure that it returns the right
values. You don't need to worry about the details of this class. You're welcome
to look inside this class to see how testing works (there's lots of things we
haven't explained yet), but don't edit the file.

To run the tests, navigate to the week3 directory and run:

    python rockpaperscissors_test.py

Before you write any code in rockpaperscissors.py, you should see something like this:


    .FF.
    ======================================================================
    FAIL: test_player0_win (__main__.TestRPS)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "rockpaperscissors_test.py", line 14, in test_player0_win
        self.assertEqual(rps.is_better_than("paper", "rock"), 0)
    AssertionError: None != 0

    ======================================================================
    FAIL: test_player1_win (__main__.TestRPS)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "rockpaperscissors_test.py", line 19, in test_player1_win
        self.assertEqual(rps.is_better_than("rock", "paper"), 1)
    AssertionError: None != 1

    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    FAILED (failures=2)

It's your job to finish the function and get these tests passing!  If you fill
out the function successfully, then running the test file should give you this
output:

    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    OK

## Function practice

Open up practice.py in your text editor.  It has further instructions in the
file itself.  There are 5 function bodies to fill out, 1 function specification
to write, and then at the bottom some code to write to call all of the functions
that you just wrote.

## Markov Chains

The next part of this assignment is the largest body of code we've
worked with in this course all at once.  What it will eventually do is
take in some body of text (we've provided a small sample bit from
Alice in Wonderland to get you started), and create some more text
that is "similar" to the source text, in the distribution of which
words come after which other words.  The resulting text is frequently
silly.  This process for generating text is called a "Markov chain".

Open up markov.py, and note that for the first few functions, all the
code is provided.  However, the specifications are all listed as
`""" REPLACE THIS TEXT WITH YOUR ANSWER """`.

For each function without a specification, look at the code to try to figure out
what it does, and play with it in the interactive python interpreter to help
you. In the python interactive mode (when it's started from this directory), you
can type

    >>> import markov

To import the markov module for the first time, and allow you to call
the functions as follows:

    >>> markov.is_word("foo")
    True
    >>> markov.is_word("ain't")
    True
    >>> markov.is_word("'")
    False
    >>> markov.is_word("...")
    False

If you've changed markov.py and want the interactive window to reflect
your changes for future lines you type, you can type:

    >>> markov = reload(markov)

Once you have a decent idea of what the function does, write down an
English description of the specification in the docstring where it
says `""" REPLACE THIS TEXT WITH YOUR ANSWER """`.

Remember that a specification should describe what the point of a function is,
and *not* what exactly all the steps in it do, or how it accomplishes its goal.

The next few functions have a specification, but do not have a
function body.  (pass is a python keyword that just plain does
nothing.  We use it to stand in for function bodies we have not filled
in yet.)  Fill in all the function bodies, based on the specifications
we've given you.

To test that you're on the right track, we've provided some tests for
you.  You can run tests.py the same way you ran
rockpaperscissors_test.py above, to see how you're doing.

The real test of your program, however, is running it.  You can run the module
in the Python interactive mode to generate some text based on our Alice excerpt,
or you can do at the command line:

    python markov.py anotherfile.txt

to generate some text based on another file.

## Modifying Markov

In this exercise, you're going to modify your markov chain program to
allow you to chat with it.  The word frequency table will learn from
things you say.

Start by going back to markov.py.  `table_of_next_words(text)` in that
file is *almost* useful for building up a table over time, but not
quite.  Create a new function `update_table(table, text)` in markov.py.
This new function updates the table its given, rather than creating a
new one.  You should be able to move most of your code from
`table_of_next_words` over to this new function, and replace most of the
body of `table_of_next_words` with a call to `update_table`.

Run the tests again to make sure that `table_of_next_words` still works.

This process is called "refactoring"

Next, use your new update_table function in conversation.py to build a
program that repeatedly:

- Asks the user for input
- Updates the table with the user's input
- Says something based on the table
- If the user ever types "bye", the program exits.

Note that if you do this correctly, the program will still generally
take a bit of time to warm up to being able to say different things.
For an example of how a conversation with a correctly-functioning
program can go, see example.txt

## Survey

How long did this assignment take you?

What did you enjoy about it?

What did you have a hard time with?

What should we go over more in class?
