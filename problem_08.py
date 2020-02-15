"""
Define a function is_palindrome()that recognizes
palindromes (i.e. words that look the same written
backwards). For example, is_palindrome("radar")
should return True
"""

import unittest


def is_palindrome(line):
    reverse_line = ''
    line_length = len(line)
    for i in range(line_length - 1, -1, -1):
        reverse_line += line[i]
    return line == reverse_line


def is_palindrome_short(line):
    return line == line[::-1]


# Below is the tests of the problem. Use the test cases to test your solution

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("radar"), True)
        self.assertEqual(is_palindrome("abcde"), False)
        self.assertEqual(is_palindrome(""), True)

    def test_is_palindrome_short(self):
        self.assertEqual(is_palindrome_short("radar"), True)
        self.assertEqual(is_palindrome_short("abcde"), False)
        self.assertEqual(is_palindrome_short(""), True)


if __name__ == "__main__":
    unittest.main()
