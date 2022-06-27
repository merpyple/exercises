import unittest
import string

def is_palindrome(word):
    if not isinstance(word, str):
        return False
    cleaned_string = word.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "")
    if len(cleaned_string)==0:
        return False
    return cleaned_string[::-1]==cleaned_string

class TestPalindrome(unittest.TestCase):

    def test_string_palindrome(self):
        self.assertEqual(is_palindrome('refer'), True)

    def test_string_not_palindrome(self):
        self.assertEqual(is_palindrome('refers'), False)

    def test_empty(self):
        self.assertEqual(is_palindrome(' '), False)

    def test_string_int(self):
        self.assertEqual(is_palindrome(321123), False) 
    
    def test_string_none(self):
        self.assertEqual(is_palindrome(None), False)

    def test_list(self):
        self.assertEqual(is_palindrome(['ref','er']), False)

    def test_sentence(self):
        self.assertEqual(is_palindrome("Delia saw I was ailed."), True)

    def test_sentence_punctuation(self):
        self.assertEqual(is_palindrome("Wonton? Not now!"), True)

    def test_sentence_not(self):
        self.assertEqual(is_palindrome("Ah. Satan seeks Natasha."), False)
