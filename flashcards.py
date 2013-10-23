import random
import textwrap
import copy

class Card(object):

    def reset(self):
        pass

    def question(self):
        pass

    def check_answer(self, answer):
        pass

    wrapper = textwrap.TextWrapper(initial_indent="  | ", subsequent_indent="  | ", width=45)

    def play(self):
        self.reset()
        lines = []
        for paragraph in self.question():
            lines.extend(Card.wrapper.wrap(paragraph))
        print "  *%s*" % ("_"*42)
        for line in lines:
            print "%s%s|" % (line, ' '*(45 - len(line)))
        print "  *%s*" % ("-"*42)            
        answer = raw_input(">>> ")
        if self.check_answer(answer):
            print random.choice(["Correct!", "Good job!", "Five points to Griffindor",
                                 "Excellent.", "Well done.", "Capital.", "Indeed."]), '\n'
            return True
        else:
            print "Not quite.  A valid answer was:\n"
            print self.answer(), '\n'
            return False

    def answer(self):
        pass

    def varname(self):
        return random.choice(['a', 'b', 'c', 'foo', 'bar', 'baz'])

class ExpectString(Card):

    def __init__(self, question, answer):
        Card.__init__(self)
        self._question = question
        self._answer = answer

    def question(self):
        return [textwrap.dedent(self._question)]

    def answer(self):
        return self._answer

    def check_answer(self, answer):
        return answer.strip() == self._answer.strip()

class MultipleChoice(Card):

    wrapper = textwrap.TextWrapper(initial_indent="", subsequent_indent="   ", width=40)
    
    def __init__(self, question, correct, incorrect):
        self._question = question
        self._correct = correct
        self._incorrect = incorrect
        
    def reset(self):
        start = ord('a')
        l = len(self._incorrect) + 1
        chars = [chr(c) for c in range(start, start+l)]
        random.shuffle(chars)
        self._answer = chars[0]
        self._distractors = chars[1:]

    def question(self):
        answers = ['%s. %s' % (self._answer, self._correct)]
        for d, i in zip(self._distractors, self._incorrect):
            answers.append('%s. %s' % (d, i))
        answers.sort()
        wrapped_answers = []
        for ans in answers:
            wrapped_answers.extend(MultipleChoice.wrapper.wrap(ans))
        return self._question + wrapped_answers

    def answer(self):
        return self._answer

    def check_answer(self, answer):
        return answer == self._answer
        

class AssignEmptyList(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["Write a line of code to store an empty list in a variable named %s" % self._var]

    def answer(self):
        return "%s = []" % self._var

    def check_answer(self, answer):
        env = {}
        try: 
            exec(answer, env)
            return env[self._var] == []
        except:
            return False

assignemptylist = AssignEmptyList()

class AssignEmptyDict(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["Write a line of code to store an empty dictionary in a variable named %s" % self._var]

    def answer(self):
        return "%s = {}" % self._var

    def check_answer(self, answer):
        env = {}
        try: 
            exec(answer, env)
            return env[self._var] == {}
        except:
            return False
        
assignemptydict = AssignEmptyDict()

class Range(Card):

    def reset(self):
        self._end = random.randrange(10, 50)

    def question(self):
        return ["Write an expression that produces a list of integers in order " + 
                "from 0 up to but not including %i" % self._end]

    def answer(self):
        return "range(%i)" % self._end

    def check_answer(self, answer):
        try:
            return eval(answer, {}) == range(self._end)
        except:
            return False

rangecard = Range()

class IntCast(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a string, write an expression that produces the equivalent integer value" % self._var]            
    
    def answer(self):
        return "int(%s)" % self._var

    def check_answer(self, answer):
        try:
            return eval(answer, {self._var : "37"}) == 37
        except:
            return False

intcast = IntCast()

class ListLen(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a list, write an expression that produces the length of the list" % self._var]
    
    def answer(self):
        return "len(%s)" % self._var

    def check_answer(self, answer):
        try:
            return eval(answer, {self._var : [1, 2, 3, "four"]}) == 4
        except:
            return False

listlen = ListLen()

class LastElt(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a list, write an expression that produces the last element of the list" % self._var]
    
    def answer(self):
        return "%s[-1]" % self._var

    def check_answer(self, answer):
        try:
            return eval(answer, {self._var : [1, 2, 3, "four"]}) == "four"
        except:
            return False        

lastelt = LastElt()

class FirstElt(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a list, write an expression that produces the first element of the list" % self._var]
    
    def answer(self):
        return "%s[0]" % self._var

    def check_answer(self, answer):
        try:
            return eval(answer, {self._var : ["argyle", 2, 3, "four"]}) == "argyle"
        except:
            return False        

firstelt = FirstElt()

class DictLookup(Card):

    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a dictionary, write an expression that produces the value in %s assocated with the key 'k'" % (self._var, self._var)]

    def answer(self):
        return "%s['k']" % self._var

    def check_answer(self, answer):
        try:
            return eval(answer, {self._var : {'k': 'xyzzy'}}) == 'xyzzy'
        except:
            return False

dictlookup = DictLookup()

class DictIndirectLookup(Card):

    def reset(self):
        self._d = self.varname()
        self._k = self.varname()
        while self._k == self._d:
            self._k = self.varname()

    def question(self):
        return [("If %s is a dictionary, write an expression that produces the " + 
                 "value in %s associated with the contents of the variable %s as the key")
                % (self._d, self._d, self._k)]

    def answer(self):
        return "%s[%s]" % (self._d, self._k)

    def check_answer(self, answer):
        try:
            return eval(answer, {self._d : { "noodle" : 321 }, self._k : "noodle" }) == 321
        except:
            return False

dictindirect = DictIndirectLookup()

class DictStore(Card):

    def reset(self):
        self._i = random.randrange(10)
        self._d = self.varname()
        self._k = self.varname()
        while self._k == self._d:
            self._k = self.varname()

    def question(self):
        return ["Write a line of code to put the value %i in the dictionary %s associated with the key '%s'"
                % (self._i, self._d, self._k)]
    
    def answer(self):
        return "%s['%s'] = %i" % (self._d, self._k, self._i)

    def check_answer(self, answer):
        try:
            env = {self._d : {}}
            exec(answer, env)
            return env[self._d][self._k] == self._i
        except:
            return False

dictstore = DictStore()

class ListLiteral(Card):

    def question(self):
        return ["Write an expression for a list with three values, the strings 'one', 'two', and 'three', in that order"]

    def answer(self):
        return "['one','two','three']"

    def check_answer(self, answer):
        try:
            return eval(answer, {}) == ['one','two','three']
        except:
            return False

listliteral = ListLiteral()

class ListLiteralOne(Card):

    def reset(self):
        self._val = random.choice(["potato", "eggplant", "brush", "teapot"])

    def question(self):        
        return ["Write an expression for a list with one value, the string '%s'" % self._val]

    def answer(self):
        return "['%s']" % self._val

    def check_answer(self, answer):
        try:
            return eval(answer, {}) == [self._val]
        except:
            return False

listliteralone = ListLiteralOne()

class TryTest(Card):
    code = textwrap.dedent("""\
    def int_or_zero(i):
        \""" If i is convertable to an
        integer, return that integer.
        Otherwise, return 0.
        \"""
        
        try:
            return int(i)
        %s
            return 0""")
            
    def question(self):
        return (["What goes in the blank to make the function docstring accurate?"]
                + (TryTest.code % '____________').splitlines())

    def answer(self):
        return "except ValueError:"

    def check_answer(self, answer):
        code = (TryTest.code % answer) + "\nx=int_or_zero('10')\ny=int_or_zero('ten')"
        d = {}
        try:
            exec(code, d)
            return d['x'] == 10 and d['y'] == 0
        except:
            return False
trytest = TryTest()
        
class Doom(Card):

    gircode = textwrap.dedent("""\
    gir = ''
    %s
        gir += 'doom'
    """)

    def question(self):
        return (["Consider the code:"] +
                (Doom.gircode % '______________').splitlines() +
                ["What goes in the blank to make the variable gir have the value 'doomdoomdoomdoomdoom' by the end of it?"])
    
    def answer(self):
        return "for i in range(5):"

    def check_answer(self, answer):
        d = {}
        try:
            exec(Doom.gircode % answer, d)
            return d['gir'] == "doomdoomdoomdoomdoom"
        except:
            return False

doom = Doom()

class Append(Card):
    def reset(self):
        self._var = self.varname()

    def question(self):
        return ["If %s is a list, write a statement to add the string 'zzz' as the last element of it" % self._var]

    def answer(self):
        return "%s.append('zzz')" % self._var

    def check_answer(self, answer):
        try:
            l = ['xxx','yyy']
            exec(answer, {self._var : l})
            return l == ['xxx','yyy','zzz']
        except:
            return False

append = Append()

whatloop1 = ExpectString("""\
                         What kind of loop would you use to do something
                         to every number from 0 to 100?""", "for")
whatloop2 = ExpectString("""\
                         What kind of loop would you use to do something
                         to every element in a list?""", "for")
whatloop3 = ExpectString("""\
                         What kind of loop would you use to keep asking
                         the user for input until the user typed 'done'?""", "while")
testing1 = ExpectString("A test designed without looking at the relevant code is a ________ test.", "black box")
testing2 = ExpectString("A test designed to verify the behavior of a small part of a larger program is a ________ test.", "unit")
whattype1 = ExpectString("What type does range(10) return?", "list")
whattype2 = ExpectString("What type does raw_input('Tell me something: ') return?", "string")
keyword1 = ExpectString("What keyword do you use to immediately exit a loop, but not exit the function?", "break")
keyword2 = ExpectString("What keyword do you use to immediately start a new loop iteration, without executing the rest of the current iteration?", "continue")

q = """\
 
def div_3(x):
    return x % 3 == 0
 
"""
docstring = MultipleChoice(["Which would make the best docstring for this function?"] + q.splitlines(),
                           "Returns True if and only if x is divisible by 3",
                           ["Mods x by 3 and then returns whether that is equal to 0",
                           "Divides x by 3",
                           "Returns 3",
                           "Returns 0"])


DECK = [whatloop1, whatloop2, whatloop3, whattype1, whattype2, assignemptylist, assignemptydict,
        rangecard, intcast, testing1, testing2, listlen, firstelt, lastelt, doom, dictlookup,
        dictindirect, dictstore, keyword1, keyword2, append, listliteral, listliteralone, trytest,
        docstring]

def check(deck):
    for card in deck:
        card.reset()
        if not card.check_answer(card.answer()):
            print card.question()
            raise Exception("Card above has a wrong answer")

def main():
    print """\
    Welcome to Transcode flash cards!

    This program will keep showing you cards, and giving you a chance
    to type in your answer.  Each correct answer is worth five points,
    and each incorrect answer takes away a quarter of your points, but
    shows you an example of a correct answer so that you can get it
    the next time that card comes up.

    This program will keep running until you hit control-d
    """
    check(DECK)
    score = 0
    done = False
    deck = DECK
    failures = []
    while not done:
        deck = copy.copy(deck + failures)
        random.shuffle(deck)
        for card in deck:
            try: 
                success = card.play()
            except EOFError:
                print "Ok, we're done for now"
                done = True
                break
            if success:
                score += 5
            else:
                failures.append(card)
                score = (score*3)/4
            print "Your score is %i\n" % score

if __name__ == '__main__':
    main()
