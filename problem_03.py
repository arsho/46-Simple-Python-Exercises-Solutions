"""
Statement:
======================
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it
yourself is nevertheless a good exercise.)
"""
from typing import Union
import unittest


def is_valid_type(data):
    if not isinstance(data, str) and not isinstance(data, list):
        return False
    return True


def custom_len(given_list_or_string: Union[list, str]) -> int:
    """

    :rtype: int
    :raise TypeError: Parameter should be list or string type
    """
    if not is_valid_type(given_list_or_string):
        raise TypeError("Parameter should be list or string type")
    cnt = 0
    for _ in given_list_or_string:
        cnt += 1
    return cnt


# Below is the tests of the problem. Use the test cases to test your solution

class TestCustomLen(unittest.TestCase):
    def test_list_length(self):
        self.assertEqual(custom_len([3, 69, 33]), 3,
                         "custom_len([3, 69, 33]) = 3")
        self.assertEqual(custom_len([3, 69, 33, -32]), 4,
                         "custom_len([3, 69, 33, -32]) = 4")
        self.assertEqual(custom_len([]), 0,
                         "custom_len([]) = 0")

    def test_string_length(self):
        self.assertEqual(custom_len("shovon"), 6,
                         "custom_len('shovon') = 6")
        self.assertEqual(custom_len("arsho"), 5,
                         "custom_len('arsho') = 5")
        self.assertEqual(custom_len(""), 0,
                         "custom_len('') = 6")

    def test_exceptions(self):
        with self.assertRaises(TypeError) as te_1:
            custom_len(5)
        te_1_exception = te_1.exception
        self.assertEqual("{}".format(te_1_exception),
                         "Parameter should be list or string type")

        with self.assertRaises(TypeError) as te_2:
            custom_len(5.6)
        te_2_exception = te_2.exception
        self.assertEqual("{}".format(te_2_exception),
                         "Parameter should be list or string type")

        with self.assertRaises(TypeError) as te_3:
            custom_len((23, 43))
        te_3_exception = te_3.exception
        self.assertEqual("{}".format(te_3_exception),
                         "Parameter should be list or string type")


if __name__ == "__main__":
    unittest.main()
