"""
Define a procedure histogram() that takes a list of
integers and prints a histogram to the screen.
For example, histogram([4, 9, 7])should print the following:

****
*********
*******
"""
import unittest


def histogram(list_var):
    s = ""
    for i in list_var:
        s += '*' * i + "\n"
    # remove the last new line
    return s[:-1]


def histogram_alternative(list_var):
    s = '\n'.join(['*' * i for i in list_var])
    return s


class TestHistogram(unittest.TestCase):
    def setUp(self):
        self.input_list = [4, 9, 7]
        self.expected_solution = "****\n" + \
                                 "*********\n" + \
                                 "*******"

    def test_histogram(self):
        self.assertEqual(histogram(self.input_list),
                         self.expected_solution)

    def test_histogram_alternative(self):
        self.assertEqual(histogram_alternative(self.input_list),
                         self.expected_solution)


if __name__ == "__main__":
    unittest.main()
