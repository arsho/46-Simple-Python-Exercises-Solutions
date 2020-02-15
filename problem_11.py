"""
Define a function generate_n_chars()that takes
an integer n and a character c and returns a string,
n characters long, consisting only of c:s. For
example, generate_n_chars(5,"x")should return
the string "xxxxx". (Python is unusual
in that you can actually write an expression
5 * "x"that will evaluate to
"xxxxx". For the sake of the exercise you should
ignore that the problem can
be solved in this manner.)
"""
import unittest


def generate_n_chars(n, c):
    s = ''
    for i in range(n):
        s += c
    return s


def generate_n_chars_alternative(n, c):
    s = ''.join([c for _ in range(n)])
    return s


class TestGenerateNChars(unittest.TestCase):
    def setUp(self):
        self.c = "x"
        self.n = 5
        self.expected_solution = "xxxxx"

    def test_generate_n_chars(self):
        self.assertEqual(generate_n_chars(self.n, self.c),
                         self.expected_solution)

    def test_generate_n_chars_alternative(self):
        self.assertEqual(generate_n_chars_alternative(self.n, self.c),
                         self.expected_solution)


if __name__ == "__main__":
    unittest.main()
