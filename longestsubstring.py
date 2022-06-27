import unittest

def longestsubstring(word):
    if not isinstance(word, str):
        return False
    if len(set(word)) == len(word):
        return len(word)
    # last index of every character
    last_idx = {}
    max_len = 0  
    # sliding window
    start_idx = 0
  
    for i in range(0, len(word)):
        
        # Slide window if character is repeating
        if word[i] in last_idx:
            start_idx = max(start_idx, last_idx[word[i]] + 1)  
        # Compare window to the last longest sub
        max_len = max(max_len, i-start_idx + 1)  
        # Update last index of current char.
        last_idx[word[i]] = i
  
    return max_len


class TestSubstring(unittest.TestCase):

    def test_set(self):
        self.assertEqual(longestsubstring('ABCDEFGHIJKL'), 12)

    def test_length_4(self):
        self.assertEqual(longestsubstring('abcabcdcx'), 4)
    
    def test_length_1(self):
        self.assertEqual(longestsubstring('bbbbb'), 1)

    def test_boolean(self):
        self.assertEqual(longestsubstring(True), 0)

    def test_int(self):
        self.assertEqual(longestsubstring(True), 0)
