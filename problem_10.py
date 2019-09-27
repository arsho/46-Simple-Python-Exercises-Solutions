'''
Define a function overlapping()that takes two lists
and returns True if they have at least one member
in common, False otherwise. You may use your
is_member()function, or the in operator, but for the
sake of the exercise, you should (also) write
it using two nested for-loops
'''
import unittest


def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def overlapping_alternative_1(list1, list2):
    return len([i for i in list1 if i in list2]) > 0


def overlapping_alternative_2(list1, list2):
    return bool(set(list1).intersection(set(list2)))


class TestOverlapping(unittest.TestCase):
    def setUp(self):
        self.a = [3, 4, 5, 6, 7]
        self.b = [6, 7, 8, 9, 10]
        self.c = [91, 92, 93]

    def test_overlapping(self):
        self.assertEqual(overlapping(self.a, self.b), True)
        self.assertEqual(overlapping(self.a, self.c), False)

    def test_overlapping_alternative_1(self):
        self.assertEqual(overlapping_alternative_1(self.a, self.b), True)
        self.assertEqual(overlapping_alternative_1(self.a, self.c), False)

    def test_overlapping_alternative_2(self):
        self.assertEqual(overlapping_alternative_2(self.a, self.b), True)
        self.assertEqual(overlapping_alternative_2(self.a, self.c), False)


if __name__ == "__main__":
    unittest.main()
