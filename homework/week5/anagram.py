def getwords():
    """
    Returns a list of words in our (included) dictionary.
    """
    words = []
    with open('2of12inf.txt', 'r') as f:
        for word in f:
            words.append(word.strip())
        words.sort()
    return words

def normalize(letters):
    """
    Since anagrams only care about what letters they have to work with, and
    not the order of them, this function returns the same string for any
    set of letters that are the same.  It removes any non-alphabetic characters.
    """
    lst = []
    for c in letters:
        lst.append(c)
    lst.sort()
    return "".join(lst)

def remove_letters(remove, bank):
    """
    Removes some letters from the letter bank

    Parameters:
    remove - the set of letters to remove from the letter bank
    bank - the letter bank

    Returns the contents of bank without all lettters in remove.  If a
    letter occurs in bank more than once, only the number of instances
    that occur in remove are removed.

    If the bank does not have enough letters such that every specified
    letter can be removed, this function returns None
    """
    for letter in remove:
        if letter not in bank:
            return None
        before, sep, after = bank.partition(letter)
        bank = before + after
    return bank

def anagrams(letters, words, min_length=3, memo = {}):
    """
    Find anagrams of a phrase.

    Parameters:
    letters - the letters to anagram, in a string
    words - the word bank, a list of valid words for anagrams
    min_length - (optional) the minimum length of word to allow
        in an anagram
    memo - (for internal use) the previously-found anagrams for
        already-tested combinations of letters

    Return all possibly multi-word anagrams of the phrase given in
    letters, as strings containing english phrases (which contain only
    real words, though the phrases may not make sense).  Only the
    alphabetic characters in letters are used, any spaces or
    punctuation is ignored.
    """
    # empty means no anagrams
    if not letters:
        return []
    letters = normalize(letters)
    # see if we've done this before
    if letters in memo:
        return memo[letters]
    candidate_words = []
    remainders = []
    # find all the words that could be part of an anagram, and what's left over for each.
    for word in words:
        if len(word) < min_length:
            continue
        remainder = remove_letters(word, letters)
        if remainder != None:
            candidate_words.append(word)
            remainders.append(remainder)
    # build up a list of anagrams
    results = []
    for word, remainder in zip(candidate_words, remainders):
        if remainder == "":
            # base case: if there are no letters left after we use this word,
            # the anagram is just the whole word.
            results.append(word)
        else:
            # recursive case: find all anagrams of the remaining letters, and
            # include this word at the beginning of each of them
            sub_anagrams = anagrams(remainder, candidate_words, min_length, memo)
            for ana in sub_anagrams:
                results.append(word + ana)
    # save the answer and return
    memo[letters] = results
    return results


