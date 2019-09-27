"""
Define a function reverse()that computes the reversal
of a string. For example, reverse("I am testing")
should return the string "gnitset ma I".
"""
import unittest


def reverse(s):
    s_length = len(s)
    reversed_s = ''
    for i in range(s_length - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s

def reverse_short(passed_string):
    return passed_string[::-1]


# Below is the tests of the problem. Use the test cases to test your solution

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("I am testing"), "gnitset ma I")

    def test_reverse_short(self):
        self.assertEqual(reverse_short("I am testing"), "gnitset ma I")

if __name__ == "__main__":
    unittest.main()
