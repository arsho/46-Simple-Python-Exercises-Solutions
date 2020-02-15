"""
 Write a function char_freq()that takes a string and
 builds a frequency listing of the characters contained
 in it. Represent the frequency listing as a Python
 dictionary. Try it with something like
 char_freq("abbabcbdbabdbdbabababcbcbab")
 """
import collections
import unittest


def char_freq(passed_string):
    char_freq_dic = dict()
    for c in passed_string:
        if c in char_freq_dic.keys():
            char_freq_dic[c] = char_freq_dic.get(c) + 1
        else:
            char_freq_dic[c] = 1
    char_sorted_dic = sorted(char_freq_dic.items())
    return char_sorted_dic


def char_freq_alternative(passed_string):
    return sorted(collections.Counter(list(passed_string)).items())


class TestCharFrequency(unittest.TestCase):
    def test_char_freq(self):
        line_of_chars = "abbabcbdbabdbdbabababcbcbab"
        expected_frequencies = [('a', 7), ('b', 14), ('c', 3), ('d', 3)]
        frequencies = char_freq(line_of_chars)
        self.assertEqual(
            frequencies, expected_frequencies
        )
        frequencies = char_freq_alternative(line_of_chars)
        self.assertEqual(
            frequencies, expected_frequencies
        )


if __name__ == "__main__":
    unittest.main()
