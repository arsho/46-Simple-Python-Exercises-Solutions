"""
Statement:
======================
Write a function that takes a character (i.e. a string of length 1) and
returns True if it is a vowel, False otherwise.
"""

import unittest


def is_valid_type_and_length(data: str) -> bool:
    """
    Checks if data is a single string type character
    :param data: input data
    :type data: str
    :return: True if data is a single type character, False otherwise
    :rtype: bool
    """
    if not isinstance(data, str) or len(data) != 1:
        return False
    return True


def check_vowel(single_char: str) -> bool:
    """
    :param: single_char: single character to check if it is a vowel
    :type single_char: str
    :rtype: bool
    """
    if not is_valid_type_and_length(single_char):
        raise TypeError("Parameter should be a single character.")
    single_char = single_char.lower()
    return single_char in ['a', 'e', 'i', 'o', 'u']


# Below is the tests of the problem. Use the test cases to test your solution

class TestCheckVowel(unittest.TestCase):
    def test_vowel(self):
        self.assertEqual(check_vowel('a'), True,
                         "check_vowel('a') = True")
        self.assertEqual(check_vowel('e'), True,
                         "check_vowel('e') = True")
        self.assertEqual(check_vowel('i'), True,
                         "check_vowel('i') = True")
        self.assertEqual(check_vowel('o'), True,
                         "check_vowel('o') = True")
        self.assertEqual(check_vowel('u'), True,
                         "check_vowel('u') = True")
        self.assertEqual(check_vowel('A'), True,
                         "check_vowel('A') = True")
        self.assertEqual(check_vowel('E'), True,
                         "check_vowel('E') = True")
        self.assertEqual(check_vowel('I'), True,
                         "check_vowel('I') = True")
        self.assertEqual(check_vowel('O'), True,
                         "check_vowel('O') = True")
        self.assertEqual(check_vowel('U'), True,
                         "check_vowel('U') = True")

    def test_non_vowel(self):
        self.assertEqual(check_vowel('Q'), False,
                         "check_vowel('Q') = False")
        self.assertEqual(check_vowel('q'), False,
                         "check_vowel('q') = False")
        self.assertEqual(check_vowel('Z'), False,
                         "check_vowel('Z') = False")
        self.assertEqual(check_vowel('z'), False,
                         "check_vowel('z') = False")
        self.assertEqual(check_vowel('!'), False,
                         "check_vowel('!') = False")
        self.assertEqual(check_vowel('!'), False,
                         "check_vowel('!') = False")
        self.assertEqual(check_vowel('4'), False,
                         "check_vowel('4') = False")
        self.assertEqual(check_vowel('y'), False,
                         "check_vowel('y') = False")

    def test_exceptions(self):
        with self.assertRaises(TypeError) as te_1:
            check_vowel('Quality')
        te_1_exception = te_1.exception
        self.assertEqual("{}".format(te_1_exception),
                         "Parameter should be a single character.")

        with self.assertRaises(TypeError) as te_2:
            check_vowel(23)
        te_2_exception = te_2.exception
        self.assertEqual("{}".format(te_2_exception),
                         "Parameter should be a single character.")

        with self.assertRaises(TypeError) as te_3:
            check_vowel(5.5)
        te_3_exception = te_3.exception
        self.assertEqual("{}".format(te_3_exception),
                         "Parameter should be a single character.")


if __name__ == "__main__":
    unittest.main()
