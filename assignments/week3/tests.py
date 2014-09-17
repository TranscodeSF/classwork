import unittest
import markov

class TestMarkov(unittest.TestCase):

    def test_split(self):
        res = markov.split_words_and_punctuation("This is a test.")
        self.assertEqual(res, ['This', 'is', 'a', 'test', '.'])
        res = markov.split_words_and_punctuation("")
        self.assertEqual(res, [])
        res = markov.split_words_and_punctuation(".!?x'")
        self.assertEqual(res, ['.', '!', '?', 'x', '\''])
        res = markov.split_words_and_punctuation("Isn't can't shan't won't")
        self.assertEqual(res, ["Isn't", "can't", "shan't", "won't"])

    def test_add_word(self):
        d = {}
        markov.add_word(d, 'foo', 'bar')
        self.assertEqual(d, {'foo':['bar']})
        markov.add_word(d, 'foo', 'bar')
        self.assertEqual(d, {'foo':['bar', 'bar']})
        markov.add_word(d, 'foo', 'baz')
        self.assertEqual(d, {'foo':['bar', 'bar', 'baz']})
        markov.add_word(d, 'quux', 'moose')
        self.assertEqual(d, {'foo':['bar', 'bar', 'baz'], 'quux':['moose']})

    def test_table_of_next_words(self):
        d = markov.table_of_next_words("a a b c a b")
        self.assertEqual(d, { None: ['a'],
                              'a': ['a', 'b', 'b'],
                              'b': ['c', None],
                              'c': ['a'] })
        d = markov.table_of_next_words("")
        self.assertEqual(d, { None: [None] })

    def test_pick_random_element(self):
        elements = ['a', 'b', 'c', 'd', 'e']
        found = []
        for x in range(1000):
            elt = markov.pick_random_element(elements)
            if elt not in found:
                found.append(elt)
            if elt not in elements:
                self.fail("Picked an element that was not in the list: %s" % elt)
        self.assertEqual(len(found), len(elements),
                         "Expected all the elements in %s after 1000 tries, but found only %s"%(elements, found))
   
if __name__ == '__main__':
    unittest.main()
