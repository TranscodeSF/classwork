import sys, os
from random import *


def is_word(text):
    """ REPLACE THIS TEXT WITH YOUR ANSWER """
    if text == "'":
        return False
    #for contractions
    elif text.replace("'", "").isalnum():
        return True
    return False

def split_words_and_punctuation(text):
    """ REPLACE THIS TEXT WITH YOUR ANSWER """
    words = []
    currentword = ""
    for i in range(len(text)):
        c = text[i]
        if i+1 < len(text):
            next = text[i+1]
        else:
            next = None
        if c.isalnum() or (c == "'" and next != None and next.isalnum()):
            #The second part of the or is for contractions, which should
            #appear as a single word
            currentword += c
        elif c.isspace():
            if currentword != "":
                words.append(currentword)
            currentword = ""
        else:
            if currentword != "":
                words.append(currentword)
            words.append(c)
            currentword = ""
    if currentword != "":
        words.append(currentword)
    return words

def add_word(d, word, next_word):
    """ REPLACE_THIS_TEXT_WITH_YOUR_ANSWER"""
    if word in d:
        d[word].append(next_word)
    else:
        d[word] = [next_word]

def table_of_next_words(text):
    """
    Creates a table of what words we have seen after other words.

    Parameters:

    text - an English string with which we will create our table.
    
    Returns a dictionary where:
    
    * Every word or punctuation in the given text is a key, and the
      associated value is a list of every word that follows the key in
      the given text.

    * If one word follows another more than once, it appears in the
      list more than once.

    * The beginning of the text is marked by a special "word" denoted by
      the python value None, as is the end of the text.

    For example, the output for the text "a a b c a b" is:
    { None: ['a'],
      'a': ['a', 'b', 'b'],
      'b': ['c', None],
      'c': ['a']
    }
    """
    pass

def pick_random_element(lst):
    """ Return a random element in the given list lst."""
    pass


def make_text(table):
    """
    Given a table of next words, construct a random text with similar
    word frequencies.

    Parameters:

    table - a dictionary of the form word->list of next words seen --
    the same form that comes out of the function table_of_next_words

    Returns a string where:

    * The first word is randomly chosen from the list table[None]

    * Every further word is randomly chosen from the list gotten by
      looking up the previous word

    * When the next word is chosen to be None, there is no next word
      and the words chosen so far are returned as a string.

    * Every word is preceded by a space.

    * No punctuation is preceded by a space.
    
    """
    pass

def main(argv):
    if len(argv) == 0:
        filename = "alice.txt"
    else:
        filename = argv[0]
    with open(filename) as f:
        text = f.read()
        table = table_of_next_words(text)
        print make_text(table)

if __name__ == '__main__':
    main(sys.argv[1:])
