"""
Statement:
======================
Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers.
For example,
sum([1, 2, 3, 4]) should return 10, and
multiply([1, 2, 3, 4]) should return 24.
"""
from functools import reduce
import unittest


def custom_sum(num_list: list) -> int:
    """
    Returns the sum of a list
    :param num_list: input data
    :type num_list: list
    :return: total
    :rtype: int
    """
    total = 0
    for c in num_list:
        total += c
    return total


def custom_sum_using_reduce(nums: list) -> int:
    """
    Returns the sum of a list using Python3's reduce
    :param nums: input data
    :type nums: list
    :return: total
    :rtype: int
    """
    return reduce(lambda a, b: a + b, nums)


def multiply(num_list: list) -> int:
    """
    Returns multiplication value of a list
    :param num_list: input data
    :type num_list: list
    :return: total
    :rtype: int
    """
    total = 1
    for c in num_list:
        total *= c
    return total


def multiply_using_reduce(num_list: list) -> int:
    """
    Returns multiplication value of a list
    :param num_list: input data
    :type num_list: list
    :return: total
    :rtype: int
    """
    return reduce(lambda a, b: a * b, num_list, 1)


# Below is the tests of the problem. Use the test cases to test your solution

class TestFunctions(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum([1, 2, 3, 4]), 10)
        self.assertEqual(custom_sum([0]), 0)

    def test_custom_sum_using_reduce(self):
        self.assertEqual(custom_sum_using_reduce([1, 2, 3, 4]), 10)
        self.assertEqual(custom_sum_using_reduce([0]), 0)

    def test_multiply(self):
        self.assertEqual(multiply([1, 2, 3, 4]), 24)
        self.assertEqual(multiply([1, 2, 3, 4, 0]), 0)
        self.assertEqual(multiply([1, 2, 3, 4, -1]), -24)
        self.assertEqual(multiply([1, 2, 3, 4, -1, -1]), 24)

    def test_multiply_using_reduce(self):
        self.assertEqual(multiply_using_reduce([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_using_reduce([1, 2, 3, 4, 0]), 0)
        self.assertEqual(multiply_using_reduce([1, 2, 3, 4, -1]), -24)
        self.assertEqual(multiply_using_reduce([1, 2, 3, 4, -1, -1]), 24)


if __name__ == "__main__":
    unittest.main()
