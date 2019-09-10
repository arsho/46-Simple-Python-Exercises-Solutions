"""
Statement:
======================
Define a function max_of_three() that takes three numbers as arguments and
returns the largest of them.
"""
from typing import Union
import unittest


def is_valid_type(data: Union[int, float]) -> bool:
    """
    Checks if the parameter is valid data type
    :param data: input parameter
    :type data: int or float
    :return: returns True if data is int or float, False otherwise
    :rtype: boolean
    """
    if not isinstance(data, int) and not isinstance(data, float):
        return False
    return True


def max_of_three(num1, num2, num3):
    if not is_valid_type(num1) or not is_valid_type(num2) or \
            not is_valid_type(num3):
        raise TypeError("All parameters should be integer or float.")
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num


# Below is the tests of the problem. Use the test cases to test your solution

class TestMaxOfThree(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_of_three(3, 69, 33), 69,
                         "max_of_three(3, 69, 33) = 69")
        self.assertEqual(max_of_three(69, 3, 33), 69,
                         "max_of_three(69, 3, 33) = 69")

    def test_negative_numbers(self):
        self.assertEqual(max_of_three(-69, 3, -32), 3,
                         "max_of_three(-69, 3, -32) = 3")
        self.assertEqual(max_of_three(-69, -3, -32), -3,
                         "max_of_three(-69, -3, -32) = -3")

    def test_exceptions(self):
        with self.assertRaises(TypeError) as te_1:
            max_of_three("-69", 3, 32)
        te_1_exception = te_1.exception
        self.assertEqual("{}".format(te_1_exception),
                         "All parameters should be integer or float.")

        with self.assertRaises(TypeError) as te_2:
            max_of_three("-69", "3", "2")
        te_2_exception = te_2.exception
        self.assertEqual("{}".format(te_2_exception),
                         "All parameters should be integer or float.")

        with self.assertRaises(TypeError) as te_3:
            max_of_three(23, "-69", 43)
        te_3_exception = te_3.exception
        self.assertEqual("{}".format(te_3_exception),
                         "All parameters should be integer or float.")


if __name__ == "__main__":
    unittest.main()
