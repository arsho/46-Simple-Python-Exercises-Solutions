"""
The function max()from exercise 1) and the function
max_of_three()from exercise 2) will only work for
two and three numbers, respectively. But
suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many
they are? Write a function max_in_list()that takes a
list of numbers and returns the largest one
"""
import unittest


def max_in_list(numbers):
    if len(numbers) > 0:
        max_number = numbers[0]
        for i in numbers:
            if i > max_number:
                max_number = i
        return max_number
    return None


def max_in_list_alternative_1(numbers):
    if len(numbers) > 0:
        return max(numbers)
    return None


def max_in_list_alternative_2(numbers):
    if len(numbers) > 0:
        return sorted(numbers)[-1]
    return None


class TestMaxInList(unittest.TestCase):
    def setUp(self):
        self.input_list_1 = [3, 7, 98, 34, 12, 14]
        self.expected_solution_1 = 98
        self.input_list_2 = [-3, -7, -98, -34, -12, -14]
        self.expected_solution_2 = -3
        self.input_list_3 = [-3, 7, -98, 34, 12, 14, 0]
        self.expected_solution_3 = 34
        self.input_list_4 = [0, 0, 0]
        self.expected_solution_4 = 0
        self.input_list_5 = [-10, -10, -10]
        self.expected_solution_5 = -10
        self.input_list_6 = []
        self.expected_solution_6 = None

    def test_max_in_list(self):
        self.assertEqual(max_in_list(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(max_in_list(self.input_list_2),
                         self.expected_solution_2)
        self.assertEqual(max_in_list(self.input_list_3),
                         self.expected_solution_3)
        self.assertEqual(max_in_list(self.input_list_4),
                         self.expected_solution_4)
        self.assertEqual(max_in_list(self.input_list_5),
                         self.expected_solution_5)
        self.assertEqual(max_in_list(self.input_list_6),
                         self.expected_solution_6)

    def test_max_in_list_alternative_1(self):
        self.assertEqual(max_in_list_alternative_1(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(max_in_list_alternative_1(self.input_list_2),
                         self.expected_solution_2)
        self.assertEqual(max_in_list_alternative_1(self.input_list_3),
                         self.expected_solution_3)
        self.assertEqual(max_in_list_alternative_1(self.input_list_4),
                         self.expected_solution_4)
        self.assertEqual(max_in_list_alternative_1(self.input_list_5),
                         self.expected_solution_5)
        self.assertEqual(max_in_list_alternative_1(self.input_list_6),
                         self.expected_solution_6)

    def test_max_in_list_alternative_2(self):
        self.assertEqual(max_in_list_alternative_2(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(max_in_list_alternative_2(self.input_list_2),
                         self.expected_solution_2)
        self.assertEqual(max_in_list_alternative_2(self.input_list_3),
                         self.expected_solution_3)
        self.assertEqual(max_in_list_alternative_2(self.input_list_4),
                         self.expected_solution_4)
        self.assertEqual(max_in_list_alternative_2(self.input_list_5),
                         self.expected_solution_5)
        self.assertEqual(max_in_list_alternative_2(self.input_list_6),
                         self.expected_solution_6)


if __name__ == "__main__":
    unittest.main()
