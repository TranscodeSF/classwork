import unittest

def word_with_blanks(word, letters):
    out = ""
    for letter in word:
        if letter in letters:
            out = out + letter
        else:
            out = out + "_"
    return out

class TestWordWithBlanks(unittest.TestCase):
    def test_no_letters(self):
        self.assertEqual(word_with_blanks("potato", ""), "______")

    def test_all_letters(self):
        self.assertEqual(word_with_blanks("potato", "ptoa"), "potato")

    def test_one_letter(self):
        self.assertEqual(word_with_blanks("potato", "p"), "p_____")

    def test_with_wrong_letters(self):
        self.assertEqual(word_with_blanks("potato", "x"), "______")

    def test_repeated_letter(self):
        self.assertEqual(word_with_blanks("potato", "t"), "__t_t_")

    def test_some_letters(self):
        self.assertEqual(word_with_blanks("potato", "pto"), "pot_to")

    def test_empty_word(self):
        self.assertEqual(word_with_blanks("", ""), "")
        self.assertEqual(word_with_blanks("", "xyz"), "")

if __name__ == '__main__':
    unittest.main()
