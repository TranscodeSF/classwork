# Assignment 1 Part 2


## 0. Hello World!

In the lecture 2 slides we saw how to print "Hello World".  Now you are goiong to write your own hello world program.  Use an IDE or a text editor to create a new file to write your program in.  Write a program in a file that outputs "Hello World!" when run.  When saving your file, choose a name such as "hello.py".  Make sure to use the ".py" extension.

To run your file in the Python interpreter, open Terminal. In Terminal, type "python" followed by a space then the name of your Python program file.  For example:
`python hello.py`


## 1. Mad Lib

Write a program in a file (e.g. madlib.py) that prompts the user with at least three questions (at least one string and one integer).  Once the program has this information, it should then print a funny sentence using those inputs.

For example:


    Transcode Madlibstravaganza
    ---------------------------
    Input a name: Naomi
    Input a place: the grocery store
    Input a number: 42
    Input an adjective: violet
    Input a noun: hair

    Vacation tips, by Naomi.

    When travelling to the grocery store, don't forget to bring at least 42 pounds of violet hair.


## 2. FizzBuzz!

Write a program in a file (e.g. fizzbuzz.py) that prints the numbers from 1 to 100.  But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".  For numbers which are multiples of both three and five print "FizzBuzz".

For this assignment you will want to use the modulo operator `%`. The modulo operator yields the remainder from the division of the first argument by the second. For example:
```
a = 5
b = 3
r = a % b  # 2
```

You will also find the keywords `for`, `range`, and `if` helpful.
