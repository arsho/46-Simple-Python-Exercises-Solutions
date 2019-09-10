"""
Statement:
======================
Define a function custom_max()  that takes two numbers as arguments and returns
the largest of them. Use the if­then­else construct available in Python.
(It is true that Python has the custom_max()  function built in, but writing it
yourself is nevertheless a good exercise.)
"""

import unittest


def is_valid_type(data):
    if not isinstance(data, int) and not isinstance(data, float):
        return False
    return True


def custom_max(num1, num2):
    if not is_valid_type(num1) or not is_valid_type(num2):
        raise TypeError("Both parameters should be integer or float.")
    if num1 > num2:
        return num1
    else:
        return num2


# Below is the tests of the problem. Use the test cases to test your solution


class TestCustomMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(custom_max(3, 69), 69, "custom_max(3, 69) = 69")
        self.assertEqual(custom_max(69, 3), 69, "custom_max(69, 3) = 69")

    def test_negative_numbers(self):
        self.assertEqual(custom_max(-69, 3), 3, "custom_max(-69, 3) = 3")
        self.assertEqual(custom_max(-69, -3), -3, "custom_max(-69, -3) = -3")

    def test_exceptions(self):
        with self.assertRaises(TypeError) as te_1:
            custom_max("-69", 3)
        te_1_exception = te_1.exception
        self.assertEqual("{}".format(te_1_exception),
                         "Both parameters should be integer or float.")

        with self.assertRaises(TypeError) as te_2:
            custom_max("-69", "3")
        te_2_exception = te_2.exception
        self.assertEqual("{}".format(te_2_exception),
                         "Both parameters should be integer or float.")

        with self.assertRaises(TypeError) as te_3:
            custom_max(23, "-69")
        te_3_exception = te_3.exception
        self.assertEqual("{}".format(te_3_exception),
                         "Both parameters should be integer or float.")


if __name__ == "__main__":
    unittest.main()
