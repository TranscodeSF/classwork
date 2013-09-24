#Welcome to Transcode!

It's time for your first homework assignment.  For things that expect
an answer in written english, just type the answers into this file on
their own line, and push it to your remote git repository with the rest
of your homework.

If you have not completed the Transcode pre-class setup, please be sure to
follow this link and install all the required software:
https://docs.google.com/document/d/15W7T-qfVfm07V0vsRKrWGK_Y-PRPXF_KQzxwwTn15Gs/

For more information about git, please see the Transcode git survival guide:
https://docs.google.com/document/d/1T4NT8W-1eqEHqnZkIAmsJVvu1Ed9u52bGB3u2u4F0k0/

If you are new to Linux, you may also want to see this Linux guide:
https://docs.google.com/document/d/1yqysf74rdhGpO59Wh0DgMsYaSHYSfmL7FdXMmxPOL58/


0. We'll be doing this problem in class.  Right below this prompt,
write a sentence of your choice, and then check that in to your local
git repository:

git commit -a -m 'Answering question 0'

Proceed to push that to your remote git repository on students.transcodesf.org

git push

Write your sentence here:


1. Play through the first three levels of http://pleasingfungus.com/Manufactoria/

You may wonder why we're assigning you to play a game.  This game in
particular helps you think like a programmer and to visually design
algorithms.  I also think it's fun.

You may be able to pick up exactly what you need to do from playing
the game.  If you need a better explanation of the concepts or the
basic controls, look at the manufactoria-faq.txt file in the
classresources directory.  Even when you know what they are, the
controls are a little cumbersome and may take some getting used to.

And yes, as you might be wondering, hints and answers to this entire
game are available online, but struggling and finding the answers
yourself is the only way to learn.  Please resist the temptation to
cheat yourself.

Put a screenshot of your solution to the third level in this directory
under the name 'manufactoria.png' (or whatever image format you
prefer).  The third level in particular is a LOT trickier than the
first two, so don't be surprised if it takes longer.


2. In lecture, we put up the memory layout of a computer program to do
exponentiation.  Let's do another problem like that, but with a
different program.  Remember, square brackets like [this] mean "the
number stored in this slot":

00: Store the remainder of [10]/[11] in slot 12
01: if [12] is 0 go to step 05
02: copy [11] to slot 10
03: copy [12] to slot 11
04: go to step 00
05: output [11]
06:
07:
10: 12
11: 15
12:
13:
14:
15:
16:
17:

Feel free to use the above as space to actually work out the
answer. What does this output?

Try the same program with some other inputs in slots 10 and 11.  What
does this program compute?

3. Another one of the same, but instead of writing out exactly what
every instruction does, we'll use some abbreviations for our instructions:

Math:
ADD A B C     ADD the value at A to the value at B and store the result in C
SUB A B C     SUBtract the value at A and the value at B and store the result in C
DIV A B C     DIVide the value at A by the value at B and store the result in C
MOD A B C     Divide the value at A by the value at B and store the remainder in C (MODulo)
MUL A B C     MULtiply the value at A by the value at B and store the remainder in C
INC A         (INCrement) Add 1 to the value in A, and store that back in A
DEC A         (DECrement) Subtract 1 from the value in A, and store that back in A

Memory:
STO a B       STOre value a in slot B.
MOV A B       MOVe (copy) the value at A to also be stored in B

Program control:
JMP X         JuMP to step X
JNZ A X       Jump to step X if the value in A is Not Zero
OUT A         Output the value in A

Here's the program:

00: STO 0  11
01: STO 1  12
02: ADD 11 12 13
03: DEC 10
04: MOV 12 11
05: MOV 13 12
06: JNZ 10 02
07: OUT 11
10: 6
11:
12:
13:
14:
15:
16:
17:

What does this output?

In general, what will this program output, given any input in slot 10?


4. Read chapter 1 of How to Think Like a Computer Scientist

Most readings for the beginning of the class will come from this textbook.  You can find this in the class resources directory as a pdf, but you can also access it online here: http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap01.html


5. Finally:

How much time did this problem set take you?

What, if anything, did you have trouble with?

What, from lecture, would you like us to cover more clearly?
