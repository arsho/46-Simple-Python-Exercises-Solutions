'''
Write a function is_member()that takes a value
(i.e. a number, string, etc) x and a list of
values a, and returns True if x is a member of a,
False otherwise.(Note that this is exactly what
the in operator does, but for the sake of the
exercise you should pretend Python did not
have this operator.)
'''
import unittest


def is_member(item, items):
    items_length = len(items)
    for i in range(items_length):
        if item == items[i]:
            return True
    return False


class TestIsMember(unittest.TestCase):
    def test_is_member(self):
        abc = [1, 4, 6, 9, 34]
        self.assertEqual(is_member(9, abc), True)
        self.assertEqual(is_member(11, abc), False)


if __name__ == "__main__":
    unittest.main()
